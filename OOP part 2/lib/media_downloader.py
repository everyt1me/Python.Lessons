from subprocess import call
import os
if __name__ == "__main__":
    downloader


class downloader():
    def menu(self):
        choise = int(
            input("1. Download Movie\n2. Download Playlist (Movie)\n====>>> "))
        return choise

    def download_youtube_single_media(self):
        movie_url = input("Enter movie URL => ")
        movie_info = "youtube-dl " + movie_url + " -F"
        print("Test URL => ", movie_info)
        call(movie_info, shell=False)
        format = input("Enter Format code : ")
        os.chdir("Downloads")
        download_command = "youtube-dl -f " + format + " " + movie_url + " -c"
        call(download_command, shell=False)
