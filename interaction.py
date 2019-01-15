from roguelike_game import *


def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def up(mydict, inst_replace, inst_player, pos):
    (mydict[pos[0]]).pop(pos[1])
    (mydict[pos[0]]).insert(pos[1], inst_replace)
    (mydict[pos[0] - 1]).pop(pos[1])
    (mydict[pos[0] - 1]).insert(pos[1], inst_player)


def down(mydict, inst_replace, inst_player, pos):
    (mydict[pos[0]]).pop(pos[1])
    (mydict[pos[0]]).insert(pos[1], inst_replace)
    (mydict[pos[0] + 1]).pop(pos[1])
    (mydict[pos[0] + 1]).insert(pos[1], inst_player)


def left(mydict, inst_replace, inst_player, pos):
    (mydict[pos[0]]).pop(pos[1])
    (mydict[pos[0]]).insert(pos[1], inst_replace)
    (mydict[pos[0]]).pop(pos[1] - 1)
    (mydict[pos[0]]).insert(pos[1] - 1, inst_player)


def right(mydict, inst_replace, inst_player, pos):
    (mydict[pos[0]]).pop(pos[1])
    (mydict[pos[0]]).insert(pos[1], inst_replace)
    (mydict[pos[0]]).pop(pos[1] + 1)
    (mydict[pos[0]]).insert(pos[1] + 1, inst_player)


def updater(room, stuff, pos):
    os.system('clear')
    gamemap(room)
    player_pos(room, stuff, pos)


def pressedkey():
    return getch()


def read_map_from_txt(filename):

    map = []
    dicted_map = {}

    with open(filename, 'r') as f:
        line = f.readlines()

    for data in line:
        map.append(list(data.strip()))

    for line in range(len(map)):
        dicted_map[line] = map[line]

    return dicted_map


def choose_map(map_number):

    room_dict = {}
    rooms = ('room1.txt', 'room2.txt', 'room3.txt')

    for number in range(len(rooms)):
        room_dict[number] = rooms[number]

    for room_index in room_dict.keys():
        if room_index == map_number:
            return room_dict[room_index]


def pickup_to_inventory(item, backpack, item_counter):
    start_values = [40, 50, 500]
    diamond_values = [40, 50, 500]

    if item is 'Y':

        if item_counter == 0:
            backpack['diamond'] = diamond_values

        if item_counter > 0:

            update_value = backpack.get('diamond')

            for value in range(len(update_value)):

                update_value[value] += start_values[value]

    return backpack


def show_invetory(myDict):
    print(myDict)


def move():

    stuff = {
        'wall': "#",
        'player': "@",
        'empty': ".",
        'teleport': 'T',
        'small_teleport': 't'}

    items = {'diamond': '*',
             'dagger': ']',
             'super_mace': ')',
             'wand': 'Y',
             'arrow': '/'}

    inventory = []
    backpack = {}
    map_counter = 0
    room = read_map_from_txt(choose_map(map_counter))
    pos = []
    item_counter = 0
    updater(room, stuff, pos)

    while True:

        pressedkey = getch()
        if pressedkey == 'i':
            show_invetory(backpack)

        if pressedkey == 'x':
            break

        if pressedkey is ('w' or 'W'):

            expected_north_movement = room[pos[0] - 1][pos[1]]

            if expected_north_movement is not stuff['wall']:

                if expected_north_movement is stuff['teleport']:
                    map_counter += 1
                    room = read_map_from_txt(choose_map(map_counter))

                for item in items.values():
                    if expected_north_movement is item:
                        pickup_to_inventory(item, backpack, item_counter)
                        item_counter += 1
                        up(room, stuff['empty'], stuff['player'], pos)

                up(room, stuff['empty'], stuff['player'], pos)
                updater(room, stuff, pos)

        if pressedkey is ('s' or 'S'):
            expected_south_movement = room[pos[0] + 1][pos[1]]

            if expected_south_movement is not stuff['wall']:

                if expected_south_movement is stuff['teleport']:
                    map_counter += 1
                    room = read_map_from_txt(choose_map(map_counter))

                for item in (items.values()):
                    if expected_south_movement is item:
                        pickup_to_inventory(item, inventory, backpack)
                        down(room, stuff['empty'], stuff['player'], pos)
                else:
                    down(room, stuff['empty'], stuff['player'], pos)
                    updater(room, stuff, pos)

        if pressedkey is ('a' or 'A'):
            expected_west_movement = room[pos[0]][pos[1] - 1]

            if expected_west_movement is not stuff['wall']:

                if expected_west_movement is stuff['teleport']:
                    map_counter += 1
                    room = read_map_from_txt(choose_map(map_counter))

                for item in items.values():
                    if expected_west_movement is item:
                        pickup_to_inventory(item, inventory, backpack)
                        left(room, stuff['empty'], stuff['player'], pos)

                left(room, stuff['empty'], stuff['player'], pos)
                updater(room, stuff, pos)

        if pressedkey is ('d' or 'D'):
            expected_east_movement = room[pos[0]][pos[1] + 1]

            if expected_east_movement is not stuff['wall']:

                if expected_east_movement is stuff['teleport']:
                    map_counter += 1
                    room = read_map_from_txt(choose_map(map_counter))

                for item in items.values():
                    if expected_east_movement is item:
                        pickup_to_inventory(item, inventory, backpack)
                        right(room, stuff['empty'], stuff['player'], pos)
                else:
                    right(room, stuff['empty'], stuff['player'], pos)
                    updater(room, stuff, pos)
