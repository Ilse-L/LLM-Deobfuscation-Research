def task_id_148(planet1, planet2):
    state_4566 = 0
    while state_4566 < 5:
        if state_4566 == 0:
            planet_names = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
            state_4566 += 1
        if state_4566 == 1:
            if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
                return ()
            state_4566 += 1
        if state_4566 == 2:
            planet1_index = planet_names.index(planet1)
            state_4566 += 1
        if state_4566 == 3:
            planet2_index = planet_names.index(planet2)
            state_4566 += 1
        if state_4566 == 4:
            if planet1_index < planet2_index:
                return planet_names[planet1_index + 1:planet2_index]
            else:
                return planet_names[planet2_index + 1:planet1_index]
            state_4566 += 1