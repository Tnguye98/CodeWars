def tower_builder(n_floors):
    spaceFloor = n_floors - 1
    starFloor = ''
    building = []
    for floor in range(n_floors):
        for leftSpace in range(spaceFloor):
            starFloor += ' '
        starFloor += '*'
        for stars in range(floor*2):
            starFloor += '*'
        for rightSpace in range(spaceFloor):
            starFloor += ' '
        building.append(starFloor)
        starFloor= ''
        spaceFloor -= 1
    return building


print(tower_builder(3))