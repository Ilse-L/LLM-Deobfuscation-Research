FIX = '\nAdd more test cases.\n'

def task_id_64(s):
    vowels = 'aeiouAEIOU'
    n_vowels = sum((c in vowels for c in s))
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels