def task_id_118(word):
    state_3252 = 0
    while state_3252 < 4:
        if state_3252 == 0:
            if len(word) < 3:
                return ''
            state_3252 += 1
        if state_3252 == 1:
            vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U', 'I'}
            state_3252 += 1
        if state_3252 == 2:
            for i in range(len(word) - 2, 0, -1):
                if word[i] in vowels:
                    if word[i + 1] not in vowels and word[i - 1] not in vowels:
                        return word[i]
            state_3252 += 1
        if state_3252 == 3:
            return ''
            state_3252 += 1