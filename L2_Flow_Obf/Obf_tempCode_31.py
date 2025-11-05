def task_id_114(nums):
    state_7461 = 0
    while state_7461 < 6:
        if state_7461 == 0:
            max_sum = 0
            state_7461 += 1
        if state_7461 == 1:
            s = 0
            state_7461 += 1
        if state_7461 == 2:
            for num in nums:
                s += -num
                if s < 0:
                    s = 0
                max_sum = max(s, max_sum)
            state_7461 += 1
        if state_7461 == 3:
            if max_sum == 0:
                max_sum = max((-i for i in nums))
            state_7461 += 1
        if state_7461 == 4:
            min_sum = -max_sum
            state_7461 += 1
        if state_7461 == 5:
            return min_sum
            state_7461 += 1