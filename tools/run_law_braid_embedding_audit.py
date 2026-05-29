import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    commutator,
    cyclic_group,
    exponent_law_word,
    free_word_power,
    law_word_on_last_strand,
    longitude_identity_profile_for_law_braid,
    symmetric_group,
)


OUT = ROOT / "proofs" / "law_braid_embedding_audit.json"


def main():
    groups = {
        "C2": cyclic_group(2),
        "C3": cyclic_group(3),
        "C5": cyclic_group(5),
        "S3": symmetric_group(3),
    }
    examples = {
        "x^6": (exponent_law_word(3), 1),
        "[x,y]": (commutator(free_word_power(0, 1), free_word_power(1, 1)), 2),
        "[x^2,y^3]": (commutator(free_word_power(0, 2), free_word_power(1, 3)), 2),
    }
    rows = {}
    for name, (word, arity) in examples.items():
        n, braid = law_word_on_last_strand(word, arity)
        invisible, visible = longitude_identity_profile_for_law_braid(groups, word, arity)
        rows[name] = {
            "arity": arity,
            "braid_index": n,
            "free_word": [list(letter) for letter in word],
            "braid_word": list(braid),
            "braid_word_length": len(braid),
            "longitude_invisible_groups": list(invisible),
            "longitude_visible_groups": list(visible),
        }
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
