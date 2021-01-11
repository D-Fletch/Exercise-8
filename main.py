import random
#note book problem 1

#change to True to test
Run = False
#sets notes to empty
notes = ['', '', '', '', '', '', '', '', '', '']

while Run == True:

    action = input("read or write? ")

    if action == "read":
        i = 0
        for i in range(0, 10):
            #prints array item by item
            print(i, ": ", notes[i])

    elif action == "write":

        number = int(input("What section do you want to write in? "))

        new_note = input("what do you want to write? ")
        #deletes note in spot that is going to be written to
        notes.pop(number)
        notes.insert(number, new_note)

# proc gen problem 2


def generator(planet_num):

    creatures = [
        'monkeys', 'lizards', 'bugs', 'birds', 'owls', 'cats', 'cows', 'sheep'
    ]

    colours = ['bald', 'red', 'black', 'invisible', 'glittering']

    characteristics = [
        'cunning', 'mad', 'evil', 'helpful', 'happy', 'confused', 'tiny',
        'strange'
    ]

    random.seed(planet_num)

    first = random.choice(characteristics)
    second = random.choice(colours)
    third = random.choice(creatures)
    #combines random choices
    result = first + " " + second + " " + third
    print(result)


'''
generator(3452)
generator(1111)
generator(32893)
generator(238576)
#returns to first seed to show they dont change
generator(3452)
'''

#days of christmas problem 2


def christmas_song(number_of_days):
    #lists song
    christmas = [
        "a partridge in a pear tree", 'two turtle doves', 'three french hens',
        'four calling birds', 'five gold rings', 'six geese a laying',
        'seven swans a swimming', 'eight maids a milking',
        'nine laides dancing', 'ten lords a leaping', 'eleven pipers piping',
        'twelve drummers drumming'
    ]

    days = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelth'
    ]

    #arrays start at 0
    x = number_of_days - 1

    #counts down from x
    for x in range(number_of_days - 1, -1, -1):
        print("on the", days[x], "day of christmas")
        print("my true love gave to me")
        i = x
        for i in range(x, -1, -1):
            #nested loop adds lyrics
            #if its the first day, there is no 'and'
            #in front of a partridge
            if i == 0 and x != 0:
                print("And ", end="")
            print(christmas[i])


#christmas_song(3)

#tank problem 3

#use two dimensional array
#one player
#need random to place tanks
#8x8
#have 50 turns


def play(grid, placed, grid_length):

    turns = 20
    tank_total = 9

    while tank_total != 0 or turns != 0:

        for row in grid:
            print(' '.join([str(elem) for elem in row]))

        print("enter x cordinate")
        x_shot = int(input(">"))
        print("enter y cordinate")
        y_shot = int(input(">"))

        #because of outline grid cordinates will be wrong
        x_shot = x_shot + 1
        y_shot = y_shot + 1
        #this corrects int

        if placed[y_shot][x_shot] == "x":
            print("hit!")
            grid[y_shot][x_shot] = "/"
            tank_total -= 1
        else:
            print("miss")
            grid[y_shot][x_shot] = 'N'
        
        turns -= 1
        print("you have", turns, "turns left")
        print("there are", tank_total, "tanks left")


def start_tank_game():

    length = 9

    battlefield = [[0] * length for i in range(length)]
    #creates grid for game

    t_places = [[0] * length for i in range(length)]
    #creates answer grid for algorithm

    for j in range(1, length):
        battlefield[j][0] = j - 1
        t_places[j][0] = j - 1

    for j in range(1, length):
        battlefield[0][j] = j - 1
        t_places[0][j] = j -1

    #places random tanks
    Tanks_Placed = 0
    used_cordinates = []

    while Tanks_Placed < 10:

        x_coord = random.randint(1, 7)
        y_coord = random.randint(1, 7)

        result = str(x_coord) + "," + str(y_coord)

        for i in range(0, len(used_cordinates)):
            if result == used_cordinates[i]:
                copy = True
                continue
            else:
                copy = False

        if len(used_cordinates) == 0:
            copy = False

        if copy == False:
            used_cordinates.append(str(x_coord) + "," + str(y_coord))

            t_places[x_coord][y_coord] = "x"
            Tanks_Placed += 1

    play(battlefield, t_places, length)

#uncomment to start
#start_tank_game()

#strong numbers problem 3

def strength_test(num):

  num = str(num)
  digits = []
  factorialed = []
  total = 0

  for i in num:
    digits.append(int(i))
  
  for j in range(0, len(digits)):
    to_factorial = digits[j]
    x = 0
    result = 1
    
    for x in range(0, to_factorial):
      result = (to_factorial - x) * result
    factorialed.append(result)
    
  
  for k in range(0, len(factorialed)):
    total = total + factorialed[k]

  if total == int(num):
    return("Strong")
  else:
    return("Weak")
    

print(strength_test(145))
print(strength_test(0))
print(strength_test(90))
