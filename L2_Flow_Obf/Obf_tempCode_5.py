def task_id_40(l: list):
    state_8138 = 0
    while state_8138 < 2:
        if state_8138 == 0:
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    for k in range(j + 1, len(l)):
                        if l[i] + l[j] + l[k] == 0:
                            return True
            state_8138 += 1
        if state_8138 == 1:
            return False
            state_8138 += 1