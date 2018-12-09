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
