def task_id_93(message):
    state_3835 = 0
    while state_3835 < 4:
        if state_3835 == 0:
            vowels = 'aeiouAEIOU'
            state_3835 += 1
        if state_3835 == 1:
            vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
            state_3835 += 1
        if state_3835 == 2:
            message = message.swapcase()
            state_3835 += 1
        if state_3835 == 3:
            return ''.join([vowels_replace[i] if i in vowels else i for i in message])
            state_3835 += 1