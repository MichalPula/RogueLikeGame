from operator import itemgetter


def display_highscore():  # define function display

    with open('highscore.txt') as f:  # open file highscore.txt
        read_data = f.read()  # read characters from file highscore.txt
    if not read_data:  # check if file is not empty
        print('Empty!')  # if file was empty display "Empty!"
    else:
        print(read_data)  # if somethink is inside file display content


def add_score_to_file(score):  # call function add score

    highscore = []
    with open('highscore.txt') as f:  # open file highscore.txt
        # read data and return a list of the lines in the string, breaking at
        # line boundaries
        temp = f.read().splitlines()
    for i in temp:  # start a in temporary files
        highscore.append(i.split(' '))

    # users was able to adding his name to hall of fame
    name = input('Write your name here: ')
    value = [name, score]
    # Add an value(value = [name, score]) to the end of the list.
    highscore.append(value)

    for i in range(len(highscore)):
        highscore[i][1] = int(highscore[i][1])
    # operator.itemgetter (n) tworzy podklasę, która zakłada obiekt
    # iterowalny(that is just what operator.itemgetter(1) will give you: A
    # function that grabs the first item from a list-like object.)
    highscore = sorted(highscore, key=itemgetter(1), reverse=True)
    save_highscore_to_file(highscore)


def save_highscore_to_file(highscore):

    with open('highscore.txt', 'w') as f:
        for i in range(len(highscore)):
            f.write(" ".join([str(highscore[i][0]), str(highscore[i][1])]))
            f.write('\n')


if __name__ == '__main__':
    add_score_to_file()
