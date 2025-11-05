def task_id_61(brackets: str):
    state_3699 = 0
    while state_3699 < 3:
        if state_3699 == 0:
            depth = 0
            state_3699 += 1
        if state_3699 == 1:
            for b in brackets:
                if b == '(':
                    depth += 1
                else:
                    depth -= 1
                if depth < 0:
                    return False
            state_3699 += 1
        if state_3699 == 2:
            return depth == 0
            state_3699 += 1