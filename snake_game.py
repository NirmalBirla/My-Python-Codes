def finalPositionOfSnake(n, commands):
    i = 0
    j = 0
    for command in commands:
        if command == "UP":
            i -= 1
        if command == "DOWN":
            i += 1
        if command == "LEFT":
            j -= 1
        if command == "RIGHT":
            j += 1
    else:
        return (i*n)+j

n = 2
commands = ["RIGHT", "DOWN"]
print(finalPositionOfSnake(n,commands))