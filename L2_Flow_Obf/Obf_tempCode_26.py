def task_id_104(x):
    state_9919 = 0
    while state_9919 < 3:
        if state_9919 == 0:
            odd_digit_elements = []
            state_9919 += 1
        if state_9919 == 1:
            for i in x:
                if all((int(c) % 2 == 1 for c in str(i))):
                    odd_digit_elements.append(i)
            state_9919 += 1
        if state_9919 == 2:
            return sorted(odd_digit_elements)
            state_9919 += 1