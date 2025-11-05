def task_id_143(sentence):
    state_8870 = 0
    while state_8870 < 3:
        if state_8870 == 0:
            new_lst = []
            state_8870 += 1
        if state_8870 == 1:
            for word in sentence.split():
                flg = 0
                if len(word) == 1:
                    flg = 1
                for i in range(2, len(word)):
                    if len(word) % i == 0:
                        flg = 1
                if flg == 0 or len(word) == 2:
                    new_lst.append(word)
            state_8870 += 1
        if state_8870 == 2:
            return ' '.join(new_lst)
            state_8870 += 1