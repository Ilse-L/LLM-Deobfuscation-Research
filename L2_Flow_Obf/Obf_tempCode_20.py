def task_id_87(lst, x):
    state_6278 = 0
    while state_6278 < 2:
        if state_6278 == 0:
            coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
            state_6278 += 1
        if state_6278 == 1:
            return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
            state_6278 += 1