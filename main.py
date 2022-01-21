from drunk import Drunk
import turtle
import random
import math
import time

start_time = time.time()

print("Hi this is the 'Homer is coming home' project")
sf_matrix = [[0,0,0,"X","X","X",0,0,0,0,0,0,0,"X",0,0,0,0,0,0],
            [0,0,0,"X","X","X",0,"X",0,0,0,0,0,"X",0,0,0,0,0,0],
            [0,0,0,"X","X","X",0,0,0,0,0,"X",0,"X",0,0,"X","X",0,0],
            [0,0,0,0,"X","X","X","X",0,0,"X","X","X","X",0,0,0,0,0,0],
            [0,0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ["X",0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,"X","X","X"],
            [0,0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,"X","X","X"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"X","X","X"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"X","X","X"],
            ["X",0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,"X","X","X"],
            [0,0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ["X",0,0,0,"X","X",0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ["X","X","X",0,"X","X",0,0,0,0,0,0,0,0,"X","X",0,0,0,0],
            ["X","X","X","X","X","X",0,"X",0,0,0,0,0,0,"X","X",0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


test_matrix = [[0,0,0,"X","X"],
                [0,0,0,"X","X"],
                [0,0,0,"X","X"],
                ["X","X","X","X","X"],
                ["X","X","X","X","X"]]
Marge = [11,11]
Moes = [6,9]


#From our postion in the matrix returns a list of possible positions to go#
def valid_position(matrix,y,x):
    valid_list = []
    if x+1 < len(matrix[0]) and matrix[y][x+1] != "X":
        valid_list.append([0,1])
    if y+1 < len(matrix) and matrix[y+1][x] != "X":
        valid_list.append([1,0])
    if x-1 >= 0 and matrix[y][x-1] != "X":
        valid_list.append([0,-1])
    if y-1 >= 0 and matrix[y-1][x] != "X":
        valid_list.append([-1,0])

    return valid_list

#Chooses from the positions wich one to go, if it gets to Marge the loop stops#
def random_walk(matrix,drunk):
    if drunk.el_time < 10000000:
        valid_moves = valid_position(matrix,drunk.posy,drunk.posx)
        move = random.choice(valid_moves)
        drunk.walk(move[0],move[1])
    else:
        drunk.posx = Marge[1]
        drunk.posy = Marge[0]


#Create Homer Simpson#
H = Drunk("Homer Simpson",Moes[0],Moes[1],0, "#")
drunk = H
matrix = sf_matrix
data = []

#Beginning Turtle#
starty = drunk.posy
startx = drunk.posx
time0 = drunk.el_time
f = open("data.txt", "w")


image = input("Do you want so see the path  (yes/no)?    ")
if image == "yes" or image == "y":
    velocity = int(input("How fast do you want it to go (1-10)?     "))
trys = int(input("How many trys do you want? "))

if image == "yes" or image == "y":
    s = turtle.getscreen()
    s.bgpic("media/teste_turtle.png")
    s.register_shape('media/homer_32.gif')
    t = turtle.Turtle('media/homer_32.gif')
    t.up()
    t.speed(velocity)


#main code#
total = 0
total_squared = 0
min = 10000
max = 0
values = []
values_median = 0
total_squared_v = 0
for i in range(trys):
    if image == "yes" or image == "y":
        t.goto(H.posx * 30 -300+15, H.posy *30 - 240+15)
        t.down()
    while (drunk.posx != Marge[1]) or (drunk.posy != Marge[0]):
        matrix[H.posy][H.posx] = 0
        random_walk(matrix,drunk)
        if image == "yes" or image == "y":
            t.goto(H.posx * 30 -300+15, H.posy *30 - 240+15)
        matrix[H.posy][H.posx] = "H"


    drunk.posy = starty
    drunk.posx = startx
    data.append(drunk.el_time)
    f.write(str(drunk.el_time)+"\n")
    total += drunk.el_time
    total_squared += drunk.el_time ** 2
    if drunk.el_time > max:
        max = drunk.el_time
    if drunk.el_time < min:
        min = drunk.el_time
    if drunk.el_time > 2880:
        values.append(drunk.el_time)
        values_median += drunk.el_time
        total_squared_v += drunk.el_time ** 2
    drunk.el_time = time0



elapsed_time = time.time() - start_time
f.write("The average time it took for Homer to get Home was:  " + str(total/trys) + " minutes. With a standard deviation of " + str(math.sqrt(total_squared/trys - (total/trys)**2 )))
print("The average time it took for Homer to get Home was:  " + str(total/trys) + " minutes. With a standard deviation of " + str(math.sqrt(total_squared/trys - (total/trys)**2 )))
