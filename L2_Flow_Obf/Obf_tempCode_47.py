def task_id_151(lst):
    state_5274 = 0
    while state_5274 < 1:
        if state_5274 == 0:
            return sum([i ** 2 for i in lst if i > 0 and i % 2 != 0 and ('.' not in str(i))])
            state_5274 += 1