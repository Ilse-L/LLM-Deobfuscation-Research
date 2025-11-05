def task_id_106(n):
    state_4756 = 0
    while state_4756 < 3:
        if state_4756 == 0:
            ret = []
            state_4756 += 1
        if state_4756 == 1:
            for i in range(1, n + 1):
                if i % 2 == 0:
                    x = 1
                    for j in range(1, i + 1):
                        x *= j
                    ret += [x]
                else:
                    x = 0
                    for j in range(1, i + 1):
                        x += j
                    ret += [x]
            state_4756 += 1
        if state_4756 == 2:
            return ret
            state_4756 += 1