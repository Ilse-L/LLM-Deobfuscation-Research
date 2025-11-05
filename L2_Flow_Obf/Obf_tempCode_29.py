def task_id_110(lst1, lst2):
    state_6500 = 0
    while state_6500 < 6:
        if state_6500 == 0:
            odd = 0
            state_6500 += 1
        if state_6500 == 1:
            even = 0
            state_6500 += 1
        if state_6500 == 2:
            for i in lst1:
                if i % 2 == 1:
                    odd += 1
            state_6500 += 1
        if state_6500 == 3:
            for i in lst2:
                if i % 2 == 0:
                    even += 1
            state_6500 += 1
        if state_6500 == 4:
            if even >= odd:
                return 'YES'
            state_6500 += 1
        if state_6500 == 5:
            return 'NO'
            state_6500 += 1