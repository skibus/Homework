import datetime
import random
import csv
import time
import os

music = []


def load_music():
    album_name = []
    album_info = []
    with open('music.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        music_list = list(reader)                                            # strip removes blank spaces before and
    for el in music_list:                                                    # behind elements in the list
        album_name = (el[0].strip().lower(), el[1].strip().lower())
        album_info = (int(el[2].strip().lower()), el[3].strip().lower(), el[4].strip().lower())
        album = (album_name, album_info)
        music.append(album)
    return music


def add_album():
    album_name = []
    album_info = []
    for el in ['name of artist', 'name of the album']:
        album_name.append(input("Please enter %s: " % el))
    for el in ['year of realese', 'genre of the album', 'length of the album']:
        album_info.append(input("Please enter %s: " % el))

    if album_info[0].isdigit():                                                          # entered year must be int
        album_info[0] = int(album_info[0])
        with open('music.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([album_name[0], album_name[1], album_info[0], album_info[1], album_info[2]])
    else:
        os.system('clear')
        print ('\nIncorrect form of year. Use arabic numerals.')

    album_name = tuple(album_name)
    album_info = tuple(album_info)
    os.system('clear')
    print ('\nYour album has been added correctly.\n')
    print (' - '.join(album_name), end='     ')
    print (*album_info)
    music.append((album_name, album_info))
    return music


def find_album_by_artist():
    artist = input('Enter the album\'s artist name: ').lower()
    albums = []
    for album in music:
        for el in album:
            if artist in el:
                albums.append(album[0])
    if len(albums) != 0:
        print ((' - '.join(albums[0])).title())
    else:
        print('\nThere is no album made by ' + artist + '.')


def find_album_by_year():
    year = input('Enter the year of realese: ')
    albums = []
    if year.isdigit():
        year = int(year)
        for album in music:
            for el in album:
                if year in el:
                    albums.append(album[0])

        if len(albums) != 0:
            print (' - '.join(albums[0]))
        else:
            print (('\nThere is no album made in: %s.') % (year))
    else:
        print ('Only arabic numerals available.')


def find_musician_by_album():
    name = input('Enter the album name: ').lower()
    albums = []
    for album in music:
        for el in album:
            if name in el:
                albums.append(album[0])

    if len(albums) != 0:
        print (' - '.join(albums[0]).title())
    else:
        print ('\nThere is no album with this name.')


def find_album_by_letters():
    letters = input('Enter the letter(s) in the album\'s name: ').lower()
    albums = []
    for album in music:
        if letters in album[0][1]:
            albums.append(album[0])

    if len(albums) != 0:
        print (' - '.join(albums[0]).title())
    else:
        print ('\nThere is no album with \"' + letters + '\" in the name.')


def find_album_by_genre():
    genre = input('Enter the genre of the album: ').lower()
    albums = []
    for album in music:
        for el in album:
            if genre in el:
                albums.append(album[0])

    if len(albums) != 0:
        print (' - '.join(albums[0]).title())
    else:
        print('\nThere is no album in this genre.')


def sum_album_age():                                       # Multiply age by 2 every time when 7 pressed (bug)
    i = 0
    albums_age = []
    now = datetime.datetime.now()
    for album in music:
        age = now.year - music[i][1][0]
        albums_age.append(age)
        i += 1
    age = sum(albums_age)
    albums_age[:] = []
    print ('The age of all albums is: %d' % (age))


def random_album_by_genre():
    genre = input('Enter the genre of the album: ').lower()
    genre_list = []
    for album in music:
        for el in album:
            if genre in el:
                genre_list.append(album[0])

    if len(genre_list) != 0:
        drawn = random.choice(genre_list)
        print (' - '.join(drawn).title())
    else:
        print ('\nThere is no album in this genre.')


def main():
    start = True
    while True:

        load_music()
        print ('\n\nWelcome in the CoolMusic! Choose the action:\n')
        actions = [
        '1) Add new album',
        '2) Find albums by artist',
        '3) Find albums by year',
        '4) Find musician by album',
        '5) Find albums by letter(s)',
        '6) Find albums by genre',
        '7) Calculate the age of all albums',
        '8) Choose a random album by genre',
        '0) Exit\n']

        for action in actions:             # printing 1 element in actions in 1 row
            print (action)

        choose = input('What do you want to do? Choose option from 0 to 10. \n')
        if choose == '1':
            os.system('clear')
            add_album()
            time.sleep(3)
        elif choose == '2':
            os.system('clear')
            find_album_by_artist()
            time.sleep(2)
        elif choose == '3':
            os.system('clear')
            find_album_by_year()
            time.sleep(2)
        elif choose == '4':
            os.system('clear')
            find_musician_by_album()
            time.sleep(2)
        elif choose == '5':
            os.system('clear')
            find_album_by_letters()
            time.sleep(2)
        elif choose == '6':
            os.system('clear')
            find_album_by_genre()
            time.sleep(2)
        elif choose == '7':
            os.system('clear')
            sum_album_age()
            time.sleep(2)
        elif choose == '8':
            os.system('clear')
            random_album_by_genre()
            time.sleep(2)
        elif choose == '0':
            exit()
        else:
            print('There is no option like ' + choose + '.')


if __name__ == '__main__':
    main()
