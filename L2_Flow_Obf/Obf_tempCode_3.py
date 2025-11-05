def task_id_36(n: int):
    state_2848 = 0
    while state_2848 < 6:
        if state_2848 == 0:
            ns = []
            state_2848 += 1
        if state_2848 == 1:
            for i in range(n):
                if i % 11 == 0 or i % 13 == 0:
                    ns.append(i)
            state_2848 += 1
        if state_2848 == 2:
            s = ''.join(list(map(str, ns)))
            state_2848 += 1
        if state_2848 == 3:
            ans = 0
            state_2848 += 1
        if state_2848 == 4:
            for c in s:
                ans += c == '7'
            state_2848 += 1
        if state_2848 == 5:
            return ans
            state_2848 += 1