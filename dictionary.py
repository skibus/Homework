import csv
import os
import time

dictionary = {}


def load_dictionary():
    with open('dictionary.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dictionary[row[0]] = (row[1], row[2])
    return dictionary


def search_by_appelation():
    appelation = input('What appelation are you looking for? ').lower().strip()
    if appelation in dictionary:
        appelation = '\nSource: '.join(dictionary[appelation])
        print (appelation)
    elif appelation not in dictionary:
        print ('There is no definition like ' + appelation + ' in the dictionary.')


def add_definition():
    appelation = input('What appelation do u want to add? ').lower()
    explanation = input('Enter the explanation for your appelation: ')
    source = input('Enter the source: ')
    new_definition = ', '.join([appelation, explanation, source])
    new_def = open('dictionary.csv', 'a')
    new_def.write(new_definition + '\n')
    new_def.close
    print ('\nYour appelation has been added correctly.\n')
    print (appelation + ' - ' + explanation + ' // Source: ' + source)


def sort_appelations():
    for key in sorted(dictionary):
        print (key)


def main():
    start = True
    while True:
        load_dictionary()
        actions = [
            '\nDictionary for a little programmer:',
            '1) search explanation by appellation',
            '2) add new definition',
            '3) show all appellations alphabetically',
            '0) exit']

        for action in actions:
            print (action)

        choose = input('What do you want to do? Choose option from 0 to 3. \n')
        if choose == '1':
            os.system('clear')
            search_by_appelation()
            time.sleep(3)
        elif choose == '2':
            os.system('clear')
            add_definition()
            time.sleep(3)
        elif choose == '3':
            os.system('clear')
            sort_appelations()
            time.sleep(3)
        elif choose == '0':
            exit()
        else:
            print('There is no option like ' + choose + '. Try again.')
            time.sleep(2)
if __name__ == '__main__':
    main()
