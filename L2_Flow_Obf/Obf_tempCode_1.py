from typing import List, Optional

def task_id_12(strings: List[str]) -> Optional[str]:
    state_1645 = 0
    while state_1645 < 3:
        if state_1645 == 0:
            if not strings:
                return None
            state_1645 += 1
        if state_1645 == 1:
            maxlen = max((len(x) for x in strings))
            state_1645 += 1
        if state_1645 == 2:
            for s in strings:
                if len(s) == maxlen:
                    return s
            state_1645 += 1