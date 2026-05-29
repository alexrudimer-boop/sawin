from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Mapping, Sequence, Tuple

from .artin_longitudes import (
    BraidWord,
    DirectProductLongitudeSubgroupAudit,
    LongitudeSubgroupProfileRow,
    artin_longitudes,
    direct_product_longitude_subgroup_audit,
    longitude_subgroup_profile,
)
from .detector_candidates import two_sided_green_detector_groups
from .detector_candidates import exact_detector_image_audit, ExactImageAudit
from .finite_group import FiniteGroup
from .local_bottleneck import LocalMasterBottleneckSummary, local_master_bottleneck_summary
from .local_interval import LocalInterval
from .local_models import solution_from_local_interval
from .residual import bounded_words, is_identity_action


TARGET_VERDICT = "bi_free_universal_corridor_bottleneck"


@dataclass(frozen=True)
class BiFreeCorridorDetectorTarget:
    """Fixed finite detector data for the remaining corridor branch.

    This is a proof-audit object.  It constructs the finite group factors
    named in the target theorem, but it does not prove the all-degree
    factorization through those factors.
    """

    summary: LocalMasterBottleneckSummary
    applies: bool
    total_size: int
    quotient_size: int
    factor_orders: Tuple[int, ...]
    detector_order: int


@dataclass(frozen=True)
class BiFreeCorridorWordCertificate:
    """Finite-word certificate against the listed corridor detector factors."""

    target: BiFreeCorridorDetectorTarget
    n: int
    braid_word: Tuple[int, ...]
    quotient_fixed: bool
    moved_residual_tuple: Tuple[Tuple[object, ...], Tuple[object, ...], Tuple[object, ...]] | None
    subgroup_profile: Tuple[LongitudeSubgroupProfileRow, ...]

    @property
    def all_listed_factors_invisible(self) -> bool:
        return all(row.identity_longitude_signature for row in self.subgroup_profile)

    @property
    def visible_factor_names(self) -> Tuple[str, ...]:
        return tuple(
            row.name
            for row in self.subgroup_profile
            if not row.identity_longitude_signature
        )

    @property
    def is_b_failure_against_listed_factors(self) -> bool:
        """Return whether this finite word has the B-shape for listed factors.

        A true value is still only finite diagnostic evidence: outcome B
        requires a normalized-law sequence defeating every finite group.
        """

        return (
            self.quotient_fixed
            and self.moved_residual_tuple is not None
            and self.all_listed_factors_invisible
        )


@dataclass(frozen=True)
class BiFreeCorridorProductSubgroupAudit:
    """Compare listed corridor factors with their single direct product."""

    target: BiFreeCorridorDetectorTarget
    n: int
    braid_word: Tuple[int, ...]
    factor_names: Tuple[str, ...]
    factor_orders: Tuple[int, ...]
    factor_identity_signatures: Tuple[bool, ...]
    all_factor_identity_signatures: bool
    product_group_order: int
    truncated: bool
    product_subgroup_size: int | None
    expected_product_subgroup_size: int | None
    product_subgroup_equals_factor_product: bool | None
    product_identity_signature: bool | None
    product_identity_signature_equivalent: bool | None


def bifree_corridor_detector_groups(
    interval: LocalInterval,
    *,
    max_kernel_degree: int | None = None,
) -> Mapping[str, FiniteGroup]:
    """Return named finite factors for the corridor detector candidate."""

    qmap = solution_from_local_interval(interval)
    groups = two_sided_green_detector_groups(
        qmap.total,
        max_kernel_degree=max_kernel_degree,
    )
    return {
        f"H{index + 1}_order_{len(group.elements)}": group
        for index, group in enumerate(groups)
    }


def bifree_corridor_detector_target(
    interval: LocalInterval,
    *,
    max_kernel_degree: int | None = None,
    max_fibre_size: int = 5,
) -> BiFreeCorridorDetectorTarget:
    """Construct the fixed detector target for a local interval."""

    qmap = solution_from_local_interval(interval)
    summary = local_master_bottleneck_summary(
        interval,
        max_kernel_degree=max_kernel_degree,
        max_fibre_size=max_fibre_size,
    )
    groups = bifree_corridor_detector_groups(
        interval,
        max_kernel_degree=max_kernel_degree,
    )
    factor_orders = tuple(len(group.elements) for group in groups.values())
    return BiFreeCorridorDetectorTarget(
        summary=summary,
        applies=summary.verdict == TARGET_VERDICT,
        total_size=len(qmap.total.elements),
        quotient_size=len(qmap.quotient.elements),
        factor_orders=factor_orders,
        detector_order=prod(factor_orders, start=1),
    )


def bifree_corridor_word_certificate(
    interval: LocalInterval,
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
    max_kernel_degree: int | None = None,
    max_fibre_size: int = 5,
) -> BiFreeCorridorWordCertificate:
    """Profile one braid word against the fixed corridor detector factors.

    The certificate records whether the braid fixes the quotient action,
    whether it moves a residual tuple, and whether each finite factor has
    trivial recursive-longitude subgroup for the word.
    """

    key = tuple(braid_word)
    qmap = solution_from_local_interval(interval)
    target = bifree_corridor_detector_target(
        interval,
        max_kernel_degree=max_kernel_degree,
        max_fibre_size=max_fibre_size,
    )
    quotient_fixed = is_identity_action(qmap.quotient, n, key)
    moved = qmap.moved_residual_tuple(n, key) if quotient_fixed else None
    groups = bifree_corridor_detector_groups(
        interval,
        max_kernel_degree=max_kernel_degree,
    )
    profile = longitude_subgroup_profile(
        groups,
        n,
        key,
        max_assignments=max_assignments,
    )
    return BiFreeCorridorWordCertificate(
        target=target,
        n=n,
        braid_word=key,
        quotient_fixed=quotient_fixed,
        moved_residual_tuple=moved,
        subgroup_profile=profile,
    )


def bifree_corridor_exact_image_audit(
    interval: LocalInterval,
    n: int,
    *,
    state_limit: int = 10000,
    max_kernel_degree: int | None = None,
) -> ExactImageAudit:
    """Close the fixed-index image for the corridor detector factors.

    This is the exact fixed-``n`` analogue of
    ``bifree_corridor_word_certificate``.  It uses the quotient colour
    solution as the base detector and the same two-sided Green factor list as
    ``bifree_corridor_detector_groups``.  A nontruncated audit with no
    failures proves the sharp detector implication only for this fixed braid
    index and this explicit interval; it is not the all-``n`` corridor
    theorem.
    """

    qmap = solution_from_local_interval(interval)
    groups = tuple(
        bifree_corridor_detector_groups(
            interval,
            max_kernel_degree=max_kernel_degree,
        ).values()
    )
    return exact_detector_image_audit(
        qmap,
        qmap.quotient,
        groups,
        n,
        state_limit=state_limit,
    )


def bifree_corridor_product_subgroup_audit(
    interval: LocalInterval,
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
    max_kernel_degree: int | None = None,
    max_fibre_size: int = 5,
    max_product_order: int = 100_000,
) -> BiFreeCorridorProductSubgroupAudit:
    """Audit the single product detector behind the corridor factor list.

    The factor list is the practical way to display the fixed detector data,
    but the sharp obstruction theorem uses one finite group.  When the product
    is small enough to enumerate, this helper checks the direct-product
    longitude-subgroup identity for the listed factors.  When it is too large,
    the returned audit is marked truncated; the symbolic product theorem still
    applies, but this finite enumerator is skipped.
    """

    key = tuple(braid_word)
    target = bifree_corridor_detector_target(
        interval,
        max_kernel_degree=max_kernel_degree,
        max_fibre_size=max_fibre_size,
    )
    groups = bifree_corridor_detector_groups(
        interval,
        max_kernel_degree=max_kernel_degree,
    )
    factor_names = tuple(groups.keys())
    factors = tuple(groups.values())
    factor_orders = tuple(len(group.elements) for group in factors)
    product_order = prod(factor_orders, start=1)
    profile = longitude_subgroup_profile(
        groups,
        n,
        key,
        max_assignments=max_assignments,
    )
    factor_identity_signatures = tuple(
        row.identity_longitude_signature for row in profile
    )
    all_factor_identity = all(factor_identity_signatures)
    if product_order > max_product_order:
        return BiFreeCorridorProductSubgroupAudit(
            target=target,
            n=n,
            braid_word=key,
            factor_names=factor_names,
            factor_orders=factor_orders,
            factor_identity_signatures=factor_identity_signatures,
            all_factor_identity_signatures=all_factor_identity,
            product_group_order=product_order,
            truncated=True,
            product_subgroup_size=None,
            expected_product_subgroup_size=None,
            product_subgroup_equals_factor_product=None,
            product_identity_signature=None,
            product_identity_signature_equivalent=None,
        )

    product_audit: DirectProductLongitudeSubgroupAudit = (
        direct_product_longitude_subgroup_audit(
            factors,
            n,
            key,
            max_assignments=max_assignments,
        )
    )
    permutation = (
        profile[0].permutation if profile else artin_longitudes(n, key).permutation
    )
    product_identity = (
        permutation == tuple(range(n))
        and product_audit.product_subgroup_size == 1
    )
    return BiFreeCorridorProductSubgroupAudit(
        target=target,
        n=n,
        braid_word=key,
        factor_names=factor_names,
        factor_orders=factor_orders,
        factor_identity_signatures=factor_identity_signatures,
        all_factor_identity_signatures=all_factor_identity,
        product_group_order=product_order,
        truncated=False,
        product_subgroup_size=product_audit.product_subgroup_size,
        expected_product_subgroup_size=(
            product_audit.expected_product_subgroup_size
        ),
        product_subgroup_equals_factor_product=(
            product_audit.product_subgroup_equals_factor_product
        ),
        product_identity_signature=product_identity,
        product_identity_signature_equivalent=(
            product_identity == all_factor_identity
            and product_audit.product_subgroup_equals_factor_product
        ),
    )


def bifree_corridor_bounded_failures(
    interval: LocalInterval,
    n: int,
    max_word_length: int,
    *,
    max_assignments: int | None = None,
    max_kernel_degree: int | None = None,
    max_fibre_size: int = 5,
    max_failures: int = 5,
) -> Tuple[BiFreeCorridorWordCertificate, ...]:
    """Return bounded listed-factor failures for the corridor target.

    This is a finite search diagnostic.  Each returned word fixes the
    quotient, moves a residual tuple, and has identity longitude-value
    subgroup profile for every listed detector factor.
    """

    qmap = solution_from_local_interval(interval)
    target = bifree_corridor_detector_target(
        interval,
        max_kernel_degree=max_kernel_degree,
        max_fibre_size=max_fibre_size,
    )
    groups = bifree_corridor_detector_groups(
        interval,
        max_kernel_degree=max_kernel_degree,
    )
    failures = []
    for word in bounded_words(n, max_word_length):
        if not word:
            continue
        key = tuple(word)
        quotient_fixed = is_identity_action(qmap.quotient, n, key)
        moved = qmap.moved_residual_tuple(n, key) if quotient_fixed else None
        profile = longitude_subgroup_profile(
            groups,
            n,
            key,
            max_assignments=max_assignments,
        )
        certificate = BiFreeCorridorWordCertificate(
            target=target,
            n=n,
            braid_word=key,
            quotient_fixed=quotient_fixed,
            moved_residual_tuple=moved,
            subgroup_profile=profile,
        )
        if not certificate.is_b_failure_against_listed_factors:
            continue
        failures.append(certificate)
        if len(failures) >= max_failures:
            break
    return tuple(failures)
