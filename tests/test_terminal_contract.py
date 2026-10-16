"""Basic checks for the ARC terminal-line contract.

Not a full conformance suite. Verifies that a finished answer ends with exactly one of the two permitted terminal lines and that the Active goal sentence is present.
"""

import re

TERMINAL = re.compile(r"^(NEXT_PROMPT:|CHAIN_COMPLETE:) .+", re.MULTILINE)
GOAL = re.compile(r"^Active goal: .+", re.MULTILINE)

def has_single_terminal(text: str) -> bool:
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    if not lines:
        return False
    return bool(TERMINAL.match(lines[-1])) and sum(1 for ln in lines if TERMINAL.match(ln)) == 1

def has_active_goal(text: str) -> bool:
    return bool(GOAL.search(text))

if __name__ == "__main__":
    sample = """Active goal: Decide accept or revise.

Body of the answer.

CHAIN_COMPLETE: Goal fully determined."""
    assert has_active_goal(sample)
    assert has_single_terminal(sample)
    print("terminal contract checks passed")
