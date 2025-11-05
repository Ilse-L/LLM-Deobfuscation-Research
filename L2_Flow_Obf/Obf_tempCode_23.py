def task_id_96(n):
    state_5713 = 0
    while state_5713 < 3:
        if state_5713 == 0:
            primes = []
            state_5713 += 1
        if state_5713 == 1:
            for i in range(2, n):
                is_prime = True
                for j in range(2, i):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(i)
            state_5713 += 1
        if state_5713 == 2:
            return primes
            state_5713 += 1