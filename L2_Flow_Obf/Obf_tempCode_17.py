def task_id_74(lst1, lst2):
    state_6306 = 0
    while state_6306 < 5:
        if state_6306 == 0:
            l1 = 0
            state_6306 += 1
        if state_6306 == 1:
            for st in lst1:
                l1 += len(st)
            state_6306 += 1
        if state_6306 == 2:
            l2 = 0
            state_6306 += 1
        if state_6306 == 3:
            for st in lst2:
                l2 += len(st)
            state_6306 += 1
        if state_6306 == 4:
            if l1 <= l2:
                return lst1
            else:
                return lst2
            state_6306 += 1