def task_id_71(a, b, c):
    state_7854 = 0
    while state_7854 < 5:
        if state_7854 == 0:
            if a + b <= c or a + c <= b or b + c <= a:
                return -1
            state_7854 += 1
        if state_7854 == 1:
            s = (a + b + c) / 2
            state_7854 += 1
        if state_7854 == 2:
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            state_7854 += 1
        if state_7854 == 3:
            area = round(area, 2)
            state_7854 += 1
        if state_7854 == 4:
            return area
            state_7854 += 1