def task_id_82(string):
    state_5633 = 0
    while state_5633 < 4:
        if state_5633 == 0:
            l = len(string)
            state_5633 += 1
        if state_5633 == 1:
            if l == 0 or l == 1:
                return False
            state_5633 += 1
        if state_5633 == 2:
            for i in range(2, l):
                if l % i == 0:
                    return False
            state_5633 += 1
        if state_5633 == 3:
            return True
            state_5633 += 1