# Author: Wendi
# Descirption: This program is a simple song list that allows a user to track songs
# that they wish to learn and songs they have completed learning.
# GitHub URL:https://github.com/Wendy1990qwe/Starter.git

# song class
class Song:
    def __init__(self, title, artist, year, required):
        # constructor for song
        self.title = title
        self.artist = artist
        self.year = year
        self.required = required

    def getTitle(self):
        # get title
        return self.title

    def getArtist(self):
        # get artist
        return self.artist

    def getYear(self):
        # get year
        return self.year

    def getRequired(self):
        # get required
        return self.required

    def isRequired(self):
        # check if is required
        return self.required == 'y'

    def complete(self):
        # ccomplete the song
        self.required = 'n'


class SongList:
    def __init__(self):
        # constrcutor for songlist
        self.songList = []
        self.songsRequired = 0
        self.songsLearned = 0

    def loadSongs(self, filename):

        # pseudocode
        # open file:
        #	for each line in file:
        #		line=line.split("")
        #		title=line[0]
        #		artist=line[1]
        #		year=line[2]
        #		required=line[3]
        #		song=Song(title, artist, year, required)
        #		songList.add(song)
        #		sort(song)
        number = 0
        with open(filename) as file:
            for line in file:
                if line:
                    line = line.replace("\n", "")
                    data = line.split(",")
                    title = data[0]
                    artist = data[1]
                    year = int(data[2])
                    required = data[3]
                    song = Song(title, artist, year, required)
                    self.songList.append(song)
                    number += 1
                    if song.isRequired():
                        self.songsRequired += 1
                    else:
                        self.songsLearned += 1
        self.songList = sorted(self.songList, key=lambda song: (song.artist, song.title))
        print(number, "songs loaded")

    def listSongs(self):
        # list songs
        for i in range(len(self.songList)):
            song = self.songList[i]
            required = ""
            title = song.getTitle()
            artist = song.getArtist()
            year = song.getYear()
            if song.isRequired():
                required = "*"
            print("%d. %-1Ls %-30s - %-25s (%d)" % (i, required, title, artist, year))
        print("%d songs learned, %d songs still to learn" % (self.songsLearned, self.songsRequired))

    def addSong(self):
        # add song
        title = ""
        while True:
            title = input("Title:\n")
            if not title:
                print("Input can not be blank")
            else:
                break
        artist = ""
        while True:
            artist = input("Artist:\n")
            if not artist:
                print("Input can not be blank")
            else:
                break
        year = None
        while True:
            year = input("Year:\n")
            if not year:
                print("Input can not be blank")
            try:
                year = int(year)
                if year < 0:
                    print("Number must be >= 0")
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")

        required = 'y'
        song = Song(title, artist, year, required)
        self.songList.append(song)
        self.songList = sorted(self.songList, key=lambda song: (song.artist, song.title))
        print("%s by %s (%d) added to song list" % (title, artist, year))

    def completeSong(self):
        # pseudocode:
        # index
        # if index is legal and song is required:
        #	complete(song)
        if self.songsRequired == 0:
            print("No more songs to learn!")
            return

        index = None
        while True:
            index = input("Enter the number of a song to mark as learned:\n")
            if not index:
                print("Input can not be blank")
            try:
                index = int(index)
                if index < 0:
                    print("Number must be >= 0")
                elif index >= len(self.songList):
                    print("Number is out of range, there are only %d songs" % (len(self.songList)))
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")
        song = self.songList[index]
        if not song.isRequired():
            print("%s by %s (%d) has been learned" % (song.getTitle(), song.getArtist(), song.getYear()))
        else:
            song.complete()
            self.songsRequired -= 1
            self.songsLearned += 1
            print("%s by %s (%d) learned" % (song.getTitle(), song.getArtist(), song.getYear()))

    def saveSongs(self, filename):
        # save song
        with open(filename, 'w') as f:
            for song in self.songList:
                title = song.getTitle()
                artist = song.getArtist()
                year = song.getYear()
                required = song.getRequired()
                songStr = title + "," + artist + "," + str(year) + "," + required + "\n"
                f.write(songStr)
        print("%d songs saved to songs.csv\nHave a nice day :)" % (len(self.songList)))  # main program


def main():
    print("Songs To Learn 1.0 - by Wendi")
    songList = SongList()
    songList.loadSongs("song.csv")
    menu = "Menu:\n" + \
           "L - List songs\n" + \
           "A - Add new song\n" + \
           "C - Complete a song\n" + \
           "Q - Quit\n"
    while True:
        option = input(menu)
        if option == 'L':
            songList.listSongs()
        elif option == 'A':
            songList.addSong()
        elif option == 'C':
            songList.completeSong()
        elif option == 'Q':
            songList.saveSongs("song.csv")
            break
        else:
            print("Invalid menu choice")


main()
