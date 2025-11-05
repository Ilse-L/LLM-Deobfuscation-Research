def task_id_146(nums):
    state_6111 = 0
    while state_6111 < 3:
        if state_6111 == 0:
            count = 0
            state_6111 += 1
        if state_6111 == 1:
            for num in nums:
                if num > 10:
                    odd_digits = (1, 3, 5, 7, 9)
                    number_as_string = str(num)
                    if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                        count += 1
            state_6111 += 1
        if state_6111 == 2:
            return count
            state_6111 += 1