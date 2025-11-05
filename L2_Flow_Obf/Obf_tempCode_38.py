def task_id_130(n):
    state_8659 = 0
    while state_8659 < 4:
        if state_8659 == 0:
            if n == 0:
                return [1]
            state_8659 += 1
        if state_8659 == 1:
            my_tri = [1, 3]
            state_8659 += 1
        if state_8659 == 2:
            for i in range(2, n + 1):
                if i % 2 == 0:
                    my_tri.append(i / 2 + 1)
                else:
                    my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
            state_8659 += 1
        if state_8659 == 3:
            return my_tri
            state_8659 += 1