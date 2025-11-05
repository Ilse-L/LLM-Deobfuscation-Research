def task_id_101(s):
    state_1578 = 0
    while state_1578 < 5:
        if state_1578 == 0:
            if not s:
                return []
            state_1578 += 1
        if state_1578 == 1:
            s_list = []
            state_1578 += 1
        if state_1578 == 2:
            for letter in s:
                if letter == ',':
                    s_list.append(' ')
                else:
                    s_list.append(letter)
            state_1578 += 1
        if state_1578 == 3:
            s_list = ''.join(s_list)
            state_1578 += 1
        if state_1578 == 4:
            return s_list.split()
            state_1578 += 1