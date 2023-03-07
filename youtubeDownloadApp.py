import tkinter as tk
from pytube import YouTube

def button_clicked():
     video_url = entry.get()
     yt = YouTube(video_url)
     stream = yt.streams.get_highest_resolution()
     stream.download(output_path='desktop')
     print("Bu program Mehmet Enes DAĞ tarafından geliştirilmiştir. İzinsiz kullanılması ve kopyalanması yasaktır. İletişim için: mhmtenesdg@gmail.com")


root = tk.Tk()
root.title("Youtube Müzik İndirme")

 # Giriş kutusu oluşturur
entry = tk.Entry(width=120)
entry.pack()

 # Buton oluşturur
button = tk.Button(root, text="Gönder", command=button_clicked)
button.pack()

 #Bilgilendirme yazısı ekler.
label= tk.Label(text="İndirmek istediğiniz Youtube Video Linkini Yukarıda verilen alana giriniz.\nBu program ticari amaçlara uygun değildir. Lütfen Emeğe Saygı Gösterin.\nBu metni görüntülüyorsanız telif haklarına dair tüm sorumlulukları kabul etmiş olursunuz.", width=100, height=10)
label.pack()
label= tk.Label(text="Mehmet Enes DAĞ keyifli dinlemeler diler.", width=100, height=10)
label.pack()
root.mainloop()
