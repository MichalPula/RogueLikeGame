import csv
import os


def open_inventory_file():

    inventory = {}
    with open('inventory.txt', 'r') as f:
        f = csv.reader(f, delimiter=',')

        for line in f:
            try:
                inventory[line[0]] = (int(line[1]), int(line[2]), str(line[3]))
            except BaseException:
                continue

    return inventory


def save_inventory_to_file(inventory):
    with open('inventory.txt', 'w') as f:
        w = csv.writer(f, delimiter=',')

        for key, value in inventory.items():
            w.writerow((key, value[0], value[1], value[2]))


def add_item_to_inventory_file(inventory):

    with open('inventory.txt', 'a') as f:
        w = csv.writer(f, delimiter=',')

        for key, value in backpack.items():
            w.writerow((key, value[0], value[1], value[2]))


pass
