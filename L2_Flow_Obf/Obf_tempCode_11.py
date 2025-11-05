def task_id_63(n: int):
    state_2294 = 0
    while state_2294 < 4:
        if state_2294 == 0:
            if n == 0:
                return 0
            state_2294 += 1
        if state_2294 == 1:
            if n == 1:
                return 0
            state_2294 += 1
        if state_2294 == 2:
            if n == 2:
                return 1
            state_2294 += 1
        if state_2294 == 3:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
            state_2294 += 1