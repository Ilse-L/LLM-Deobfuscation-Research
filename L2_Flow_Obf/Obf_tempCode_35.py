def task_id_125(txt):
    state_2054 = 0
    while state_2054 < 1:
        if state_2054 == 0:
            if ' ' in txt:
                return txt.split()
            elif ',' in txt:
                return txt.replace(',', ' ').split()
            else:
                return len([i for i in txt if i.islower() and ord(i) % 2 == 0])
            state_2054 += 1