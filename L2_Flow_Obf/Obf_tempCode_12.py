FIX = '\nAdd more test cases.\n'

def task_id_64(s):
    state_7391 = 0
    while state_7391 < 4:
        if state_7391 == 0:
            vowels = 'aeiouAEIOU'
            state_7391 += 1
        if state_7391 == 1:
            n_vowels = sum((c in vowels for c in s))
            state_7391 += 1
        if state_7391 == 2:
            if s[-1] == 'y' or s[-1] == 'Y':
                n_vowels += 1
            state_7391 += 1
        if state_7391 == 3:
            return n_vowels
            state_7391 += 1