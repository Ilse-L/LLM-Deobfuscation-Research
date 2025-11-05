def task_id_131(n):
    state_2954 = 0
    while state_2954 < 4:
        if state_2954 == 0:
            product = 1
            state_2954 += 1
        if state_2954 == 1:
            odd_count = 0
            state_2954 += 1
        if state_2954 == 2:
            for digit in str(n):
                int_digit = int(digit)
                if int_digit % 2 == 1:
                    product = product * int_digit
                    odd_count += 1
            state_2954 += 1
        if state_2954 == 3:
            if odd_count == 0:
                return 0
            else:
                return product
            state_2954 += 1