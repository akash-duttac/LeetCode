# n = 2
# commands = ["RIGHT","DOWN"]

n = 3
commands = ["DOWN","RIGHT","UP"]

def finalPositionofSnake(n, commands):
    i, j = 0, 0
    for command in commands:
        if command == "UP":
            j-=1
        elif command == "DOWN":
            j+=1
        elif command == "LEFT":
            i-=1
        elif command == "RIGHT":
            i+=1
        
    return (i*n)+j

print(finalPositionofSnake(n, commands))