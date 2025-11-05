def task_id_38(s: str):
    state_4432 = 0
    while state_4432 < 4:
        if state_4432 == 0:
            '\n    returns encoded string by cycling groups of three characters.\n    '
            state_4432 += 1
        if state_4432 == 1:
            groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
            state_4432 += 1
        if state_4432 == 2:
            groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
            state_4432 += 1
        if state_4432 == 3:
            return ''.join(groups)
            state_4432 += 1

def task_id_38(s: str):
    state_3591 = 0
    while state_3591 < 1:
        if state_3591 == 0:
            return encode_cyclic(encode_cyclic(s))
            state_3591 += 1