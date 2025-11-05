def task_id_147(n):
    state_9993 = 0
    while state_9993 < 4:
        if state_9993 == 0:
            A = [i * i - i + 1 for i in range(1, n + 1)]
            state_9993 += 1
        if state_9993 == 1:
            ans = []
            state_9993 += 1
        if state_9993 == 2:
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if (A[i] + A[j] + A[k]) % 3 == 0:
                            ans += [(A[i], A[j], A[k])]
            state_9993 += 1
        if state_9993 == 3:
            return len(ans)
            state_9993 += 1