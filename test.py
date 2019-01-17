

# # if pressedkey is ('w' or 'W'):

# #             expected_north_movement = room[pos[0] - 1][pos[1]]

# #             if expected_north_movement is not stuff['wall']:
# #                 if expected_north_movement is stuff['dragon']:
# #                     dragon.starting_fight()

# # #                 if expected_north_movement is stuff['teleport']:
# # #                     map_counter += 1
# # #                     room = read_map_from_txt(choose_map(map_counter))
            
# # #                 for item in (items.values()):
# # #                     if expected_north_movement is item:
# # #                         pickup_to_inventory(item,inventory,backpack)
# # #                         up(room, stuff['empty'], stuff['player'], pos)
# # #                 else:
# # #                     up(room, stuff['empty'], stuff['player'], pos)
# # # #                     updater(room, stuff, pos)


# # tupel = [30, 550, 850]

# # tupel_ = [40, 50, 80]


# # for item in range(len(tupel_)):
# #     tupel[item] += tupel_[item]

# items = {'diamond': '*',
#         'dagger': ']',
#         'super_mace': ')',
#         'wand': 'Y',
#         'arrow' : '/' }

# print(tupel)

# inventory = []
# backpack = {}
# item = '*'

# def pickup_to_inventory(item, inventory,backpack):

#     inventory.append(item)

#     for item in inventory:

#         if item == '*':
#             item_counter = 1
#             diamond_values = [40,50,500]
#             for item in range(len(diamond_values)):
#                 if item_counter == 1:
#                     backpack['diamond'] = diamond_values
#                     item_counter += 1
#                 if item_counter > 1:
#                     for item in range(len(diamond_values)):
#                         diamond_values[item] += diamond_values[item]
            

       
#         elif item == '/':
#             backpack['arrow'] = (15, 10, 'weapon')
#         elif item == ')':
#             backpack['super mace'] = (50, 30, 'weapon')
#         elif item == 'Y':
#             values = (50,20, 'weapon')
#             backpack['wand'] = values
#         elif item == ']':
#             backpack['dagger'] = (120, 30, 'weapon')

#     return backpack

# print(backpack)


# items = [40,50,90]

# for item in range(len(items)):
#     items[item] += items[item]

# print(items)
values11 = [400,3000,500]
dictionary = {}
dictionary['diamond'] = values11


update = dictionary.get('diamond')
for values in range(len(update)):
    update[values] += update[values]

print(dictionary)

#dictionary['diamond'] = [current_values + 1 for current_values in dictionary['diamond']]