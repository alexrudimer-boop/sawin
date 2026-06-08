# Linear F3 Collision Quotient-Invariant Audit

This generated audit checks the all-arity quotient-invariant
certificate for the formal monolith-collision rows in the
six-point linear skew-over-flip degenerate non-involutive family.

## Summary

- rows checked: `144`;
- subdirect rows: `64`;
- subdirect rows with nondegenerate four-point quotient: `32`;
- subdirect rows with degenerate quotient: `32`;
- formal monolith `J`-collision rows: `32`;
- quotient-invariant certificates succeeded: `16`;
- quotient-invariant certificates failed: `16`;
- passive transport failures: `16`;
- passive-certified rows: `[20, 22, 40, 42, 58, 59, 60, 61, 72, 73, 74, 75, 128, 130, 140, 142]`;
- passive-failure rows: `[21, 23, 41, 43, 86, 87, 88, 89, 100, 101, 102, 103, 129, 131, 141, 143]`;
- all claimed checks passed: `True`.

## Distribution

| cases | monolith blocks | quotient nondegenerate | formal collision |
|---:|---|---|---|
| 32 | [1, 1, 1, 3] | False | False |
| 32 | [1, 1, 1, 3] | True | True |

## Certificate

For each certified row, the monolith has one collapsed
three-point fibre and three singleton quotient colours.  The
collapsed fibre crosses itself trivially.  For every singleton
`z`, the mixed crossing `z,F_i -> F_{S_z(i)},z'` gives an affine
permutation `S_z(i)=alpha_z i+beta_z` of `F_3`.  The audit checks
the identities:

```text
S_z S_w = S_{z'} S_{w'}        when R(z,w)=(z',w'),
S_{z'} T_z = id               when R(F_i,z)=(z',F_{T_z(i)}),
S_{alpha z}=S_z, S_{beta z}=S_z for passive left-list moves,
R(F_i,F_j)=(F_i,F_j).
```

Thus a tracked collapsed-fibre strand has invariant

```text
H_s = S_{a_1} S_{a_2} ... S_{a_k}(i),
```

where `a_1,...,a_k` are the singleton quotient colours to its
left.  If a braid fixes the four-point quotient word, then the
left singleton list and `H_s` return unchanged, so the hidden
fibre coordinate returns unchanged.  Therefore
`ker rho^Z_n <= ker rho^X_n` for all arities for these rows.

Since each such quotient `Z` is nondegenerate, the known
derived-rack theorem dominates `Z`, and the certificate dominates
the six-point lift.  The remaining passive-failure rows are not
closed by this one-strand invariant; they require either a
stronger invariant or an actual quotient-kernel witness.

## Failures

```json
[
  {
    "row_index": 21,
    "matrix_indices": [
      5,
      28,
      11,
      12
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          3,
          4,
          5
        ]
      ],
      "collapsed_block": [
        3,
        4,
        5
      ],
      "singleton_colors": [
        0,
        1,
        2
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "0": [
          2,
          0
        ],
        "1": [
          2,
          1
        ],
        "2": [
          2,
          2
        ]
      },
      "singleton_after_left_crossing": {
        "0": 0,
        "1": 2,
        "2": 1
      },
      "right_actions": {
        "0": {
          "output_singleton": 0,
          "hidden_action": [
            2,
            0
          ]
        },
        "1": {
          "output_singleton": 2,
          "hidden_action": [
            2,
            2
          ]
        },
        "2": {
          "output_singleton": 1,
          "hidden_action": [
            2,
            1
          ]
        }
      },
      "reachable_state_count": 6,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ],
        [
          2,
          0
        ],
        [
          2,
          1
        ],
        [
          2,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            2,
            1
          ],
          "transported_action": [
            2,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            2,
            1
          ],
          "transported_action": [
            2,
            2
          ]
        },
        {
          "side": "left",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            2,
            2
          ],
          "transported_action": [
            2,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            2,
            2
          ],
          "transported_action": [
            2,
            1
          ]
        }
      ]
    }
  },
  {
    "row_index": 23,
    "matrix_indices": [
      5,
      46,
      10,
      12
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          3,
          4,
          5
        ]
      ],
      "collapsed_block": [
        3,
        4,
        5
      ],
      "singleton_colors": [
        0,
        1,
        2
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "0": [
          2,
          0
        ],
        "1": [
          2,
          2
        ],
        "2": [
          2,
          1
        ]
      },
      "singleton_after_left_crossing": {
        "0": 0,
        "1": 2,
        "2": 1
      },
      "right_actions": {
        "0": {
          "output_singleton": 0,
          "hidden_action": [
            2,
            0
          ]
        },
        "1": {
          "output_singleton": 2,
          "hidden_action": [
            2,
            1
          ]
        },
        "2": {
          "output_singleton": 1,
          "hidden_action": [
            2,
            2
          ]
        }
      },
      "reachable_state_count": 6,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ],
        [
          2,
          0
        ],
        [
          2,
          1
        ],
        [
          2,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            2,
            2
          ],
          "transported_action": [
            2,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            2,
            2
          ],
          "transported_action": [
            2,
            1
          ]
        },
        {
          "side": "left",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            2,
            1
          ],
          "transported_action": [
            2,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            2,
            1
          ],
          "transported_action": [
            2,
            2
          ]
        }
      ]
    }
  },
  {
    "row_index": 41,
    "matrix_indices": [
      8,
      22,
      7,
      12
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          3,
          4,
          5
        ]
      ],
      "collapsed_block": [
        3,
        4,
        5
      ],
      "singleton_colors": [
        0,
        1,
        2
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "0": [
          1,
          0
        ],
        "1": [
          1,
          1
        ],
        "2": [
          1,
          2
        ]
      },
      "singleton_after_left_crossing": {
        "0": 0,
        "1": 2,
        "2": 1
      },
      "right_actions": {
        "0": {
          "output_singleton": 0,
          "hidden_action": [
            1,
            0
          ]
        },
        "1": {
          "output_singleton": 2,
          "hidden_action": [
            1,
            1
          ]
        },
        "2": {
          "output_singleton": 1,
          "hidden_action": [
            1,
            2
          ]
        }
      },
      "reachable_state_count": 3,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "left",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        }
      ]
    }
  },
  {
    "row_index": 43,
    "matrix_indices": [
      8,
      40,
      8,
      12
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          3,
          4,
          5
        ]
      ],
      "collapsed_block": [
        3,
        4,
        5
      ],
      "singleton_colors": [
        0,
        1,
        2
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "0": [
          1,
          0
        ],
        "1": [
          1,
          2
        ],
        "2": [
          1,
          1
        ]
      },
      "singleton_after_left_crossing": {
        "0": 0,
        "1": 2,
        "2": 1
      },
      "right_actions": {
        "0": {
          "output_singleton": 0,
          "hidden_action": [
            1,
            0
          ]
        },
        "1": {
          "output_singleton": 2,
          "hidden_action": [
            1,
            2
          ]
        },
        "2": {
          "output_singleton": 1,
          "hidden_action": [
            1,
            1
          ]
        }
      },
      "reachable_state_count": 3,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 1,
          "transported_singleton": 2,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "left",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 2,
          "transported_singleton": 1,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        }
      ]
    }
  },
  {
    "row_index": 86,
    "matrix_indices": [
      12,
      7,
      22,
      8
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          3
        ],
        [
          4
        ],
        [
          5
        ],
        [
          0,
          1,
          2
        ]
      ],
      "collapsed_block": [
        0,
        1,
        2
      ],
      "singleton_colors": [
        3,
        4,
        5
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "3": [
          1,
          0
        ],
        "4": [
          1,
          1
        ],
        "5": [
          1,
          2
        ]
      },
      "singleton_after_left_crossing": {
        "3": 3,
        "4": 5,
        "5": 4
      },
      "right_actions": {
        "3": {
          "output_singleton": 3,
          "hidden_action": [
            1,
            0
          ]
        },
        "4": {
          "output_singleton": 5,
          "hidden_action": [
            1,
            1
          ]
        },
        "5": {
          "output_singleton": 4,
          "hidden_action": [
            1,
            2
          ]
        }
      },
      "reachable_state_count": 3,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "left",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        }
      ]
    }
  },
  {
    "row_index": 87,
    "matrix_indices": [
      12,
      7,
      22,
      40
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          3
        ],
        [
          4
        ],
        [
          5
        ],
        [
          0,
          1,
          2
        ]
      ],
      "collapsed_block": [
        0,
        1,
        2
      ],
      "singleton_colors": [
        3,
        4,
        5
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "3": [
          1,
          0
        ],
        "4": [
          1,
          1
        ],
        "5": [
          1,
          2
        ]
      },
      "singleton_after_left_crossing": {
        "3": 3,
        "4": 5,
        "5": 4
      },
      "right_actions": {
        "3": {
          "output_singleton": 3,
          "hidden_action": [
            1,
            0
          ]
        },
        "4": {
          "output_singleton": 5,
          "hidden_action": [
            1,
            1
          ]
        },
        "5": {
          "output_singleton": 4,
          "hidden_action": [
            1,
            2
          ]
        }
      },
      "reachable_state_count": 3,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "left",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        }
      ]
    }
  },
  {
    "row_index": 88,
    "matrix_indices": [
      12,
      8,
      40,
      8
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          3
        ],
        [
          4
        ],
        [
          5
        ],
        [
          0,
          1,
          2
        ]
      ],
      "collapsed_block": [
        0,
        1,
        2
      ],
      "singleton_colors": [
        3,
        4,
        5
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "3": [
          1,
          0
        ],
        "4": [
          1,
          2
        ],
        "5": [
          1,
          1
        ]
      },
      "singleton_after_left_crossing": {
        "3": 3,
        "4": 5,
        "5": 4
      },
      "right_actions": {
        "3": {
          "output_singleton": 3,
          "hidden_action": [
            1,
            0
          ]
        },
        "4": {
          "output_singleton": 5,
          "hidden_action": [
            1,
            2
          ]
        },
        "5": {
          "output_singleton": 4,
          "hidden_action": [
            1,
            1
          ]
        }
      },
      "reachable_state_count": 3,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "left",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        }
      ]
    }
  },
  {
    "row_index": 89,
    "matrix_indices": [
      12,
      8,
      40,
      40
    ],
    "reason": null,
    "certificate": {
      "certified": false,
      "monolith_blocks": [
        [
          3
        ],
        [
          4
        ],
        [
          5
        ],
        [
          0,
          1,
          2
        ]
      ],
      "collapsed_block": [
        0,
        1,
        2
      ],
      "singleton_colors": [
        3,
        4,
        5
      ],
      "quotient_size": 4,
      "quotient_left_nondegenerate": true,
      "quotient_right_nondegenerate": true,
      "collapsed_self_identity": true,
      "singleton_actions": {
        "3": [
          1,
          0
        ],
        "4": [
          1,
          2
        ],
        "5": [
          1,
          1
        ]
      },
      "singleton_after_left_crossing": {
        "3": 3,
        "4": 5,
        "5": 4
      },
      "right_actions": {
        "3": {
          "output_singleton": 3,
          "hidden_action": [
            1,
            0
          ]
        },
        "4": {
          "output_singleton": 5,
          "hidden_action": [
            1,
            2
          ]
        },
        "5": {
          "output_singleton": 4,
          "hidden_action": [
            1,
            1
          ]
        }
      },
      "reachable_state_count": 3,
      "reachable_states": [
        [
          1,
          0
        ],
        [
          1,
          1
        ],
        [
          1,
          2
        ]
      ],
      "state_separates_hidden_fibre": true,
      "transition_closed_in_affine_group": true,
      "left_action_failure_count": 0,
      "right_crossing_failure_count": 0,
      "singleton_crossing_failure_count": 0,
      "passive_transport_failure_count": 4,
      "left_action_failures": [],
      "right_crossing_failures": [],
      "singleton_crossing_failures": [],
      "passive_transport_failures": [
        {
          "side": "left",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "right",
          "singleton": 4,
          "transported_singleton": 5,
          "action": [
            1,
            2
          ],
          "transported_action": [
            1,
            1
          ]
        },
        {
          "side": "left",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        },
        {
          "side": "right",
          "singleton": 5,
          "transported_singleton": 4,
          "action": [
            1,
            1
          ],
          "transported_action": [
            1,
            2
          ]
        }
      ]
    }
  }
]
```
