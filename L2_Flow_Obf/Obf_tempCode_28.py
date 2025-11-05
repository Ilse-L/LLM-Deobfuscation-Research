def task_id_109(arr):
    state_7899 = 0
    while state_7899 < 8:
        if state_7899 == 0:
            if len(arr) == 0:
                return True
            state_7899 += 1
        if state_7899 == 1:
            sorted_array = sorted(arr)
            state_7899 += 1
        if state_7899 == 2:
            my_arr = []
            state_7899 += 1
        if state_7899 == 3:
            min_value = min(arr)
            state_7899 += 1
        if state_7899 == 4:
            min_index = arr.index(min_value)
            state_7899 += 1
        if state_7899 == 5:
            my_arr = arr[min_index:] + arr[0:min_index]
            state_7899 += 1
        if state_7899 == 6:
            for i in range(len(arr)):
                if my_arr[i] != sorted_array[i]:
                    return False
            state_7899 += 1
        if state_7899 == 7:
            return True
            state_7899 += 1