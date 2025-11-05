def task_id_150(n, x, y):
    state_9709 = 0
    while state_9709 < 2:
        if state_9709 == 0:
            if n == 1:
                return y
            state_9709 += 1
        if state_9709 == 1:
            for i in range(2, n):
                if n % i == 0:
                    return y
                    break
            else:
                return x
            state_9709 += 1