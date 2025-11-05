def task_id_111(test):
    state_5765 = 0
    while state_5765 < 6:
        if state_5765 == 0:
            dict1 = {}
            state_5765 += 1
        if state_5765 == 1:
            list1 = test.split(' ')
            state_5765 += 1
        if state_5765 == 2:
            t = 0
            state_5765 += 1
        if state_5765 == 3:
            for i in list1:
                if list1.count(i) > t and i != '':
                    t = list1.count(i)
            state_5765 += 1
        if state_5765 == 4:
            if t > 0:
                for i in list1:
                    if list1.count(i) == t:
                        dict1[i] = t
            state_5765 += 1
        if state_5765 == 5:
            return dict1
            state_5765 += 1