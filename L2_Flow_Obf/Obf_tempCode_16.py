def task_id_72(q, w):
    state_6947 = 0
    while state_6947 < 4:
        if state_6947 == 0:
            if sum(q) > w:
                return False
            state_6947 += 1
        if state_6947 == 1:
            i, j = (0, len(q) - 1)
            state_6947 += 1
        if state_6947 == 2:
            while i < j:
                if q[i] != q[j]:
                    return False
                i += 1
                j -= 1
            state_6947 += 1
        if state_6947 == 3:
            return True
            state_6947 += 1