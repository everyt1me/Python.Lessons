from lib.media_downloader import downloader

media_file = downloader()

exit = False
while not exit:
    choise = media_file.menu()
    if choise == 1:
        media_file.download_youtube_single_media()
    elif choise == 2:
        print("User choise => ", choise)
    elif choise == 0:
        exit = True
        print("Bye!")
    else:
        print("R.T.F.M.")
