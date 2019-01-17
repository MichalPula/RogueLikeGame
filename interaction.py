import roguelike_game
import os
import time
from timeit import default_timer as timer



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


def updater(room, stuff, pos):
    os.system('clear')
    print_map(room)
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


def print_map(room):
    
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



def show_invetory (myDict):
    print(myDict)



def movement_(movement_var,pos,mydict,stuff_dict):
   
    (mydict[pos[0]]).pop(pos[1])
    (mydict[pos[0]]).insert(pos[1], stuff_dict['empty'])
    (mydict[pos[0] + movement_var[0]]).pop(pos[1] + movement_var[1])
    (mydict[pos[0] + movement_var[0]]).insert(pos[1] + movement_var[1], stuff_dict['player'])

    updater(mydict, stuff_dict, pos)


def set_movement_variable(key,room,pos):
    result = "initialize var which never returns this string but its mandatory"

    if key is( "w" or "W"):
        x_key = -1
        y_key = 0
        
    
    if key is( "s" or "S"):
        x_key = 1
        y_key = 0
    
    if key is ("d" or "D"):
        x_key = 0
        y_key = 1
    
    if key is ("a" or "A"):
        x_key = 0
        y_key = -1

    result_dict_position = room[pos[0] + x_key][pos[1]+y_key]  
    
    return (x_key, y_key,result_dict_position)


def movement_buttons():
    mov_buttons = ['A','a','S','s','w','W','D','d']
    return mov_buttons
  

def add_to_inventory(item, backpack, item_counter, item_string, item_values):
    new_item_values = []
    values_to_update = []
   

    print(item_counter, "kaunter")
    if item_counter == 0:
        backpack.update({item_string: item_values})
        item_counter += 1

    if item_counter > 0:
        
        for item, value in backpack.items():  # długa pełna nazwa itemka
            if item == item_string:
                values_to_update = backpack.get(item_string)
        for value in range(len(values_to_update)):
            values_to_update[value] += item_values[value]
        backpack.update({item_string: values_to_update})

    return backpack


def pickup_to_inventory(item, backpack, item_counter):
    if item is '*':
        item_string = "Diamond"
        item_values = [40, 50, 500]
        add_to_inventory(item, backpack, item_counter, item_string, item_values)

    if item is 'Y':
        item_string = "Wand"
        item_values = [35, 10, 600]
        add_to_inventory(item, backpack, item_counter, item_string, item_values)

    if item is ']':
        item_string = "Dagger"
        item_values = [15, 35, 200]
        add_to_inventory(item, backpack, item_counter, item_string, item_values)

    if item is ')':
        item_string = "Super Mace"
        item_values = [80, 50, 1000]
        add_to_inventory(item, backpack, item_counter, item_string, item_values)

    if item is '/':
        item_string = "Arrow"
        item_values = [5, 10, 50]
        add_to_inventory(item, backpack, item_counter, item_string, item_values)
            
def enviroment(expected_movement,stuff_dict,items_dict,inventory,item_counter,backpack,map_counter,room):

    for item in items_dict.values():
        if expected_movement is item:
            print(item,expected_movement)
            pickup_to_inventory(item, backpack,item_counter)
    
    if expected_movement is stuff_dict['teleport']:
            map_counter += 1
            room = read_map_from_txt(choose_map(map_counter))


def move():

    stuff = {
        'wall': "#",
        'player': "@",
        'empty': ".",
        'teleport': 'T',
        'small_teleport':'t',
        'dragon':'D' }

    items = {'diamond': '*',
            'dagger': ']',
            'super_mace': ')',
            'wand': 'Y',
            'arrow' : '/' }

    inventory = []
    backpack = {}
    map_counter = 0
    room = read_map_from_txt(choose_map(map_counter))
    pos = []
    item_counter = 0
    updater(room, stuff, pos)
    pressedkey = "initialize"
   
    print("press 0 to show time")

    while pressedkey != "x":
        
        pressedkey = getch()
        if pressedkey in(movement_buttons()):
            expected_movement_coordinates_x_y = set_movement_variable(pressedkey,room,pos) 
            if not expected_movement_coordinates_x_y[2] is stuff['wall']:
                enviroment(expected_movement_coordinates_x_y[2],stuff,items,inventory,item_counter,backpack,map_counter,room)
                movement_(expected_movement_coordinates_x_y,pos,room,stuff)

        if pressedkey == 'i':
            show_invetory(backpack)

        # if pressedkey == '0':
        #     print(start)
            