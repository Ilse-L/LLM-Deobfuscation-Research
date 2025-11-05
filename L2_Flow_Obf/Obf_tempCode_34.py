def task_id_121(lst):
    state_8686 = 0
    while state_8686 < 1:
        if state_8686 == 0:
            return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])
            state_8686 += 1