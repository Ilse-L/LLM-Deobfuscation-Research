def task_id_137(a, b):
    state_5280 = 0
    while state_5280 < 5:
        if state_5280 == 0:
            temp_a, temp_b = (a, b)
            state_5280 += 1
        if state_5280 == 1:
            if isinstance(temp_a, str):
                temp_a = temp_a.replace(',', '.')
            state_5280 += 1
        if state_5280 == 2:
            if isinstance(temp_b, str):
                temp_b = temp_b.replace(',', '.')
            state_5280 += 1
        if state_5280 == 3:
            if float(temp_a) == float(temp_b):
                return None
            state_5280 += 1
        if state_5280 == 4:
            return a if float(temp_a) > float(temp_b) else b
            state_5280 += 1