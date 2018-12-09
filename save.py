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
