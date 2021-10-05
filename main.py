import numpy
import random
import time
import msvcrt
import os
def genminolayer():
    global selectedmino, minocoord, minolayer
    if selectedmino.ndim == 1:
        minolayer = numpy.append(numpy.zeros(minocoord[1]), selectedmino)
        minolayer = numpy.append(minolayer, numpy.zeros(12 - minolayer.shape[0]))
    else:
        minolayer = numpy.hstack([numpy.zeros([selectedmino.shape[0], minocoord[1]]), selectedmino])
        minolayer = numpy.hstack([minolayer, numpy.zeros([selectedmino.shape[0], 12 - minolayer.shape[1]])])
    minolayer = numpy.vstack([numpy.zeros([minocoord[0], 12]), minolayer])
    minolayer = numpy.vstack([minolayer, numpy.zeros([22 - minolayer.shape[0], 12])])
field = numpy.zeros((20, 10))
field = numpy.vstack((numpy.full(10, 3), field))
field = numpy.vstack((field, numpy.ones(10)))
field = numpy.hstack([field, numpy.ones([22, 1])])
field = numpy.hstack([numpy.ones([22, 1]), field])
minos = [
    numpy.array([[1,1,1,1]]),
    numpy.array(([1,1],[1,1])),
    numpy.array(([0,1,1],[1,1,0])),
    numpy.array(([1,1,0],[0,1,1])),
    numpy.array(([1,0,0],[1,1,1])),
    numpy.array(([0,0,1],[1,1,1])),
    numpy.array(([0,1,0],[1,1,1]))
]
count = 0
while True:
    for row in range(2, 21):
        if numpy.sum(field[row]) == 12.0:
            field = numpy.delete(field, row, 0)
            field = numpy.insert(field, 2, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], axis=0)
    selectedmino = random.choice(minos)
    minocoord = numpy.array([1, 5])
    genminolayer()
    if 2 in field + minolayer:
        break
    while True:
        time.sleep(0.01)
        count += 1
        if count % 70 == 0:
            if count == 70 and 2 in field + minolayer:
                break
            minocoord += numpy.array([1, 0])
            genminolayer()
            if 2 in field + minolayer:
                field = fieldbuffer
                break
            else:
                fieldbuffer = field + minolayer
                os.system('cls')
                print(numpy.where(field + minolayer == 0, ' ', 'X'))
        elif msvcrt.kbhit():
            key = str(msvcrt.getch())
            if key == "b'd'":
                #print("you enter d")
                minocoord += numpy.array([0, 1])
                genminolayer()
                if 2 in field + minolayer:
                    minocoord -= numpy.array([0, 1])
                    genminolayer()
                else:
                    fieldbuffer = field + minolayer
                    os.system('cls')
                    print(numpy.where(field + minolayer == 0, ' ', 'X'))
            elif key == "b'a'":
                minocoord -= numpy.array([0, 1])
                genminolayer()
                if 2 in field + minolayer:
                    minocoord += numpy.array([0, 1])
                    genminolayer()
                else:
                    fieldbuffer = field + minolayer
                    os.system('cls')
                    print(numpy.where(field + minolayer == 0, ' ', 'X'))
            elif key == "b's'":
                minocoord += numpy.array([1, 0])
                genminolayer()
                if 2 in field + minolayer:
                    field = fieldbuffer
                    break
                else:
                    fieldbuffer = field + minolayer
                    os.system('cls')
                    print(numpy.where(field + minolayer == 0, ' ', 'X'))
            elif key == "b'w'":
                selectedmino = numpy.rot90(selectedmino, -1)
                genminolayer()
                if 2 in field + minolayer:
                    selectedmino = numpy.rot90(selectedmino)
                    genminolayer()
                else:
                    fieldbuffer = field + minolayer
                    os.system('cls')
                    print(numpy.where(field + minolayer == 0, ' ', 'X'))
os.system('cls')
print('Game Over!')