def task_id_117(s, n):
    state_3047 = 0
    while state_3047 < 3:
        if state_3047 == 0:
            result = []
            state_3047 += 1
        if state_3047 == 1:
            for word in s.split():
                n_consonants = 0
                for i in range(0, len(word)):
                    if word[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
                        n_consonants += 1
                if n_consonants == n:
                    result.append(word)
            state_3047 += 1
        if state_3047 == 2:
            return result
            state_3047 += 1