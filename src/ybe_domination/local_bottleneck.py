from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from .context_retraction import (
    context_coretraction_audit,
    context_retraction_audit,
    direct_product_witness,
    product_permutation_witness,
)
from .detector_candidates import two_sided_green_detector_groups
from .finite_group import FiniteGroup, cyclic_group, direct_product_group
from .group_laws import group_exponent
from .label_detectors import direct_product_label_group, swapped_product_label_group
from .local_interval import (
    LocalInterval,
    coordinate_kernel_pair_closure_audits,
    coordinate_kernel_seed_pairs,
    generated_admissible_congruence_audit,
)
from .local_models import solution_from_local_interval
from .product_permutation import (
    direct_product_holonomy_summary,
    identity_base_swapped_reduction,
    swapped_product_holonomy_summary,
)
from .small_search import branch_tags, known_branch_detector_certificate


# Only tags with a symbolic all-n finite-G detector belong here.  Audit tags
# such as "affine_cyclic" are deliberately excluded unless another tag in this
# set, or a product-specific closed subbranch, supplies the detector proof.
KNOWN_TOTAL_DETECTOR_TAGS = frozenset(
    {
        "involutive",
        "permutation_form",
        "rack_type",
        "nondegenerate",
    }
)


@dataclass(frozen=True)
class ProductFiniteGDetectorCertificate:
    """Detector bookkeeping for one closed product finite-G subbranch."""

    detail: str
    detector_kind: str
    detector_group: FiniteGroup | None
    detector_group_order: int | None
    sharp_rack_factor_size: int | None
    proof_reference: str
    braid_index_independent: bool

    @property
    def has_explicit_group_order(self) -> bool:
        return self.detector_group_order is not None

    @property
    def has_explicit_group(self) -> bool:
        return self.detector_group is not None


@dataclass(frozen=True)
class LocalMasterBottleneckSummary:
    """A compact ledger for the current local-minimal reduction fork.

    This is not a proof of the master theorem.  It packages the symbolic
    reductions that are already proved or explicitly targeted, so a candidate
    local interval can be routed to the exact remaining obligation.
    """

    colored_ybe: bool
    semisplit_count: int
    local_minimal: bool | None
    local_minimal_error: str | None
    local_minimal_pair_count: int
    local_minimal_pair_failure_count: int
    local_minimal_pair_max_depth: int
    retraction_kind: str
    coretraction_kind: str
    product_branch: str
    product_holonomy_details: Tuple[str, ...]
    output_kernel_kind: str
    output_kernel_stable_depth: int
    output_kernel_pair_count: int
    output_kernel_pair_failure_count: int
    output_kernel_pair_max_depth: int
    all_coordinate_kernel_kind: str
    all_coordinate_kernel_stable_depth: int
    product_detector_certificates: Tuple[ProductFiniteGDetectorCertificate, ...]
    total_branch_tags: Tuple[str, ...]
    known_total_detector_reason: str | None
    known_total_detector_group: FiniteGroup | None
    known_total_detector_group_order: int | None
    known_total_detector_factor_size: int | None
    green_detector_group_orders: Tuple[int, ...]
    verdict: str
    remaining_obligation: str

    @property
    def output_kernel_pairs_all_universal(self) -> bool:
        return self.output_kernel_pair_failure_count == 0

    @property
    def product_detector_group_orders(self) -> Tuple[int, ...]:
        return tuple(
            certificate.detector_group_order
            for certificate in self.product_detector_certificates
            if certificate.detector_group_order is not None
        )

    @property
    def product_detector_groups(self) -> Tuple[FiniteGroup, ...]:
        return tuple(
            certificate.detector_group
            for certificate in self.product_detector_certificates
            if certificate.detector_group is not None
        )

    @property
    def product_detector_gaps(self) -> Tuple[str, ...]:
        return tuple(
            certificate.detail
            for certificate in self.product_detector_certificates
            if certificate.detector_group_order is None
        )

    @property
    def known_total_detector_groups(self) -> Tuple[FiniteGroup, ...]:
        if self.known_total_detector_group is None:
            return tuple()
        return (self.known_total_detector_group,)

    @property
    def closed_detector_groups(self) -> Tuple[FiniteGroup, ...]:
        """Return actual finite groups for closed verdicts when known.

        The returned groups are interval-level detector factors.  They are not
        populated for open corridor/product bottlenecks, and delegated affine
        rows remain visible through ``closed_detector_gaps``.
        """

        if self.verdict == "product_finite_g_branch":
            return self.product_detector_groups
        if self.verdict in {"known_total_branch", "locally_nondegenerate_branch"}:
            return self.known_total_detector_groups
        return tuple()

    @property
    def closed_detector_group_orders(self) -> Tuple[int, ...]:
        return tuple(len(group.elements) for group in self.closed_detector_groups)

    @property
    def closed_detector_product_group(self) -> FiniteGroup | None:
        """Return the single interval detector group when the row is closed."""

        if self.closed_detector_gaps:
            return None
        groups = self.closed_detector_groups
        if not groups:
            return None
        if len(groups) == 1:
            return groups[0]
        return direct_product_group(groups)

    @property
    def closed_detector_product_group_order(self) -> int | None:
        group = self.closed_detector_product_group
        if group is None:
            return None
        return len(group.elements)

    @property
    def closed_detector_gaps(self) -> Tuple[str, ...]:
        if self.verdict == "product_finite_g_branch":
            return self.product_detector_gaps
        if (
            self.verdict in {"known_total_branch", "locally_nondegenerate_branch"}
            and self.known_total_detector_group is None
        ):
            return (self.verdict,)
        return tuple()


def _local_minimal_value(
    interval: LocalInterval,
    max_fibre_size: int,
) -> tuple[bool | None, str | None, int, int, int]:
    try:
        audits = interval.pair_generated_local_minimality_audits()
        failures = [
            audit for audit in audits if audit.generated.kind != "universal"
        ]
        max_depth = max(
            (audit.generated.stable_depth for audit in audits),
            default=0,
        )
        return not failures, None, len(audits), len(failures), max_depth
    except ValueError as exc:
        return None, str(exc), 0, 0, 0


def _product_branch(interval: LocalInterval) -> str:
    has_swapped = product_permutation_witness(interval) is not None
    has_direct = direct_product_witness(interval) is not None
    if has_swapped and has_direct:
        return "swapped_and_direct"
    if has_swapped:
        return "swapped"
    if has_direct:
        return "direct"
    return "none"


def _product_holonomy_detail(
    interval: LocalInterval,
    side: str,
    total_branch_tags: Tuple[str, ...],
) -> str:
    if side == "swapped":
        summary = swapped_product_holonomy_summary(interval)
    elif side == "direct":
        summary = direct_product_holonomy_summary(interval)
    else:
        raise ValueError(f"unknown product side {side!r}")
    if summary.is_trivial:
        return f"{side}_coboundary"
    if (
        side == "swapped"
        and all(
            interval.base_R[(left, right)] == (left, right)
            for left in interval.colors
            for right in interval.colors
        )
    ):
        reduction = identity_base_swapped_reduction(interval)
        if reduction.satisfies_central_form and reduction.prime_cycle_modulus is not None:
            return "swapped_identity_base_cyclic"
    if len(interval.colors) == 1:
        return f"{side}_one_color_pairwise"
    if all(len(interval.fibres[color]) == 2 for color in interval.colors):
        return f"{side}_fibre2_affine"
    if set(total_branch_tags) & KNOWN_TOTAL_DETECTOR_TAGS:
        return f"{side}_genuinely_coloured_known_total"
    return f"{side}_genuinely_coloured_open"


def _product_holonomy_details(
    interval: LocalInterval,
    product_branch: str,
    total_branch_tags: Tuple[str, ...],
) -> Tuple[str, ...]:
    details = []
    if product_branch in {"swapped", "swapped_and_direct"}:
        details.append(_product_holonomy_detail(interval, "swapped", total_branch_tags))
    if product_branch in {"direct", "swapped_and_direct"}:
        details.append(_product_holonomy_detail(interval, "direct", total_branch_tags))
    return tuple(details)


def _sharp_rack_factor_size(group_order: int) -> int:
    return 2 * group_order * group_order


def _cyclic_product_certificate(
    *,
    detail: str,
    detector_kind: str,
    order: int,
    proof_reference: str,
) -> ProductFiniteGDetectorCertificate:
    group = cyclic_group(order)
    return ProductFiniteGDetectorCertificate(
        detail=detail,
        detector_kind=detector_kind,
        detector_group=group,
        detector_group_order=len(group.elements),
        sharp_rack_factor_size=_sharp_rack_factor_size(len(group.elements)),
        proof_reference=proof_reference,
        braid_index_independent=True,
    )


def _product_label_detector_order(interval: LocalInterval, side: str) -> int:
    if side == "swapped":
        group = swapped_product_label_group(interval).group
    elif side == "direct":
        group = direct_product_label_group(interval).group
    else:
        raise ValueError(f"unknown product side {side!r}")
    return group_exponent(group)


def _product_detector_certificate(
    interval: LocalInterval,
    detail: str,
) -> ProductFiniteGDetectorCertificate:
    side = detail.split("_", 1)[0]
    if detail.endswith("_coboundary"):
        return _cyclic_product_certificate(
            detail=detail,
            detector_kind="trivial_coboundary_group",
            order=1,
            proof_reference="proofs/product_coboundary_telescope.md",
        )
    if detail.endswith("_one_color_pairwise"):
        order = _product_label_detector_order(interval, side)
        return _cyclic_product_certificate(
            detail=detail,
            detector_kind="cyclic_pairwise_linking_group",
            order=order,
            proof_reference="proofs/pairwise_linking_detector.md",
        )
    if detail == "swapped_identity_base_cyclic":
        order = identity_base_swapped_reduction(interval).prime_cycle_modulus
        if order is None:
            raise ValueError("identity-base cyclic detail has no cyclic modulus")
        return _cyclic_product_certificate(
            detail=detail,
            detector_kind="cyclic_identity_base_group",
            order=order,
            proof_reference="proofs/identity_base_product_branch.md",
        )
    if detail.endswith("_genuinely_coloured_known_total"):
        known = known_branch_detector_certificate(solution_from_local_interval(interval).total)
        if known is None:
            raise ValueError("known-total product detail has no known detector certificate")
        return ProductFiniteGDetectorCertificate(
            detail=detail,
            detector_kind=f"known_total_{known.detector_kind}",
            detector_group=known.detector_group,
            detector_group_order=known.detector_group_order,
            sharp_rack_factor_size=known.sharp_rack_factor_size,
            proof_reference=known.proof_reference,
            braid_index_independent=True,
        )
    if detail.endswith("_fibre2_affine"):
        return ProductFiniteGDetectorCertificate(
            detail=detail,
            detector_kind="delegated_affine_f2_branch",
            detector_group=None,
            detector_group_order=None,
            sharp_rack_factor_size=None,
            proof_reference="proofs/fibre2_product_branch.md",
            braid_index_independent=True,
        )
    raise ValueError(f"open product detail has no finite-G certificate: {detail}")


def _product_detector_certificates(
    interval: LocalInterval,
    product_holonomy_details: Tuple[str, ...],
) -> Tuple[ProductFiniteGDetectorCertificate, ...]:
    return tuple(
        _product_detector_certificate(interval, detail)
        for detail in product_holonomy_details
        if not detail.endswith("_open")
    )


def _verdict_and_obligation(
    *,
    colored_ybe: bool,
    semisplit_count: int,
    local_minimal: bool | None,
    retraction_kind: str,
    coretraction_kind: str,
    product_branch: str,
    product_holonomy_details: Tuple[str, ...],
    output_kernel_kind: str,
    total_branch_tags: Tuple[str, ...],
) -> tuple[str, str]:
    if not colored_ybe:
        return (
            "invalid_colored_ybe",
            "Reject as a local interval until the coloured YBE is proved.",
        )
    if semisplit_count:
        return (
            "semisplit_leak",
            "Not local-minimal: an equality/universal mixed congruence survives.",
        )
    if local_minimal is None:
        return (
            "local_minimality_unchecked",
            "Full congruence-family enumeration was disabled; supply a symbolic local-minimality proof before routing this interval.",
        )
    if local_minimal is False:
        return (
            "not_local_minimal",
            "Refine the congruence chain before applying the master local theorem.",
        )
    if product_branch in {"swapped", "direct", "swapped_and_direct"}:
        if any(not detail.endswith("_open") for detail in product_holonomy_details):
            return (
                "product_finite_g_branch",
                "Use the closed product subbranch: coboundary telescope, one-colour pairwise cyclic detector, fibre-size-two affine detector, or known total branch.",
            )
        return (
            "product_genuinely_coloured_bottleneck",
            "Product normal form has genuinely coloured holonomy outside current known tags; prove product-label finite-longitude factorization or realize the product B-route.",
        )
    if retraction_kind == "universal" or coretraction_kind == "universal":
        return (
            "product_witness_missing",
            "Audit the universal retraction/coretraction proof against this interval; a product witness should exist.",
        )
    if output_kernel_kind == "equality":
        return (
            "locally_nondegenerate_branch",
            "Use the already bookkept left-nondegenerate/guitar finite-G detector branch.",
        )
    if set(total_branch_tags) & {"involutive", "permutation_form", "rack_type"}:
        return (
            "known_total_branch",
            "Use the whole-solution finite-G detector branch; no Green/corridor factorization is needed for this interval.",
        )
    if output_kernel_kind == "universal":
        return (
            "bi_free_universal_corridor_bottleneck",
            "Prove input-dependent Green/corridor finite-longitude factorization through fixed detector groups, or construct normalized-law B.",
        )
    return (
        "proper_mixed_kernel_closure",
        "If the interval is truly local-minimal this should not occur; audit local-minimality and semisplit/proper mixed families.",
    )


def local_master_bottleneck_summary(
    interval: LocalInterval,
    *,
    max_fibre_size: int = 5,
    max_kernel_degree: int | None = None,
) -> LocalMasterBottleneckSummary:
    """Return the current reduction ledger for one finite local interval.

    The ledger combines:

    - semisplit congruence checks;
    - exact single-pair local-minimality closures, including failure count
      and maximum closure depth;
    - two-sided retraction and coretraction dichotomies;
    - product-permutation witnesses;
    - product holonomy closed/open subbranch details;
    - coordinate-kernel closure;
    - the finite two-sided Green detector group orders.

    The output is meant for proof audits and counterexample triage.  It should
    never be cited as finite-search evidence for the global theorem.
    """

    colored_ybe = interval.is_colored_ybe()
    semisplit_count = len(interval.semisplit_families())
    (
        local_minimal,
        local_minimal_error,
        local_minimal_pair_count,
        local_minimal_pair_failure_count,
        local_minimal_pair_max_depth,
    ) = _local_minimal_value(
        interval,
        max_fibre_size,
    )
    retraction_kind = context_retraction_audit(interval).kind
    coretraction_kind = context_coretraction_audit(interval).kind
    product_branch = _product_branch(interval)
    output_kernel_audit = generated_admissible_congruence_audit(
        interval,
        coordinate_kernel_seed_pairs(
            interval,
            include_coretraction_kernels=False,
        ),
    )
    output_kernel_pair_audits = coordinate_kernel_pair_closure_audits(
        interval,
        include_coretraction_kernels=False,
    )
    output_kernel_pair_failures = tuple(
        audit
        for audit in output_kernel_pair_audits
        if audit.generated.kind != "universal"
    )
    output_kernel_pair_max_depth = max(
        (audit.generated.stable_depth for audit in output_kernel_pair_audits),
        default=0,
    )
    all_coordinate_kernel_audit = generated_admissible_congruence_audit(
        interval,
        coordinate_kernel_seed_pairs(
            interval,
            include_coretraction_kernels=True,
        ),
    )
    qmap = solution_from_local_interval(interval)
    total_tags = branch_tags(qmap.total)
    known_total_certificate = known_branch_detector_certificate(qmap.total)
    product_details = _product_holonomy_details(
        interval,
        product_branch,
        total_tags,
    )
    verdict, obligation = _verdict_and_obligation(
        colored_ybe=colored_ybe,
        semisplit_count=semisplit_count,
        local_minimal=local_minimal,
        retraction_kind=retraction_kind,
        coretraction_kind=coretraction_kind,
        product_branch=product_branch,
        product_holonomy_details=product_details,
        output_kernel_kind=output_kernel_audit.kind,
        total_branch_tags=total_tags,
    )
    if verdict != "bi_free_universal_corridor_bottleneck":
        green_orders = tuple()
    else:
        green_orders = tuple(
            sorted(
                len(group.elements)
                for group in two_sided_green_detector_groups(
                    qmap.total,
                    max_kernel_degree=max_kernel_degree,
                )
            )
        )
    return LocalMasterBottleneckSummary(
        colored_ybe=colored_ybe,
        semisplit_count=semisplit_count,
        local_minimal=local_minimal,
        local_minimal_error=local_minimal_error,
        local_minimal_pair_count=local_minimal_pair_count,
        local_minimal_pair_failure_count=local_minimal_pair_failure_count,
        local_minimal_pair_max_depth=local_minimal_pair_max_depth,
        retraction_kind=retraction_kind,
        coretraction_kind=coretraction_kind,
        product_branch=product_branch,
        product_holonomy_details=product_details,
        output_kernel_kind=output_kernel_audit.kind,
        output_kernel_stable_depth=output_kernel_audit.stable_depth,
        output_kernel_pair_count=len(output_kernel_pair_audits),
        output_kernel_pair_failure_count=len(output_kernel_pair_failures),
        output_kernel_pair_max_depth=output_kernel_pair_max_depth,
        all_coordinate_kernel_kind=all_coordinate_kernel_audit.kind,
        all_coordinate_kernel_stable_depth=all_coordinate_kernel_audit.stable_depth,
        product_detector_certificates=_product_detector_certificates(
            interval,
            product_details,
        ),
        total_branch_tags=total_tags,
        known_total_detector_reason=(
            None if known_total_certificate is None else known_total_certificate.reason
        ),
        known_total_detector_group=(
            None if known_total_certificate is None else known_total_certificate.detector_group
        ),
        known_total_detector_group_order=(
            None
            if known_total_certificate is None
            else known_total_certificate.detector_group_order
        ),
        known_total_detector_factor_size=(
            None
            if known_total_certificate is None
            else known_total_certificate.sharp_rack_factor_size
        ),
        green_detector_group_orders=green_orders,
        verdict=verdict,
        remaining_obligation=obligation,
    )
