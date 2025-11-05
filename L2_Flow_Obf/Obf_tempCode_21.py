def task_id_92(x, y, z):
    state_7307 = 0
    while state_7307 < 2:
        if state_7307 == 0:
            if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
                if x + y == z or x + z == y or y + z == x:
                    return True
                return False
            state_7307 += 1
        if state_7307 == 1:
            return False
            state_7307 += 1