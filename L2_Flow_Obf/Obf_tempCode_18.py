def task_id_80(s):
    state_4913 = 0
    while state_4913 < 3:
        if state_4913 == 0:
            if len(s) < 3:
                return False
            state_4913 += 1
        if state_4913 == 1:
            for i in range(len(s) - 2):
                if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
                    return False
            state_4913 += 1
        if state_4913 == 2:
            return True
            state_4913 += 1