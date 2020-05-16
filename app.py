from pytube import YouTube
import colorConsole as color
import os
import random

renk = color.mycolors

class YouTubeInstaller:

    def __init__(self,ytLink = "",iTag=0,downloadDurum= False, videoAdi = "", resolitions = [["360p","+",18],["720p","-",22]]):
        self.ytLink = ytLink
        self.videoAdi = videoAdi
        self.resolitions = resolitions
        self.iTag = iTag
        self.downloadDurum = downloadDurum

    def videoGiris(self,video):
        print("İşleniyor...")
        self.ytLink = YouTube(video)
        self.videoAdi = self.ytLink.title
        return self.videoAdi

    def bul(self,cevap):
        for i in range(len(self.resolitions)):
            if cevap == self.resolitions[i][1]:
                return self.resolitions[i][2]

    def mp4Download(self):
        liste = self.ytLink.streams.filter(progressive=True,file_extension="mp4")
        print("\n\n")
        for i in range(len(liste)):
            print(self.resolitions[i][0], " => ", self.resolitions[i][1])
        islem = input("\n\nÇözünürlük Seçin =>")
        #iTag Seçildi
        self.iTag = self.bul(islem)
        self.ytDownload()

    def controlDownload(self):
        return self.downloadDurum

    def ytDownload(self):
        try:
            stream = self.ytLink.streams.get_by_itag(self.iTag)
            print(f"{renk.OKGREEN}İndirme İşlemi Başladı! Lütfen Bekleyin... {renk.ENDC}")
            stream.download()
            konum = os.getcwd()
            print(f"{renk.OKBLUE}İndirme İşlemi Tamamlandı! {renk.ENDC}")
            print("Dosya Konumu : {0}{1}".format(konum,self.videoAdi))
            self.downloadDurum = True
        except e:
            self.downloadDurum = False
            print("Hata : ",e)

    def uznatiDegistir(self,dosyaAdi,yeniIsım,yeniUzanti):
        try:
            yeniIsım,ext = os.path.splitext(dosyaAdi)
            os.rename(dosyaAdi,yeniIsım+yeniUzanti)
        except FileExistsError:
            rndSayi = random.randint(0,99)
            yeniIsım,ext = os.path.splitext(dosyaAdi)
            os.rename(dosyaAdi,yeniIsım+str(rndSayi)+yeniUzanti)

    def titleArindir(self,zTitle):
        zTitle = zTitle.replace("/","")
        zTitle = zTitle.replace(".","")
        return zTitle

    def mp3Download(self):
        liste = self.ytLink.streams.filter(only_audio=True)
        self.iTag = 251
        self.ytDownload()

        yeniDosyaAdi = self.titleArindir(self.videoAdi)
        self.uznatiDegistir(yeniDosyaAdi+".webm",self.videoAdi,".mp3")



















###
