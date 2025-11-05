def task_id_66(s):
    state_9319 = 0
    while state_9319 < 2:
        if state_9319 == 0:
            if s == '':
                return 0
            state_9319 += 1
        if state_9319 == 1:
            return sum((ord(char) if char.isupper() else 0 for char in s))
            state_9319 += 1