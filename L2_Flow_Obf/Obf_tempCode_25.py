def task_id_102(x, y):
    state_9902 = 0
    while state_9902 < 4:
        if state_9902 == 0:
            if x > y:
                return -1
            state_9902 += 1
        if state_9902 == 1:
            if y % 2 == 0:
                return y
            state_9902 += 1
        if state_9902 == 2:
            if x == y:
                return -1
            state_9902 += 1
        if state_9902 == 3:
            return y - 1
            state_9902 += 1