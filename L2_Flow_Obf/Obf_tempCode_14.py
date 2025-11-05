def task_id_69(lst):
    state_4688 = 0
    while state_4688 < 5:
        if state_4688 == 0:
            frq = [0] * (max(lst) + 1)
            state_4688 += 1
        if state_4688 == 1:
            for i in lst:
                frq[i] += 1
            state_4688 += 1
        if state_4688 == 2:
            ans = -1
            state_4688 += 1
        if state_4688 == 3:
            for i in range(1, len(frq)):
                if frq[i] >= i:
                    ans = i
            state_4688 += 1
        if state_4688 == 4:
            return ans
            state_4688 += 1