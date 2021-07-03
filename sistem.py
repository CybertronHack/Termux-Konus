from gtts import gTTS
import os

metin = input("Metin Giriniz : ")

isim = input("Dosya İsmi Giriniz : ")

language = 'tr'

output = gTTS(text=metin, lang=language, slow=False)

output.save(""+isim+".mp3")

os.system("mpv {}.mp3".format(isim))
