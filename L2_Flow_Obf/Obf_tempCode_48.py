def task_id_154(a, b):
    state_4347 = 0
    while state_4347 < 4:
        if state_4347 == 0:
            l = len(b)
            state_4347 += 1
        if state_4347 == 1:
            pat = b + b
            state_4347 += 1
        if state_4347 == 2:
            for i in range(len(a) - l + 1):
                for j in range(l + 1):
                    if a[i:i + l] == pat[j:j + l]:
                        return True
            state_4347 += 1
        if state_4347 == 3:
            return False
            state_4347 += 1