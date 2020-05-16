import colorConsole as color
import time
import app

renk = color.mycolors
downloader = app.YouTubeInstaller()

while True:
    print(f"{renk.WARNING} --------------- YouTube Mp3/Mp4 Downloader --------------- {renk.ENDC}")
    print(f"{renk.FAIL}\nÇıkış İçin => exit {renk.ENDC}")
    video = input(f"{renk.OKGREEN}YouTube Link => {renk.ENDC}")
    #video = "https://www.youtube.com/watch?v=4EVV3Cw98r4"
    if video == "exit":
        print("Çıkış Yapılıyor....")
        time.sleep(0.8)
        break
    else:
        try:
            isim = downloader.videoGiris(video)
            print(f"{renk.OKBLUE}[TITLE] =>", isim,f"{renk.ENDC}")

            while True:
                print("\nMp4 => +\nMp3 => -")
                print("Bir Üst Menü İçin => exit")
                format = input("\nFormat Seçin => ")

                if format == "exit":
                    break
                elif format == "+":
                    downloader.mp4Download()
                    durum = downloader.controlDownload()
                    if durum == True:
                        break
                    else:
                        exit()
                elif format == "-":
                    downloader.mp3Download()
                    durum = downloader.controlDownload()
                    if durum == True:
                        break
                    else:
                        exit()
                else:
                    print("Geçersiz İşlem!!")
        except:
            print(f"{renk.FAIL}YouTube Linkini Doğru Girdiğinizden Emin Olun!{renk.ENDC}")
















print("İyi Günler...")

# https://www.youtube.com/watch?v=4EVV3Cw98r4
