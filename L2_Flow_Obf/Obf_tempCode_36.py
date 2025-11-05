def task_id_126(lst):
    state_4728 = 0
    while state_4728 < 4:
        if state_4728 == 0:
            count_digit = dict([(i, 0) for i in lst])
            state_4728 += 1
        if state_4728 == 1:
            for i in lst:
                count_digit[i] += 1
            state_4728 += 1
        if state_4728 == 2:
            if any((count_digit[i] > 2 for i in lst)):
                return False
            state_4728 += 1
        if state_4728 == 3:
            if all((lst[i - 1] <= lst[i] for i in range(1, len(lst)))):
                return True
            else:
                return False
            state_4728 += 1