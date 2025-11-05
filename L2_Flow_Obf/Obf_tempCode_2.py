def task_id_31(n):
    state_1395 = 0
    while state_1395 < 3:
        if state_1395 == 0:
            if n < 2:
                return False
            state_1395 += 1
        if state_1395 == 1:
            for k in range(2, n - 1):
                if n % k == 0:
                    return False
            state_1395 += 1
        if state_1395 == 2:
            return True
            state_1395 += 1