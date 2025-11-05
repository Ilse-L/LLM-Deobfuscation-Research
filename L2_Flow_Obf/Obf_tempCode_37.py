def task_id_128(arr):
    state_6913 = 0
    while state_6913 < 3:
        if state_6913 == 0:
            if not arr:
                return None
            state_6913 += 1
        if state_6913 == 1:
            prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
            state_6913 += 1
        if state_6913 == 2:
            return prod * sum([abs(i) for i in arr])
            state_6913 += 1