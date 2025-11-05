def task_id_121(lst):
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])