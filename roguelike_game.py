import os
import interaction
import csv
import inventory
import introduction


def gamemap(room):
    
    for i in range(len(room)):
        print("".join(room[i]))


def player_pos(room, stuff, pos):

    for i in range(len(room)):
        if stuff['player'] in room[i]:
            x_axis = i
            y_axis = room[i].index(stuff['player'])

            del pos[:]
            pos.append(x_axis)
            pos.append(y_axis)


def main():
   
    introduction.menu_select()
    introduction.hero_creation()
    interaction.move()


if __name__ == '__main__':
    main()
