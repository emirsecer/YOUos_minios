import time
import requests
import webbrowser
import sqlite3
from bs4 import BeautifulSoup
from folium.plugins import MiniMap
import folium
from tkinter import *
import calendar

def TakvimUygulamasi():

    class TakvimUygulamasi :
        def __init__(self, pencere) :
            self.pencere = pencere
            self.pencere.title ("Takvim Uygulaması")

            # Takvim widget'ı oluştur
            self.takvim_widget = tk.Label (self.pencere, font=('Arial', 14))

            # Takvim widget'ını yerleştir
            self.takvim_widget.pack (padx=20, pady=20)

            # Düğme widget'ları oluştur
            self.ilk_yil_dugmesi = tk.Button (self.pencere, text="Önceki Yıl", command=self.ilk_yil)
            self.ilk_yil_dugmesi.pack (side=tk.LEFT, padx=20, pady=20)

            self.sonraki_yil_dugmesi = tk.Button (self.pencere, text="Sonraki Yıl", command=self.sonraki_yil)
            self.sonraki_yil_dugmesi.pack (side=tk.RIGHT, padx=20, pady=20)

            self.ilk_ay_dugmesi = tk.Button (self.pencere, text="Önceki Ay", command=self.ilk_ay)
            self.ilk_ay_dugmesi.pack (side=tk.LEFT, padx=20, pady=20)

            self.sonraki_ay_dugmesi = tk.Button (self.pencere, text="Sonraki Ay", command=self.sonraki_ay)
            self.sonraki_ay_dugmesi.pack (side=tk.RIGHT, padx=20, pady=20)

            # Varsayılan olarak, takvim ay ve yılını bugünün tarihine ayarla
            bugun = calendar.datetime.date.today ()
            self.ay = bugun.month
            self.yil = bugun.year
            self.takvim = calendar.monthcalendar (self.yil, self.ay)
            self.guncelle ()

            # Pencere kapatıldığında anasayfaya_don fonksiyonunu çağır
            self.pencere.protocol ("WM_DELETE_WINDOW", self.anasayfaya_don)

        def guncelle(self) :
            # Takvim widget'ını güncelle
            takvim_metni = f"{calendar.month_name[self.ay]} {self.yil}\n\n"
            for hafta in self.takvim :
                hafta_metni = "  ".join ([str (gun) if gun != 0 else "  " for gun in hafta])
                takvim_metni += hafta_metni + "\n"
            self.takvim_widget.config (text=takvim_metni)

        def ilk_yil(self) :
            # Takvim yılını bir önceki yıla ayarla ve güncelle
            self.yil -= 1
            self.takvim = calendar.monthcalendar (self.yil, self.ay)
            self.guncelle ()

        def sonraki_yil(self) :
            # Takvim yılını bir sonraki yıla ayarla ve güncelle
            self.yil += 1
            self.takvim = calendar.monthcalendar (self.yil, self.ay)
            self.guncelle ()

        def ilk_ay(self) :
            # Takvim ayını bir önceki aya ayarla ve güncelle
            if self.ay == 1 :
                self.ay = 12
                self.yil -= 1
            else :
                self.ay -= 1
            self.takvim = calendar.monthcalendar (self.yil, self.ay)
            self.guncelle ()

        def sonraki_ay(self) :
            # Takvim ayını bir sonraki aya ayarla ve güncelle
            if self.ay == 12 :
                self.ay = 1
                self.yil += 1
            else :
                self.ay += 1
            self.takvim = calendar.monthcalendar (self.yil, self.ay)
            self.guncelle ()

        def anasayfaya_don(self):
            # Pencere kapatıldığında anasayfaya dön
            self.pencere.destroy()
            anasayfayadon()
            # Burada anasayfaya dönmek için gerekli kodu yazabilirsiniz

    # Ana program
    if __name__ == "__main__":
        # Tkinter penceresini oluştur
        pencere = tk.Tk()

        # Takvim uygulamasını oluştur
        takvim_uygulamasi = TakvimUygulamasi(pencere)

        # Pencereyi göster
        pencere.mainloop()
def kişiler_kişiler():
    def arama_yap():
        numara = numara_alani.get()
        sonuc_alani.config(state=NORMAL)
        sonuc_alani.insert(
            END,
            f"\nAranan numara: {numara}\nArama yapılıyor... Aradığınız kişi müsait değil!")
        sonuc_alani.config(state=DISABLED)

    def arama_gecmisi():
        sonuc_alani.config(state=NORMAL)
        sonuc_alani.insert(END, "\nARAMA GEÇMİŞİ\n\n\n\n\n")
        sonuc_alani.config(state=DISABLED)

    def kisiler():
        pass

    def anasayfayadon():
        # anasayfaya dönüş işlemleri burada yapılır
        pass

    pencere = Tk()
    pencere.title("Arama Uygulaması")

    baslik = Label(pencere, text="Yapmak istediğiniz işlem sekmesini seçiniz:")
    baslik.pack()

    arama_yap_btn = Button(pencere, text="Arama Yap", command=arama_yap)
    arama_yap_btn.pack()

    arama_gecmisi_btn = Button(
        pencere,
        text="Arama Geçmişi",
        command=arama_gecmisi)
    arama_gecmisi_btn.pack()

    kisiler_btn = Button(pencere, text="Kişiler", command=kisiler)
    kisiler_btn.pack()

    numara_alani = Entry(pencere)
    numara_alani.pack()

    sonuc_alani = Text(pencere, state=DISABLED)
    sonuc_alani.pack()

    def kapat_event():
        anasayfayadon()
        pencere.destroy()

    pencere.protocol("WM_DELETE_WINDOW", kapat_event)

    pencere.mainloop()
def notlar():
    import tkinter as tk
    import tkinter.simpledialog as tk_simpledialog
    from tkinter import messagebox, filedialog
    import os

    class NotlarApp (tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("Notlar Uygulaması")
            self.pack()
            self.create_widgets()
            # pencere kapatıldığında veya "Çıkış" düğmesine basıldığında
            # anasayfayadon fonksiyonunu çağırma

            self.quit_button.config(command=self.anasayfayadon)

        def anasayfayadon(self):
            anasayfayadon()

        def create_widgets(self):
            self.not_ekle_button = tk.Button(
                self, text="Not Ekle", command=self.not_ekle)
            self.not_ekle_button.pack(side="top")

            self.not_goruntule_button = tk.Button(
                self, text="Notları Görüntüle", command=self.not_goruntule)
            self.not_goruntule_button.pack(side="top")

            self.not_duzenle_button = tk.Button(
                self, text="Not Düzenle", command=self.not_duzenle)
            self.not_duzenle_button.pack(side="top")

            self.not_sil_button = tk.Button(
                self, text="Not Sil", command=self.not_sil)
            self.not_sil_button.pack(side="top")

            self.quit_button = tk.Button(
                self, text="Çıkış", fg="red", command=self.master.destroy)
            self.quit_button.pack(side="bottom")

        def not_ekle(self):
            filename = filedialog.asksaveasfilename(defaultextension=".txt")
            if filename:
                with open(filename, "w") as file:
                    file.write("")
                messagebox.showinfo(
                    "Notlar Uygulaması",
                    f"{filename} adlı not defteri oluşturuldu.")

        def not_goruntule(self):
            filename = filedialog.askopenfilename(defaultextension=".txt")
            if filename:
                with open(filename, "r") as file:
                    content = file.read()
                messagebox.showinfo(f"{filename} Not Defteri", content)

        def not_duzenle(self):
            filename = filedialog.askopenfilename(defaultextension=".txt")
            if filename:
                with open(filename, "r") as file:
                    content = file.read()
                content = tk_simpledialog.askstring(
                    f"{filename} Not Defteri", "Notu düzenleyin:", initialvalue=content)
                with open(filename, "w") as file:
                    file.write(content)
                messagebox.showinfo(
                    "Notlar Uygulaması",
                    f"{filename} adlı not defteri güncellendi.")

        def not_sil(self):
            filename = filedialog.askopenfilename(defaultextension=".txt")
            if filename:
                response = messagebox.askyesno(
                    "Notlar Uygulaması",
                    f"{filename} adlı not defterini silmek istediğinizden emin misiniz?")
                if response == tk.YES:
                    try:
                        os.remove(filename)
                        messagebox.showinfo(
                            "Notlar Uygulaması",
                            f"{filename} adlı not defteri silindi.")
                    except BaseException:
                        messagebox.showerror(
                            "Notlar Uygulaması",
                            f"{filename} adlı not defteri silinemedi.")

    root = tk.Tk()
    app = NotlarApp(master=root)
    app.mainloop()
def hava_durumu():
    import tkinter as tk
    import requests
    from bs4 import BeautifulSoup

    def hava_durumu_sorgula():
        # Hava durumu verilerini sorgulama fonksiyonu
        sehir = sehir_entry.get()
        hava_durumu_verisi = get_weather_data(sehir)

        # Hava durumu verilerini görüntüleme
        hava_durumu_alani.delete("1.0", tk.END)
        if hava_durumu_verisi is not None:
            hava_durumu_alani.insert(tk.END, hava_durumu_verisi)
        else:
            hava_durumu_alani.insert(tk.END, "Hava durumu verileri alınamadı.")

        # Pencereyi kapatma
        hava_durumu_penceresi.destroy()
        anasayfayadon()

    def get_weather_data(city):
        # Hava durumu verilerini alma işlevi
        url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            weather_data = soup.find_all(
                class_='b-forecast__table-description-content')[0].get_text().strip()

            return weather_data
        else:
            return None

    # Hava durumu sorgulama arayüzünü oluşturma
    hava_durumu_penceresi = tk.Tk()
    hava_durumu_penceresi.title("Hava Durumu")

    sehir_sorgulama_cercevesi = tk.Frame(hava_durumu_penceresi)

    sehir_label = tk.Label(sehir_sorgulama_cercevesi, text="Şehir:")
    sehir_label.pack(side="left")

    sehir_entry = tk.Entry(sehir_sorgulama_cercevesi)
    sehir_entry.pack(side="left")

    sorgula_button = tk.Button(
        sehir_sorgulama_cercevesi,
        text="Sorgula",
        command=hava_durumu_sorgula)
    sorgula_button.pack(side="left")

    sehir_sorgulama_cercevesi.pack()

    hava_durumu_alani = tk.Text(hava_durumu_penceresi)
    hava_durumu_alani.pack()

    def pencereyi_kapat():
        # Pencereyi kapatma
        hava_durumu_penceresi.destroy()
        anasayfayadon()

    hava_durumu_penceresi.protocol("WM_DELETE_WINDOW", pencereyi_kapat)

    hava_durumu_penceresi.mainloop()
def mesajlar():
    import tkinter as tk

    def mesajlar():
        # Mesajlar penceresini oluşturma
        mesajlar_penceresi = tk.Toplevel()
        mesajlar_penceresi.title("Mesajlar")

        # Mesajlar alanını oluşturma
        mesajlar_alani = tk.Text(mesajlar_penceresi)
        mesajlar_alani.pack()

        # Mesaj gönderme bölümünü oluşturma
        mesaj_gonderme_cercevesi = tk.Frame(mesajlar_penceresi)

        kisi_label = tk.Label(
            mesaj_gonderme_cercevesi,
            text="Gönderilecek Kişi:")
        kisi_label.pack(side="left")

        kisi_entry = tk.Entry(mesaj_gonderme_cercevesi)
        kisi_entry.pack(side="left")

        mesaj_label = tk.Label(mesaj_gonderme_cercevesi, text="Mesajınız:")
        mesaj_label.pack(side="left")

        mesaj_entry = tk.Entry(mesaj_gonderme_cercevesi)
        mesaj_entry.pack(side="left")

        def mesaj_gonder():
            # Mesaj gönderme işlevini gerçekleştirme
            kisi = kisi_entry.get()
            mesaj = mesaj_entry.get()

            # Mesajı mesajlar alanına ekleme
            mesajlar_alani.insert(tk.END, f"Gönderilen Kişi: {kisi}\n")
            mesajlar_alani.insert(tk.END, f"Mesaj: {mesaj}\n\n")

            # Girdi kutularını temizleme
            kisi_entry.delete(0, tk.END)
            mesaj_entry.delete(0, tk.END)

        gonder_button = tk.Button(
            mesaj_gonderme_cercevesi,
            text="Gönder",
            command=mesaj_gonder)
        gonder_button.pack(side="left")

        mesaj_gonderme_cercevesi.pack()

        # Mesajları görüntüleme
        mesajlar_alani.insert(
            tk.END, "Gelen hiç yeni mesaj yok. Önceki mesajlar listelenmiştir.\n\n")

        def pencereyi_kapat():
            # Pencere kapatılınca anasayfayadon fonksiyonunu çağırma
            mesajlar_penceresi.destroy()
            anasayfayadon()
        mesajlar_penceresi.mainloop()

    # Örnek kullanım
    root = tk.Tk()

    mesajlar_button = tk.Button(root, text="Mesajlar", command=mesajlar)
    mesajlar_button.pack()

    root.mainloop()
def ayarlar():
    def şifre_değiş():
        import sqlite3

        # Veritabanı bağlantısı oluşturun
        conn = sqlite3.connect(
            r"C:\Users\EMİR\Desktop\dersle ve yazılımla alakalı\yazılım eğitim ve çalışmaları\çalışmalar\bu_bir_dt_denemesidir_6.db")

        # Bir imleç oluşturun
        cursor = conn.cursor()

        # "cihaz1" adlı bir kayıt var mı diye kontrol edin
        cursor.execute("SELECT * FROM tablo WHERE id = 'cihazbir'")
        existing_record = cursor.fetchone()

        if existing_record:
            # "cihazbir" adlı kayıt varsa, yeni bir şifre sorun
            new_password = input("Lütfen yeni bir şifre girin: ")

            # Yeni şifreyi "tablo" adlı tabloya kaydedin
            cursor.execute(
                "UPDATE tablo SET password = ? WHERE id = 'cihazbir'", (new_password,))
            conn.commit()
            print("Şifre başarıyla değiştirildi.")
        else:
            # "cihaz1" adlı kayıt yoksa, yeni bir kayıt ekleyin
            id = 'cihaz1'
            password = '12345'
            cursor.execute(
                "INSERT INTO tablo (id, password) VALUES (?, ?)", (id, password))
            conn.commit()
            print("Yeni bir kayıt oluşturuldu.")

        # Veritabanı bağlantısını kapatın
        conn.close()

    def MEUP():

        def cihaz_işlemleri():
            """

            Kullanıcıdan cihaz işlemleri seçimlerini alır ve ilgili işlemi yapar.
            """

            cihazlar = {}

            print("1- Cihazımı bul")

            print("2- Güncelleme yap")

            print("3- Sıfırlama yap")

            print("4- Şifremi aç")

            print("5- Uygulama yükle")

            print("6- Çıkış")

            secim = input("İşlem seçin: ")

            if secim == "1":

                cihaz_adi = input("Cihaz adı girin: ")

                cihaz = cihaz_bul(cihazlar, cihaz_adi)

                if cihaz is None:

                    # Sözlükte cihaz yok, yeni bir cihaz ekle

                    cihazlar[cihaz_adi] = {
                        "guncelleme": False, "sifre": "1234", "uygulamalar": []}

                    print(f"{cihaz_adi} adlı yeni bir cihaz eklendi.")

                else:

                    print(f"{cihaz_adi} adlı cihaz zaten var.")

            elif secim == "2":

                cihaz_adi = input("Cihaz adı girin: ")

                cihaz = cihaz_bul(cihazlar, cihaz_adi)

                if cihaz is not None:

                    cihaz["guncelleme"] = True

                    print(f"{cihaz_adi} adlı cihaza güncelleme yapılıyor.")

                else:

                    print(f"{cihaz_adi} adlı cihaz bulunamadı.")

            elif secim == "3":

                cihaz_adi = input("Cihaz adı girin: ")

                cihaz = cihaz_bul(cihazlar, cihaz_adi)

                if cihaz is not None:

                    cihaz["sifre"] = "1234"

                    print(f"{cihaz_adi} adlı cihazın şifresi sıfırlandı.")

                else:

                    print(f"{cihaz_adi} adlı cihaz bulunamadı.")

            elif secim == "4":

                cihaz_adi = input("Cihaz adı girin: ")

                cihaz = cihaz_bul(cihazlar, cihaz_adi)

                if cihaz is not None:

                    print(f"{cihaz_adi}")

                    # Boş bir kullanıcı sözlüğü oluşturun

        def cihaz_bul(cihazlar, cihaz_adi):
            """

            Verilen cihaz adına göre, cihazların sözlüğünde eşleşen bir cihaz varsa

            bu cihazı döndürür. Aksi halde None döndürür.
            """

            if cihaz_adi in cihazlar:

                return cihazlar[cihaz_adi]

            else:

                print(f"{cihaz_adi} adlı cihaz bulunamadı.")

                return None

        kullanicilar = {}

        # Kullanıcıları kaydetmek için bir fonksiyon tanımlayın

        def kaydet():

            # Kullanıcı adını ve şifreyi kullanıcıdan alın

            kullanici_adi = input("Kullanıcı adı: ")

            sifre = input("Şifre: ")

            # Kullanıcı adının sözlükte olup olmadığını kontrol edin

            if kullanici_adi in kullanicilar:

                print("Bu kullanıcı adı zaten mevcut.")

            else:

                # Kullanıcı adı sözlükte yoksa, yeni bir kullanıcı ekleyin

                kullanicilar[kullanici_adi] = sifre

                print("Kullanıcı başarıyla eklendi.")

        # Giriş yapmak için bir fonksiyon tanımlayın

        def giris():

            # Kullanıcı adını ve şifreyi kullanıcıdan alın

            kullanici_adi = input("Kullanıcı adı: ")

            sifre = input("Şifre:")

            # Kullanıcı adı ve şifrenin sözlükte eşleştiğini kontrol edin

            if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:

                print("Giriş başarılı.")

                cihaz_işlemleri()

            else:

                print("Kullanıcı adı veya şifre hatalı.")

        # Şifremi unuttum için bir fonksiyon tanımlayın

        def sifremi_unuttum():

            # Kullanıcı adını alın

            kullanici_adi = input("Kullanıcı adı: ")

            # Kullanıcı adının sözlükte olup olmadığını kontrol edin

            if kullanici_adi in kullanicilar:

                # Yeni şifreyi kullanıcıdan alın ve sözlüğe kaydedin

                yeni_sifre = input("Yeni şifre: ")

                kullanicilar[kullanici_adi] = yeni_sifre

                print("Şifre başarıyla değiştirildi.")

            else:

                print("Bu kullanıcı adı mevcut değil.")

        # Sonsuz bir döngü başlatın ve kullanıcıya seçenekler sunun

        while True:

            print("1 - Kaydol")

            print("2 - Giriş yap")

            print("3 - Şifremi unuttum")

            print("4 - Çıkış")

            secim = input("Seçiminiz: ")

            if secim == "1":
                kaydet()

            elif secim == "2":

                giris()

            elif secim == "3":

                sifremi_unuttum()

            elif secim == "4":
                anasayfayadon()

            else:

                print("Geçersiz seçim. Lütfen tekrar deneyin.")

    def cihaz_hakkında():

        def yazılım():

            print("yazılım sürümü =6.0(beta)")

        def beta():
            print(

                "beta sürümüne katılıyıorsunuz. \n beta sürümlerinin kararsız, hatalı olabileceğini unutmayın. \n devam etmek için beta sözleşmesini onaylayın. ")

            betaonay = input("onaylıyor musunuz (e \\ h")

            if betaonay == "evet":
                print(

                    "beta kaydınız yapıldı. yakında güncellemeniz teslim edilecek \n güncellemeler, denetle kısmını kontrol edin")
                anasayfayadon()

            elif betaonay == "hayır":

                print("beta kaydı iptal edildi.")
                anasayfayadon()

            else:
                anasayfayadon()

        def güncelleme_var_mı():

            print(
                "GÜNCELLEMELERİ DENETLE\n en son sürüm yüklü, yeni güncelleme yok.\n \n\n\n beta ya kaydol.")

        def depolama():

            print("52GB \\ 512 GB ")

            print(
                "MEos depolama web sayfasından daha fazla depolama alanı satın alabilirsiniz.")

        def lisans_durumu():

            print("lisanslı ve aktif")
            anasayfayadon()

        def ram():

            print("ram 6 GB")

            print(
                "sanal ram özelliğini açarsanız hafızadan bir miktar işgal edilerek 8 GB ram a tamamlanır."
                "")

        print(

            "cihaz HAKKINDA \n yazılım sürümü \n güncellemeleri denetle\n betaya kaydol\n  depolama  \n  lisans durumu \n ram  ")
        anasayfayadon()

        ekdenetim = input(":")

        if ekdenetim == "güncellemeleri denetle":

            güncelleme_var_mı()

        elif ekdenetim == "betaya kaydol.":

            beta()

        elif ekdenetim == "yazılım sürümü":

            yazılım()

        elif ekdenetim == "depolama":
            depolama()

        elif ekdenetim == "lisans durumu":

            lisans_durumu()

        elif ekdenetim == "ram":
            ram()

        else:
            anasayfayadon()

    def bağlantılar():

        import subprocess

        def wifi():
            print("Kullanılabilir ağlar:")
            try:
                result = subprocess.check_output(
                    ["netsh", "wlan", "show", "network"])
                result = result.decode("ascii")
                print(result)
            except subprocess.CalledProcessError as e:
                print("Ağlar listelenirken bir hata oluştu:", e)
            anasayfayadon()

        def bluetooth():
            print("Daha önceden bağlanmış cihazlar:")
            try:
                result = subprocess.check_output(["btdiscovery", "-all"])
                result = result.decode("ascii")
                print(result)
            except subprocess.CalledProcessError as e:
                print("Cihazlar listelenirken bir hata oluştu:", e)
            anasayfayadon()

        def kişisel_erişim():
            print("Bağlı cihazlar:")
            try:
                result = subprocess.check_output(
                    ["netsh", "wlan", "show", "hostednetwork"])
                result = result.decode("ascii")
                print(result)
            except subprocess.CalledProcessError as e:
                print("Cihazlar listelenirken bir hata oluştu:", e)

            print("Ek ayarlar:")
            print("Tek seferlik veri sınırı")
            print("Bağlantı noktasını otomatik kapat")
            print("USB ile veri paylaşımı")

            anasayfayadon()

        def yansıt():

            print("cihaz seçildi \n yansıtılıyor")
            anasayfayadon()

        def yazdırma():

            print(
                "yazıcı seçildi ve yazdırmaya hazır belge seçin ve paylaşım ekranından yazdıra tıklayın.")
            anasayfayadon()

        def vpn():

            print("vpn servisi mevcut değil \n mağazayı ziyaret edin")
            anasayfayadon()

        def veri_kullanım():

            print("web sayfası yükleniyor")
            anasayfayadon()

        print(

            "BAĞLANTILAR\n wifi\n bluetooth\n kişisel erişim noktası\nyansıt\nyazdırma\n vpn\n veri kullanma istatistikleri ve daha fazla bilgi")

        bağlantılar = input(":")

        if bağlantılar == "wifi":

            wifi()

        if bağlantılar == "bluetooth":

            bluetooth()

        if bağlantılar == "kişisel erişim noktası":

            kişisel_erişim()

        if bağlantılar == "yansıt":
            yansıt()

        if bağlantılar == "yazdırma":

            yazdırma()

        if bağlantılar == "vpn":

            vpn()

        if bağlantılar == "veri kullanma istatistikleri ve daha fazla bilgi":

            veri_kullanım()

    def kişiselleştirme():

        print("KİŞİSELLEŞTİRME\nkilit ekranı\n ses ve titreşim \n ekran ve başlatıcı \n duvar kağıdı")

        kişiselleştirme = input(":")

        if kişiselleştirme == "kilit ekranı":
            print(

                "KİLİT EKRANI \n uyku\nuyandırmak için kaldır \n bildirimler için uyandır \n kilit ekranı biçimi\n kestirmeler \nkilit ekranı döngüsü")

            kilit = input(":")

            if kilit == "uyku":
                print(

                    "cihazınız 1 dk işlem yapılmadığında ekranı kilitler. bu süreyi 5 dk\\ 10 \\ asla olarak da düzenleyebilirsiniz")
                anasayfayadon()

            if kilit == "uyandırmak için kaldır":

                print("cihazınızı kaldırdığınızda ekran otomatik olarak uyanır.")
                anasayfayadon()

            if kilit == "bildirimler için uyandır":

                print("gelen her bildirimde ekran uyandırılır.")

            if kilit == "kilit ekranı biçimi":
                print(

                    "saat konumu ,renkler,şekil, kısayollar,wigdetlar,simgeler ve animasyonlar ile kilit ekranınızı size özel hale getirin.\n birden fazla kilit ekranı ile her senaryoya uygun kilit ekranı oluşturun .")
                anasayfayadon()

            if kilit == "kestirmeler":

                print("kilit ekranındaki kestirmeleri buradan yönetebilirsiniz")
                anasayfayadon()

            if kilit == "kilit ekranı döngüsü":
                print(

                    "her ekran uyanışında yeni bir stil ile karşılaşın\n isterseniz tüm ögeleri  isterseniz seçtiğiniz ögeleri yenileyin.")
                anasayfayadon()

        if kişiselleştirme == "ses ve titreşim ":

            print("SES VE TİTREŞİM \n bildirim sesleri \n titreşim modelleri")

            ses = input(":")

            if ses == "bildirim sesleri":

                print("buradan bildirim\\çağrı\\ alarm seslerini yönetebilirsiniz.\n")
                print(

                    "------sesler-------\n ses1\n ses2\n ses3\n ses4\n ses5\n ses6\n ses7\n ses8\n ses9\n ses10\n ses11\n ses12\n ses13\n ses14\n ses15")

                sesseçim = input(":")

                print(sesseçim)

                print("seçim uygulandı.")
                anasayfayadon()

            if ses == "titreşim modelleri":
                print(

                    "titreşim 1 \n titreşim 2\n titreşim 3\n titreşim 4\n titreşim 5\n titreşim 6\n titreşim 7\n titreşim 8")

                titreşimseçim = input(":")

                print(titreşimseçim)

                print("titreşim modeli uygulandı")
                anasayfayadon()

        if kişiselleştirme == "ekran ve başlatıcı":

            print("EKRAN VE BAŞLATICI \n ekran ayarları \n başlatıcı ayarları")

            ekranseçim = input(":")

            if ekranseçim == "ekran ayarları":

                print(
                    "EKRAN AYARLARI\n parlaklık\n ekran modu \n karanlık mod\n ekran yenileme hızı")

                ekranayarı = input(":")

                if ekranayarı == "parlaklık":

                    print(
                        "_________*---- \n parlaklığı ayarlamak için imleci hareket ettirin.")
                    print(

                        "--------------------------\n gün ışığı modu\n gün ışığı modu açık olduğunda parlaklık %20 artar .15 dk sonra eski haline gelir. \n gün ışığı modu güç tüketimini arttırır. ")

                    print(
                        "mavi filtre ışığı \n mavi filtre ışığı modu gözünüze gelen zararlı ışıkları azaltır.")
                    anasayfayadon()

            if ekranseçim == "başlatıcı ayarları":

                print(
                    "BAŞLATICI AYARLARI\nsimgeler\n bildirimler\n rahatsız etme \n varsıyalan başlatıcı")

                başlatıcıayar = input(":")

                if başlatıcıayar == "simgeler":

                    print(
                        "şu anda varsıyılan simgeler kullanılıyor daha fazla tema için mağazayı ziyaret et.")
                    anasayfayadon()

                if başlatıcıayar == "bildirimler":

                    print(
                        "BİLDİRİMLER\n bildirim ayarları \n bildirim rozetleri\nbildirimleri yönet")

                    bildirimayar = input(":")

                    if bildirimayar == "bildirim ayarları":

                        print("kilit ekranı\n bildirim paneli")
                        anasayfayadon()

                    if bildirimayar == "bildirim rozetleri":

                        print(
                            "bildirim geldiğinde ana sayfada uygulama üzerinde göster\n rozet ayarlar\n")
                        anasayfayadon()

                    if bildirimayar == "bildirimleri yönet":
                        print(

                            "bildirimleri engelenen uygulamalar\n bildirimleri ertelemek için bildirime baılı tut\n bildirimden yanıtlama")
                        anasayfayadon()

                if başlatıcıayar == "rahatsız etme":
                    print(

                        "RAHATSIZ ETME\n rahatsız etme \n şu zamanda rahatsız etmeyine geç :\n her zaman izin verilenler:\nüst üste iki veya daha fazla aynı kişiden uyartı gelirse sesli bildir. ")
                    anasayfayadon()

                if başlatıcıayar == "varsayılan başlatıcı":

                    print(
                        "varsıyılan başlatıcı sistem \n daha fazla başlatıcı için mağazayı ziyaret et")
                    anasayfayadon()

        if kişiselleştirme == "duvar kağıdı":

            print("DUVAR KAĞIDI\n +\n hareketli duvar kağıtları\n duvar kağıtları")

            duvarkağıdıseçim = input(":")

            if duvarkağıdıseçim == "+":

                print("bir fotoğraf seçin\n \n ana sayfa\n kilit ekanı\n her ikisi")

                duvaryer = input(":")

                if duvaryer == "kilit ekranı":

                    print("uygulandı...")
                    anasayfayadon()

                if duvaryer == "ana sayfa":

                    print("uygulandı...")
                    anasayfayadon()

                if duvaryer == "her ikisi":

                    print("uygulandı...")
                    anasayfayadon()

            if duvarkağıdıseçim == "hareketli duvar kağıtları":

                print("hareketli1\nhareketli2\nhareketli3\nhareketli4\nhareketli5")
                anasayfayadon()

            if duvarkağıdıseçim == "duvar kağıtları":

                print("DUVAR KAĞITLARI \n DÜNYA \nUZAY VE GEZEGENLER\nCARTOON\nDÜZ RENK")

                walpaperx = input(":")

                if walpaperx == "DÜNYA":
                    print(

                        "duvar kağıdı1\nduvar kağıdı2\nduvar kağıdı3\nduvar kağıdı4\nduvar kağıdı5\nduvar kağıdı6\nduvar kağıdı7\nduvar kağıdı8\nduvar kağıdı9\nduvar kağıdı10\nduvar kağıdı11\nduvar kağıdı12\nduvar kağıdı13\nduvar kağıdı14\nduvar kağıdı15\nduvar kağıdı16\nduvar kağıdı17\n")

                    walp = input(":")

                    print(walp)

                    print("uygulandı")
                    anasayfayadon()

                if walpaperx == "UZAY VE GEZEGENLER":
                    print(

                        "duvar kağıdı1\nduvar kağıdı2\nduvar kağıdı3\nduvar kağıdı4\nduvar kağıdı5\nduvar kağıdı6\nduvar kağıdı7\nduvar kağıdı8\nduvar kağıdı9\nduvar kağıdı10\nduvar kağıdı11\nduvar kağıdı12\nduvar kağıdı13\nduvar kağıdı14\nduvar kağıdı15\nduvar kağıdı16\nduvar kağıdı17\nduvar kağıdı18")

                    walp = input(":")

                    print(walp)

                    print("uygulandı")
                    anasayfayadon()

                if walpaperx == "CARTOON":
                    print(

                        "duvar kağıdı1\nduvar kağıdı2\nduvar kağıdı3\nduvar kağıdı4\nduvar kağıdı5\nduvar kağıdı6\nduvar kağıdı7\nduvar kağıdı8\nduvar kağıdı9")

                    walp = input(":")

                    print(walp)

                    print("uygulandı")
                    anasayfayadon()

                if walpaperx == "DÜZ RENK":
                    print(

                        "duvar kağıdı1\nduvar kağıdı2\nduvar kağıdı3\nduvar kağıdı4\nduvar kağıdı5\nduvar kağıdı6\nduvar kağıdı7")

                    walp = input(":")

                    print(walp)

                    print("uygulandı")
                    anasayfayadon()

    def guvenlik():
        print(

            "GÜVENLİK\n parola ve biyometrik girişler\n kayıtlı şifreler\nuygulama izinleri\nkonum\n uygulama kilidi")

        güvenlikseçim = input(":")

        if güvenlikseçim == "parola ve biyometrik girişler":

            print("PAROLA VE BİYOMETRİK GİRİŞ\nparola\n parmak izi okuyucu \\yüz tanıma")

            parolaseçim = input(":")

            if parolaseçim == "parola":

                print("mevcut parola")

                defparola = "1"
                print(defparola)

                print("parola değiştir ?:")

                parolago = input(":")

                if parolago == "parola değiştir":
                    şifre_değiş()

            if parolaseçim == "parmak izi okuyucu":

                print("bu cihazda bu yöntem kullanılmıyor ancak eklenebilir")
                anasayfayadon()

            if parolaseçim == "yüz tanıma":

                print("bu cihazda bu yöntem kullanılmıyor ancak eklenebilir")
                anasayfayadon()

        elif güvenlikseçim == "kayıtlı şifreler":

            print("kayıtlı şifre bulunamadı")
            anasayfayadon()

        elif güvenlikseçim == "uygulama izinleri":
            print(

                "uygulamalara ait kullanılan izinleri aşağıda görebilirsiniz \n sistem uygulamaları şuanda izin kullanmıyor,yüklediğiniz uygulamaların izin ullanımları burada görünür.")
            anasayfayadon()

        elif güvenlikseçim == "konum":

            print("konumuzu kullanan uygulamalar aşağıda görünür.\n\n\n")
            anasayfayadon()

        else:
            anasayfayadon()

    def uygulamalar():

        print("tüm uygulamalaarı buradan yönetebilir ve depolama ile ilgili menüyü burada görebilirsiniz.")
        anasayfayadon()

    def anasayfayadon():
        def ayarlar_geri():
            print("geri dönmek için geri yazabilirsiniz")
            ayarlar()

        print(" ana sayfaya dönmek için ana sayfa yazın\n geri dönmek için geri yazınız.")

        işlem = input(":")

        if işlem == "ana sayfa":

            menudolaşım()
        elif işlem == "geri":
            ayarlar_geri()

        else:
            print("hala uygulamadasınız.")

    def ekran_süresi():

        print("EKRAN SÜRESİ \n /// \n -----------evebeyn denetimi şuan kapalı.")
        anasayfayadon()

    def senkronizasyon():

        print("hesaplarınız aşağıda listelenmiştir")

        print("---------------\n senkronizasyon açık \n senkronizesayon sıklığı 30 dk ")
        anasayfayadon()

    def ME_CLOUD():

        print("------------------------"

              "-----------             -"

              "-----------             -"

              "------------------------")
        print(

            "16 GB cloud hafızasının 7 GB ı dolu\n daha fazla depolama alanı almak için web sayfasını ziyaret edin.")

        print("\n \n")
        print(

            "cloud ile yedekleme şunun için kullanılsın:\n resimler\n videolar\n sesler\naramalar\n mesajlar\n notlar"

            "\n posta\n ses kayıtları\n uygulamalar ve verileri \n parola ve şifreler\n adresler \n cüzdan verileri\n indirilmiş diller"

            "\n dosyalar\ndiğer cihaz verileri")

        print("MEcloud size ait diğer MEos cihazlarınızdaki verileri de yedekler.")
        anasayfayadon()

    def easy_share():
        print(

            "easy share bir MEos cihazına anında veri göndermeyi ve almayı sağlayan bir servistir.\n verini büyüklüğüne göre veri iletim tipi değişebilir")
        print(

            "bir iletim veya alım başlatmak için cihazları dokundurabilir veya  yakındaki cihazları seçebilirsiniz.")
        anasayfayadon()

    print(

        "AYARLAR \n cihaz  hakkında \n bağlantılar ve paylaşım\nkişiselleştirme\n güvenlik \n uygulamalar ve depolama "

        "\n ekran süresi\n hesaplar ve senkronizasyon\n MEcloud \n easy share\n MEUP \n")

    ayar = input(":")

    if ayar == "bağlantılar ve paylaşım":

        bağlantılar()

    if ayar == "cihaz hakkında":

        cihaz_hakkında()

    elif ayar == "kişiselleştirme":

        kişiselleştirme()

    elif ayar == "güvenlik":

        guvenlik()

    elif ayar == "uygulamalar ve depolama":

        uygulamalar()

    elif ayar == "ekran süresi":

        ekran_süresi()

    elif ayar == "hesaplar ve senkronizasyon":

        senkronizasyon()

    elif ayar == "MEcloud":

        ME_CLOUD()

    elif ayar == "easy share":

        easy_share()

    elif ayar == "MEUP":

        MEUP()

    else:
        anasayfayadon()
def simge():

    import ctypes

    # .ico dosyasının yolu

    icon_path = r"C:\Users\EMİR\Desktop\dersle ve yazılımla alakalı\yazılım eğitim ve çalışmaları\çalışmalar\python çalışmaları\MEos\yardımcı olanlar\yedekleme__MEos__6_logo_geçici.ico"

    # Simgenin tanıtılması

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

    ctypes.windll.user32.SetWindowIcon(
        ctypes.windll.kernel32.GetConsoleWindow(), icon_path)
def power_menu():
    import tkinter as tk
    from tkinter import messagebox
    import os

    class PowerMenuApp (tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("Güç Menüsü")
            self.pack()
            self.create_widgets()

            # pencere kapatıldığında veya "Çıkış" düğmesine basıldığında
            # anasayfayadon fonksiyonunu çağırma
            self.master.protocol("WM_DELETE_WINDOW", self.anasayfayadon)
            self.quit_button.config(command=self.anasayfayadon)

        def create_widgets(self):
            self.kapat_button = tk.Button(
                self, text="Kapat", command=self.kapat)
            self.kapat_button.pack(side="top")

            self.yeniden_baslat_button = tk.Button(
                self, text="Yeniden Başlat", command=self.yeniden_baslat)
            self.yeniden_baslat_button.pack(side="top")

            self.sessiz_button = tk.Button(
                self, text="Sessiz", command=self.sessiz)
            self.sessiz_button.pack(side="top")

            self.acil_durum_button = tk.Button(
                self, text="Acil Durum", command=self.acil_durum)
            self.acil_durum_button.pack(side="top")

            self.ekrani_kilitle_button = tk.Button(
                self, text="Ekranı Kilitle", command=self.ekrani_kilitle)
            self.ekrani_kilitle_button.pack(side="top")

            self.quit_button = tk.Button(
                self, text="Çıkış", fg="red", command=self.anasayfayadon)
            self.quit_button.pack(side="bottom")

        def kapat(self):
            os.system("shutdown /s /t 0")

        def yeniden_baslat(self):
            os.system("shutdown /r /t 0")

        def sessiz(self):
            messagebox.showinfo("Güç Menüsü", "Sessiz mod açıldı.")
            self.anasayfayadon()

        def acil_durum(self):
            messagebox.showinfo(
                "Güç Menüsü",
                "Acil durum numarası aranıyor...")
            self.anasayfayadon()

        def ekrani_kilitle(self):
            messagebox.showinfo("Güç Menüsü", "Ekran kilidi etkinleştirildi.")
            self.kilitekranı()

        def anasayfayadon(self):
            anasayfayadon()

        def kilitekranı(self):
            kilitekranı()

    root = tk.Tk()
    app = PowerMenuApp(master=root)
    app.mainloop()

def uygulama_cikti_sil():
    # Uygulama çıktısını temizle
    print("\033[H\033[J")

def kilit_ekrani_cikti_sil():
    # Kilit ekranı çıktısını temizle
    print("\033[H\033[J")


def menudolaşım():

    from datetime import datetime

    import locale

    locale.setlocale(locale.LC_ALL, '')

    print(
        "***seçenekler****\n 1-mesajlar\n 2-aramalar\n 3-kamera \n 4- tarayıcı\n 5-game machine \n 6- galeri \n"
        " 7- uygulama mağazası \n 8- ayarlar \n 9-video player\n 10-müzik çalar \n 11-saat\n hold-hold\n 12-notlar \n 13-dosya yöneticisi \n 14- haritalar\n 15-çeviri"
        "\n 16-hesap makinesi\n 17-hava durumu\n 18-kişiler \n  19-mail \n 20-asistan \n 21-takvim\n 22-sesli notlar\n 23-pusula\n 24-homeapp\n 25-radio"
        " \n 26-dijital cüzdan\n27- görüntülü görüşme \nsağ kaydır\n sol kaydır\n tık\n hold")

    seçim = input(":")

    if seçim == "1":
        mesajlar()
    elif seçim == "2":
        kişiler_kişiler()

    elif seçim == "3":
        print(

            "kamera modları\n fotoğraf\n viddo\n portre\n 108 MP \n ağır çekim \n hızlandırılmış çekim \n gece modu "

            "\n yapay zwka desteği \n astrophotograpy \n time kapse \n makro kamera \n pro mod \n panorama   ")

        kameramod = input("seçtiğiniz mod : \n ")

        if kameramod == "fotoğraf":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "video":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "portre":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "108 MP":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "ağır çekim":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "hızladırılmış çekim":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "gece modu":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "yapay zeka desteği":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "astrophptography":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "time lapse":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "makro kamera":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "pro mod":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        elif kameramod == "panorama":

            print("\n")
            print("kaydediliyor...")

            print("\n \n \n")

            print("fotoğrafları görmek için ikona tıklayın.")
            anasayfayadon()

        else:
            anasayfayadon()

    elif seçim == "4":
        print(

            "girmek istediğiniz web sayfasını seçiniz:\n 1-facebook\n 2-instagram \n 3-twitter \n 4- başka bir site \n 5-gizli sayfa")

        web = input("web adresi veya internet araması ? :")

        if web == "1":

            print("sayfaya gidiliyor...")

            print("\n \n \n \n")
            anasayfayadon()

        if web == "2":

            print("sayfaya gidiliyor...")

            print("\n \n \n \n")
            anasayfayadon()

        if web == "3":

            print("sayfaya gidiliyor...")

            print("\n \n \n \n")
            anasayfayadon()

        if web == "4":

            print("istediğiniz web aramasını veya adresini giriniz  :")

            input("web sitesi :")

            print("sıkı tutunun ...\n webde sörf başlıyor...")

            print("...\n")
            anasayfayadon()

        if web == "5":
            print(

                "gizli sayfa etkin \n yaptığınız etkinlikler tarayıcıda saklanmaz ancak yine de tamamen görünmez olmadığınızı unutmayın \n"

                "internet servis sağlayıcınız ve kurum yöneticiniz gibi bazı kişi ve kurumlar yaptıklarınızı görebilir \n \n \n   ")

            gizlisite = input("internet araması yapmak için tıklayın.")

            print(gizlisite)

            print("sayfaya gidiliyor...")

            print(
                "gizli sayfa kapatılıyor, tüm etkinlikler siliniyor ana sayfaya dönülüyor...")
            anasayfayadon()

    elif seçim == "5":

        print("\n  hazır oyunlar \nistersen uygulama mağazasını ziyaret et ve bir kaç oyun yükle ")

        hazıroyunlar = input("hazır oyunlar oynamak ister misin?")

        if hazıroyunlar == "evet":
            oyunlar()

        anasayfayadon()

    elif seçim == "6":

        print(
            "galeri uygulaması \n tüm fotoğraflar \n kamera\\ diğer klasörler\n çöp kutusu")

        print("fotoğrafı düzenlemek için basılı tutabilirsiniz...")

        print(" fotoğraf yönetme seçenekleri \n sil\n yedekle \n düzenle")

        galeribasili = input(":")

        if galeribasili == "sil":
            print("silindi...")
            anasayfayadon()

        elif galeribasili == "yedekle":
            print("yedeklendi...")
            anasayfayadon()

        elif galeribasili == "düzenle":

            print("fotoğrafın yeni hali kaydedildi...")
            anasayfayadon()

        else:
            anasayfayadon()

    elif seçim == "7":
        print(

            "*** kategoriler*** \n *sosyal ağ uygulamaları \n *oyunlar \n *eğlencelikler \n * kişiselleşitirmeler \n * sizin için önerilenler \n ara")

        print("seçtiğiniz uygulama indiriliyor")

        print("...\n ...\n ...\n ...")

        print("uygulama yüklendi.")
        anasayfayadon()

    elif seçim == "8":
        ayarlar()

    elif seçim == "9":
        print(

            "henüz inidrdiğiniz veya çektiğiniz video yok \n video kaydettiğinizde veya indirdiğinizde burada görünür.")
        anasayfayadon()

    elif seçim == "10":
        print(

            "henüz indirdiğiniz müzik yok \n  indirdiiğiniz müzükler burada görünür.")
        anasayfayadon()

    elif seçim == "11":

        print("SAAT\nalarm\n kronometre\n sayaç")

        an = datetime.now()

        print(datetime.ctime(an))

        saatseçim = input(":")

        if saatseçim == "alarm":

            print("alarmlar burada görünür\n buradan yeni alarm ekleyebilirsiniz")

            print("alarmlar----\n alarm oluşturmak için tıklayın.")
            print("alarm kaydedildi")
            anasayfayadon()

        elif saatseçim == "kronometre":
            kronometre()

        elif saatseçim == "sayaç":

            print("10 dakikalık sayaç \n 30 dakikalık sayaç\n 60 dklık sayaç")

            sayaçseçim = input(":")

            if sayaçseçim == "10":

                sayac10()
                anasayfayadon()

            if sayaçseçim == "30":

                sayac30()
                anasayfayadon()

            if sayaçseçim == "60":

                sayac60()
                anasayfayadon()

    elif seçim == "12":
        notlar()

    elif seçim == "13":

        dosya_yöneticisi()

    elif seçim == "14":

        haritalar()

    elif seçim == "15":

        çeviri()

    elif seçim == "16":

        hesap_makinesi()
        anasayfayadon()

    elif seçim == "17":

        hava_durumu()

    elif seçim == "18":

        kişiler()

    elif seçim == "19":
        mail()

    elif seçim == "20":
        asistan()

    elif seçim == "21":
        TakvimUygulamasi()

    elif seçim == "22":

        sesli_notlar()

    elif seçim == "23":
        pusula()

    elif seçim == "24":

        homeapp()

    elif seçim == "25":
        radio()

    elif seçim == "26":

        vallet()

    elif seçim == "27":

        görüntülü()

    elif seçim == "hold":

        power_menu()

    elif seçim == "tık":
        kilitekranı()

    elif seçim == "sağ kaydır":

        eylemmerkezi()
        anasayfayadon()

    elif seçim == "sol kaydır":

        bildirim_merkezi()
        anasayfayadon()

    else:
        anasayfayadon()
import tkinter as tk

def anasayfayadon():
    def button_clicked():
        uygulama_cikti_sil()
        menudolaşım()

    # Ana pencereyi oluşturma
    root = tk.Tk()

    # Ana sayfa etiketini oluşturma
    label = tk.Label(root, text="Ana sayfaya dönmek için 'Ana Sayfa' yazın")
    label.pack()

    # İşlem giriş kutusunu oluşturma
    entry = tk.Entry(root)
    entry.pack()

    # Butonu oluşturma
    button = tk.Button(root, text="Gönder", command=button_clicked)
    button.pack()

    # Pencereyi gösterme döngüsünü başlatma
    root.mainloop()


    def anasayfaya_don(self):
        self.pencere.destroy ()
        anasayfayadon()










def giris_yapin():
    # Veritabanı bağlantısı oluşturun
    conn = sqlite3.connect(
        r"C:\Users\EMİR\Desktop\dersle ve yazılımla alakalı\yazılım eğitim ve çalışmaları\çalışmalar\python çalışmaları\MEos\dist\YOUos1.2\bu_bir_dt_denemesidir_6.db")

    # Bir imleç oluşturun
    cursor = conn.cursor()

    # "cihazbir" adlı kaydın şifresini sorgulayın
    password = input("Lütfen şifrenizi girin: ")
    cursor.execute("SELECT password FROM tablo WHERE id = 'cihazbir'")
    db_password = cursor.fetchone()[0]
    # Veritabanı bağlantısını kapatın
    conn.close()
    if password == db_password:
        # Şifre doğruysa, menüyü dolaşım() fonksiyonunu çağırın
        print("Giriş başarılı!")
        menudolaşım()

    else:
        # Şifre yanlışsa, tekrar deneyin
        print("Şifre yanlış. Lütfen tekrar deneyin.")


def kilitekranı():
    from datetime import datetime

    şimdi = datetime.now()

    print(datetime.ctime(şimdi))

    print(" yeni bildirim yok.")

    print("kilit açmak için şifreyi veya biyometrik verileri kullanın")
    giris_yapin()


def kronometre():

    baslangic = None

    ara_zamanlar = []

    durmus_mu = False

    while True:

        try:

            print("Kronometreyi başlatmak için 'başla' yazın.")

            print("Ara zaman kaydetmek için 'ara' yazın.")

            print("Kronometreyi durdurmak için 'dur' yazın.")

            secim = input("Seçiminiz: ")

            if secim == "başla":

                if not baslangic:

                    baslangic = time.time()

                    print("Kronometre başladı!")

                elif durmus_mu:

                    baslangic += time.time() - durmus_mu

                    durmus_mu = False

                    print("Kronometre tekrar başlatıldı!")

                else:

                    print("Kronometre zaten başladı!")

            elif secim == "ara":

                if not baslangic:

                    print("Kronometre henüz başlamadı!")

                else:

                    ara_zamanlar.append(time.time() - baslangic)

                    print("Ara zaman kaydedildi!")

            elif secim == "dur":

                if not baslangic:

                    print("Kronometre henüz başlamadı!")

                elif durmus_mu:

                    print("Kronometre zaten durmuş!")

                else:

                    durmus_mu = time.time()

                    print("Kronometre durdu!")

            else:

                print("Geçersiz seçim!")

        except KeyboardInterrupt:

            print("\nKronometre durduruldu!")

            break

    if baslangic:

        gecen_sure = time.time() - baslangic

        print(
            "Geçen süre: {:.2f} dakika {:.2f} saniye {:.2f} salise".format(
                gecen_sure //
                60,
                gecen_sure %
                60,
                (gecen_sure %
                 1) *
                100))

    if ara_zamanlar:

        print("Ara zamanlar:")

        for i, zaman in enumerate(ara_zamanlar, start=1):

            print("{} - {:.2f} dakika {:.2f} saniye {:.2f} salise".format(i,
                  zaman // 60, zaman % 60, (zaman % 1) * 100))
            anasayfayadon()


def sayac10():

    baslangic = time.time()

    while True:

        try:
            simdi = time.time()

            gecen_zaman = simdi - baslangic

            kalan_zaman = 600 - gecen_zaman

            if kalan_zaman < 0:

                print("Sayaç tamamlandı!")

                break

            print(
                "Kalan süre: {:.0f} dakika {:.0f} saniye".format(
                    kalan_zaman //
                    60,
                    kalan_zaman %
                    60))

            time.sleep(1)

        except KeyboardInterrupt:

            print("\nSayaç durduruldu!")

            break
            anasayfayadon()


def sayac30():

    baslangic = time.time()

    while True:

        try:
            simdi = time.time()

            gecen_zaman = simdi - baslangic

            kalan_zaman = 1800 - gecen_zaman

            if kalan_zaman < 0:

                print("Sayaç tamamlandı!")

                break

            print(
                "Kalan süre: {:.0f} dakika {:.0f} saniye".format(
                    kalan_zaman //
                    60,
                    kalan_zaman %
                    60))

            time.sleep(1)

        except KeyboardInterrupt:

            print("\nSayaç durduruldu!")

            break
            anasayfayadon()


def sayac60():

    baslangic = time.time()

    while True:

        try:
            simdi = time.time()

            gecen_zaman = simdi - baslangic

            kalan_zaman = 3600 - gecen_zaman

            if kalan_zaman < 0:

                print("Sayaç tamamlandı!")

                break

            print(
                "Kalan süre: {:.0f} dakika {:.0f} saniye".format(
                    kalan_zaman //
                    60,
                    kalan_zaman %
                    60))

            time.sleep(1)

        except KeyboardInterrupt:

            print("\nSayaç durduruldu!")

            break
            anasayfayadon()


def eylemmerkezi():

    print(
        "wifi                       bluethooth                   ses modu \n"
        "gece modu                  konum                        kişisel erişim noktası \n"
        "mobil veri                 güç tasarrufu modu           uçak modu \n"
        "ekran yansıtma             fener                        rahatsız etmeyin\n"
        "yakındakilerle paylaş      senkronizasyon               wifi araması \n "
        "mavi ışık filtresi\n"
        "parlaklık \n---------------*_____ \n ses\n--------*___________ \n"
        "kestirme ekle ")
    anasayfayadon()


def haritalar():
    # Haritanın başlangıç koordinatlarını ayarlayın
    map_center = [41.015137, 28.979530]

    # Haritayı oluşturun
    m = folium.Map(location=map_center, zoom_start=12)

    # Mini harita ekle
    minimap = MiniMap()
    m.add_child(minimap)

    # Arama kutusu ekle
    search = MiniMap(
        position="topleft",
        zoom_level_offset=-6,
        width=300,
        height=300,
        tile_layer='OpenStreetMap',
        toggle_display=True
    )
    m.add_child(search)

    # Haritaya bir işaretçi ekleyin
    marker = folium.Marker(location=map_center, popup="İstanbul")
    marker.add_to(m)

    # Haritayı kaydedin
    m.save("map.html")

    # Haritayı varsayılan web tarayıcınızda açın
    webbrowser.open("map.html")

    # Tarayıcı kapatıldığında anasayfayadon() fonksiyonunu çağırın
    anasayfayadon()


def bildirim_merkezi():
    from datetime import datetime

    şimdi = datetime.now()

    print(datetime.ctime(şimdi))

    print(" yeni bildirim yok.")
    anasayfayadon()


def dosya_yöneticisi():
    import os
    import shutil
    import tkinter as tk
    from tkinter import filedialog

    class FileExplorerApp (tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("Dosya Yöneticisi")
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.list_files_button = tk.Button(
                self, text="Dosyaları Listele", command=self.list_files)
            self.list_files_button.pack(side="top")

            self.create_file_button = tk.Button(
                self, text="Dosya Oluştur", command=self.create_file)
            self.create_file_button.pack(side="top")

            self.delete_file_button = tk.Button(
                self, text="Dosya Sil", command=self.delete_file)
            self.delete_file_button.pack(side="top")

            self.copy_file_button = tk.Button(
                self, text="Dosya Kopyala", command=self.copy_file)
            self.copy_file_button.pack(side="top")

            self.move_file_button = tk.Button(
                self, text="Dosya Taşı", command=self.move_file)
            self.move_file_button.pack(side="top")

            self.read_file_button = tk.Button(
                self, text="Dosya Oku", command=self.read_file)
            self.read_file_button.pack(side="top")

            self.write_file_button = tk.Button(
                self, text="Dosyaya Yaz", command=self.write_file)
            self.write_file_button.pack(side="top")

            self.quit_button = tk.Button(
                self, text="Çıkış", fg="red", command=self.master.destroy)
            self.quit_button.pack(side="bottom")

        def list_files(self):
            path = filedialog.askdirectory()
            if path:
                print(f"{path} klasöründeki dosyalar:")
                for file in os.listdir(path):
                    print(file)

        def create_file(self):
            filename = filedialog.asksaveasfilename()
            if filename:
                with open(filename, "w"):
                    pass
                print(f"{filename} dosyası oluşturuldu.")

        def delete_file(self):
            filename = filedialog.askopenfilename()
            if filename:
                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"{filename} dosyası silindi.")
                else:
                    print(f"{filename} dosyası mevcut değil.")

        def copy_file(self):
            src = filedialog.askopenfilename()
            dst = filedialog.asksaveasfilename()
            if src and dst:
                shutil.copy(src, dst)
                print(f"{src} dosyası {dst} konumuna kopyalandı.")

        def move_file(self):
            src = filedialog.askopenfilename()
            dst = filedialog.asksaveasfilename()
            if src and dst:
                shutil.move(src, dst)
                print(f"{src} dosyası {dst} konumuna taşındı.")

        def read_file(self):
            filename = filedialog.askopenfilename()
            if filename:
                with open(filename, "r") as file:
                    content = file.read()
                print(f"{filename} dosyasının içeriği:")
                print(content)

        def write_file(self):
            filename = filedialog.askopenfilename()
            if filename:
                content = input("İçeriği girin: ")
                with open(filename, "w") as file:
                    file.write(content)
                print(f"{filename} dosyasına yazıldı.")

        def ana_sayfaya_don(self):
            self.master.destroy()
            anasayfayadon()

    root = tk.Tk()
    app = FileExplorerApp(master=root)
    app.mainloop()


def çeviri():
    import tkinter as tk
    from googletrans import LANGUAGES, Translator

    class TranslationApp:
        def __init__(self, master):
            self.master = master
            master.title("Çeviri")

            # Kaynak dil, hedef dil ve metin kutularını oluşturun
            self.src_lang_label = tk.Label(master, text="Kaynak Dil:")
            self.src_lang_label.grid(row=0, column=0, padx=5, pady=5)
            self.src_lang_var = tk.StringVar()
            self.src_lang_dropdown = tk.OptionMenu(
                master, self.src_lang_var, *LANGUAGES.keys())
            self.src_lang_dropdown.grid(row=0, column=1, padx=5, pady=5)

            self.dest_lang_label = tk.Label(master, text="Hedef Dil:")
            self.dest_lang_label.grid(row=1, column=0, padx=5, pady=5)
            self.dest_lang_var = tk.StringVar()
            self.dest_lang_dropdown = tk.OptionMenu(
                master, self.dest_lang_var, *LANGUAGES.keys())
            self.dest_lang_dropdown.grid(row=1, column=1, padx=5, pady=5)

            self.text_label = tk.Label(master, text="Metin:")
            self.text_label.grid(row=2, column=0, padx=5, pady=5)
            self.text_entry = tk.Entry(master)
            self.text_entry.grid(row=2, column=1, padx=5, pady=5)

            # Çevir düğmesini oluşturun
            self.translate_button = tk.Button(
                master, text="Çevir", command=self.translate_text)
            self.translate_button.grid(row=3, column=1, padx=5, pady=5)

            # Çeviri sonuçlarını göstermek için bir metin kutusu oluşturun
            self.result_textbox = tk.Text(master, height=10, width=50)
            self.result_textbox.grid(
                row=4, column=0, columnspan=2, padx=10, pady=10)

            # Pencere kapatıldığında anasayfayadon() fonksiyonunu çağırmak için
            # etkinleştirici ekle
            master.protocol("WM_DELETE_WINDOW", self.on_closing)

        def translate_text(self):
            # Kaynak ve hedef dilleri ve metin kutusu içeriğini alın
            src_lang = self.src_lang_var.get()
            dest_lang = self.dest_lang_var.get()
            text = self.text_entry.get()

            # Metni çevirin
            translator = Translator()
            result = translator.translate(text, src=src_lang, dest=dest_lang)

            # Çeviri sonuçlarını metin kutusuna yazın
            self.result_textbox.delete("1.0", tk.END)
            self.result_textbox.insert(
                tk.END,
                f"{result.origin} ({LANGUAGES[result.src]}) -> {result.text} ({LANGUAGES[result.dest]})")

        def on_closing(self):
            self.master.destroy()
    root = tk.Tk()
    translation_app = TranslationApp(root)
    root.mainloop()


def hesap_makinesi():
    import tkinter as tk

    class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Hesap Makinesi")

            # Ekranı oluşturun
            self.display = tk.Entry(master, width=30, font=("Helvetica", 18))
            self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

            # Butonları oluşturun
            buttons = [
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", ".", "C", "+"
            ]

            # Butonları yerleştirin
            row = 1
            col = 0
            for button_text in buttons:
                tk.Button(
                    master,
                    text=button_text,
                    width=7,
                    height=3,
                    command=lambda text=button_text: self.add_to_display(text)).grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5)
                col += 1
                if col > 3:
                    col = 0
                    row += 1

            # Eşittir butonunu ekle
            tk.Button(
                master,
                text="=",
                width=7,
                height=3,
                command=self.calculate).grid(
                row=5,
                column=2,
                padx=5,
                pady=5)

            # Pencere kapatıldığında anasayfayadon() fonksiyonunu çağırın
            master.protocol("WM_DELETE_WINDOW", self.on_closing)

        def add_to_display(self, text):
            self.display.insert(tk.END, text)

        def calculate(self):
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)

        def on_closing(self):
            # Pencere kapatıldığında anasayfayadon() fonksiyonunu çağırın
            self.master.destroy()
            anasayfayadon()

    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


def hava_durumu():

    import requests

    from bs4 import BeautifulSoup

    def get_weather_data(city):

        url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"

        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')

            weather_data = soup.find_all(
                class_='b-forecast__table-description-content')[0].get_text().strip()

            return weather_data

        else:

            return None


def kişiler():
    import tkinter as tk

    class PersonList:
        def __init__(self, master):
            self.master = master
            master.title("Kişiler")

            # Kişiler listesini oluşturun
            self.persons = []

            # Kişileri göstermek için bir metin kutusu oluşturun
            self.textbox = tk.Text(master, height=10, width=50)
            self.textbox.grid(row=0, column=0, padx=10, pady=10)

            # Kişi ekleme düğmesi oluşturun
            self.add_button = tk.Button(
                master, text="+", command=self.add_person)
            self.add_button.grid(row=1, column=0, padx=10, pady=10)

            # Pencere kapatıldığında anasayfayadon() fonksiyonunu çağırmak için
            # etkinleştirici ekle
            master.protocol("WM_DELETE_WINDOW", self.on_closing)

        def add_person(self):
            # Yeni bir kişi eklemek için bir alt pencere oluşturun
            person_window = tk.Toplevel(self.master)
            person_window.title("Yeni Kişi Ekle")

            # Kişi bilgileri için girdi kutularını oluşturun
            name_label = tk.Label(person_window, text="İsim:")
            name_label.grid(row=0, column=0, padx=5, pady=5)
            name_entry = tk.Entry(person_window)
            name_entry.grid(row=0, column=1, padx=5, pady=5)

            surname_label = tk.Label(person_window, text="Soyisim:")
            surname_label.grid(row=1, column=0, padx=5, pady=5)
            surname_entry = tk.Entry(person_window)
            surname_entry.grid(row=1, column=1, padx=5, pady=5)

            phone_label = tk.Label(person_window, text="Telefon:")
            phone_label.grid(row=2, column=0, padx=5, pady=5)
            phone_entry = tk.Entry(person_window)
            phone_entry.grid(row=2, column=1, padx=5, pady=5)

            # Kaydet düğmesini oluşturun
            save_button = tk.Button(
                person_window,
                text="Kaydet",
                command=lambda: self.save_person(
                    name_entry.get(),
                    surname_entry.get(),
                    phone_entry.get()))
            save_button.grid(row=3, column=1, padx=5, pady=5)

        def save_person(self, name, surname, phone):
            # Yeni bir kişi oluşturun ve kişiler listesine ekleyin
            person = {"name": name, "surname": surname, "phone": phone}
            self.persons.append(person)

            # Kişileri göstermek için metin kutusunu güncelleyin
            self.update_textbox()

        def update_textbox(self):
            # Kişileri göstermek için metin kutusunu güncelleyin
            self.textbox.delete("1.0", tk.END)
            if self.persons:
                for person in self.persons:
                    self.textbox.insert(
                        tk.END, f"{person['name']} {person['surname']}: {person['phone']}\n")
            else:
                self.textbox.insert(tk.END, "Kayıtlı kişi yok.")

        def on_closing(self):
            # Pencere kapatıldığında anasayfayadon() fonksiyonunu çağırın
            self.master.destroy()
            anasayfayadon()

    root = tk.Tk()
    person_list = PersonList(root)
    root.mainloop()


def mail():

    import smtplib

    from email.mime.text import MIMEText

    from email.mime.multipart import MIMEMultipart

    import imaplib

    import getpass

    def read_emails():

        email = input("E-posta adresi: ")

        password = getpass.getpass("Şifre: ")

        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        mail.login(email, password)

        mail.select('inbox')

        status, data = mail.search(None, 'ALL')

        mail_ids = data[0]

        id_list = mail_ids.split()

        first_email_id = int(id_list[0])

        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):

            typ, data = mail.fetch(str(i), '(RFC822)')

            for response in data:

                if isinstance(response, tuple):

                    msg = email.message_from_bytes(response[1])

                    print('From: ' + msg['From'])

                    print('Subject: ' + msg['subject'])

                    print('Date: ' + msg['date'])

    def send_email():

        email = input("E-posta adresi: ")

        password = getpass.getpass("Şifre: ")

        to = input("Alıcı E-posta adresi: ")

        subject = input("E-posta konusu: ")

        body = input("E-posta içeriği: ")

        msg = MIMEMultipart()

        msg['From'] = email

        msg['To'] = to

        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(email, password)

        text = msg.as_string()

        server.sendmail(email, to, text)

        server.quit()

    while True:

        print("1 - Gelen Kutusunu Kontrol Et")

        print("2 - E-posta Gönder")

        print("3 - Çıkış")

        choice = int(input("Seçiminiz: "))

        if choice == 1:

            read_emails()

        elif choice == 2:

            send_email()

        elif choice == 3:

            break

        else:

            print("Geçersiz seçim.")


def asistan():
    def anasayfayadon():
        print("Ana sayfaya dönmek için ana sayfa yazın.")
        işlem = input(":")
        if işlem == "ana sayfa":
            menudolaşım()
        else:
            print("Hala uygulamadasınız.")

    search = input("Ne aramak istiyorsunuz?: ")
    if search == "anasayfaya dön":
        anasayfayadon()
    else:
        url = f"https://www.google.com/search?q={search}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        search_results = soup.find_all('div', {'class': 'g'})
        for result in search_results:
            title = result.find('h3').get_text()
            print(title)
            description = result.find('span', {'class': 'aCOpRe'}).get_text()
            print(description)
            print()


def takvim():

    import calendar
    from datetime import datetime

    # Şu anki yıl ve ay bilgisini alma

    suanki_zaman = datetime.now()

    yil = suanki_zaman.year

    ay = suanki_zaman.month

    # Kullanıcıdan yıl ve ay bilgisini alma

    yil = int(input("Yılı girin (varsayılan: {}): ".format(yil))) or yil

    ay = int(input("Ayı girin (varsayılan: {}): ".format(ay))) or ay

    # Takvim çıktısını alma

    takvim = calendar.month(yil, ay)

    print(takvim)
    anasayfayadon()


def sesli_notlar():
    import pyaudio

    import wave

    # Kayıt ayarları

    FORMAT = pyaudio.paInt16

    CHANNELS = 1

    RATE = 44100

    CHUNK = 1024

    RECORD_SECONDS = 5

    # PyAudio nesnesi oluşturma

    p = pyaudio.PyAudio()

    # Ses kayıt cihazının başlatılması

    stream = p.open(format=FORMAT,

                    channels=CHANNELS,

                    rate=RATE,

                    input=True,

                    frames_per_buffer=CHUNK)

    print("Kaydediliyor...")

    # Ses verilerinin kaydedilmesi

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

        data = stream.read(CHUNK)
        frames.append(data)

    print("Kayıt tamamlandı.")

    # Kaydedilen sesin kaydedilmesi

    wf = wave.open("kaydedilen_ses.wav", "wb")

    wf.setnchannels(CHANNELS)

    wf.setsampwidth(p.get_sample_size(FORMAT))

    wf.setframerate(RATE)

    wf.writeframes(b"".join(frames))

    wf.close()

    # PyAudio nesnesi ve kayıt cihazının kapatılması

    stream.stop_stream()

    stream.close()
    p.terminate()

    # Kaydedilen sesin çalınması

    wf = wave.open("kaydedilen_ses.wav", "rb")

    player = pyaudio.PyAudio()

    # Ses çalma cihazının başlatılması

    stream = player.open(
        format=player.get_format_from_width(
            wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)

    print("Kaydedilen ses çalınıyor...")

    # Kaydedilen sesin çalınması

    data = wf.readframes(CHUNK)

    while data:

        stream.write(data)

        data = wf.readframes(CHUNK)

    print("Kaydedilen sesin çalınması tamamlandı.")

    # PyAudio nesnesi ve çalma cihazının kapatılması

    stream.stop_stream()

    stream.close()

    wf.close()
    player.terminate()
    anasayfayadon()


def pusula():

    import pygame

    import math

    # Pencere boyutları

    WIDTH = 600

    HEIGHT = 600

    # Pencere renkleri

    BG_COLOR = (255, 255, 255)

    LINE_COLOR = (0, 0, 0)

    # Pusula ayarları

    CENTER = (WIDTH // 2, HEIGHT // 2)

    RADIUS = WIDTH // 3

    LINE_WIDTH = 2

    # Pusulanın çizimi

    def draw_compass(screen, angle):

        # Dairenin çizimi

        pygame.draw.circle(screen, LINE_COLOR, CENTER, RADIUS, LINE_WIDTH)

        # Yön çizgilerinin çizimi

        for i in range(0, 360, 45):

            x = int(CENTER[0] + math.cos(math.radians(i - angle)) * RADIUS)

            y = int(CENTER[1] - math.sin(math.radians(i - angle)) * RADIUS)

            pygame.draw.line(screen, LINE_COLOR, CENTER, (x, y), LINE_WIDTH)

    # Pencere ve ekran oluşturulması

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Pusula")

    clock = pygame.time.Clock()

    # Pusulanın açısı

    angle = 0

    # Oyun döngüsü

    running = True

    while running:

        # Olay işleme

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

        # Ekran temizleme

        screen.fill(BG_COLOR)

        # Pusulanın çizimi

        draw_compass(screen, angle)

        # Pusulanın açısını güncelleme

        angle = (angle + 1) % 360

        # Ekran güncelleme

        pygame.display.flip()

        # Oyun saatini güncelleme

        clock.tick(60)

    # Pygame nesnesi ve pencereyi kapatma

    pygame.quit()


class Snake:
    pass


def oyunlar():

    def pong_oyunu():

        import pygame
        import random

        # Oyun alanı boyutları

        WIDTH = 600

        HEIGHT = 400

        # Renk tanımları

        WHITE = (255, 255, 255)

        BLACK = (0, 0, 0)

        # Pencereyi aç

        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Pong")

        # Raketi oluştur

        class Paddle (pygame.sprite.Sprite):

            def __init__(self, x, y):

                super().__init__()

                self.image = pygame.Surface([10, 75])

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = x

                self.rect.y = y

            def move_up(self, pixels):

                self.rect.y -= pixels

                if self.rect.y < 0:

                    self.rect.y = 0

            def move_down(self, pixels):

                self.rect.y += pixels

                if self.rect.y > HEIGHT - 75:

                    self.rect.y = HEIGHT - 75

        # Topu oluştur

        class Ball (pygame.sprite.Sprite):

            def __init__(self):

                super().__init__()

                self.image = pygame.Surface([10, 10])

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = WIDTH / 2

                self.rect.y = HEIGHT / 2

                self.speed_x = 5

                self.speed_y = random.choice([-5, 5])

            def update(self):

                self.rect.x += self.speed_x

                self.rect.y += self.speed_y

                if self.rect.y < 0 or self.rect.y > HEIGHT - 10:

                    self.speed_y = -self.speed_y

                if pygame.sprite.collide_rect(
                        ball,
                        paddle1) or pygame.sprite.collide_rect(
                        ball,
                        paddle2):

                    self.speed_x = -self.speed_x

        # Raketi ve topu oluştur

        paddle1 = Paddle(50, HEIGHT / 2 - 37)

        paddle2 = Paddle(WIDTH - 60, HEIGHT / 2 - 37)

        ball = Ball()

        # Tüm sprite'ları bir grup içine koy

        all_sprites = pygame.sprite.Group()

        all_sprites.add(paddle1)

        all_sprites.add(paddle2)

        all_sprites.add(ball)

        # Oyun döngüsü

        clock = pygame.time.Clock()

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    running = False

            # Oyuncu 1 için hareket kontrolü

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:

                paddle1.move_up(5)

            if keys[pygame.K_s]:

                paddle1.move_down(5)

            # Oyuncu 2 için hareket kontrolü

            if keys[pygame.K_UP]:

                paddle2.move_up(5)

            if keys[pygame.K_DOWN]:

                paddle2.move_down(5)

                # Topun hareketi ve güncellenmesi

                all_sprites.update()

                # Topun kenarlara çarpınca geri dönmesi

                if ball.rect.x < -10 or ball.rect.x > WIDTH + 10:

                    ball.rect.x = WIDTH / 2

                    ball.rect.y = HEIGHT / 2

                    ball.speed_x = 5

                    ball.speed_y = random.choice([-5, 5])

                # Ekrana çizim işlemi

                screen.fill(BLACK)

                pygame.draw.line(
                    screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 5)

                all_sprites.draw(screen)

                pygame.display.flip()

                # Oyun hızı

                clock.tick(60)

            # Pencereyi kapat

            pygame.quit()

    def yılan_oyunu(Snake=None):

        import pygame
        import random

        # Oyun alanı boyutları

        WIDTH = 600

        HEIGHT = 400

        # Renk tanımları

        WHITE = (255, 255, 255)

        BLACK = (0, 0, 0)

        RED = (255, 0, 0)

        # Pencereyi aç

        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Yılan Oyunu")

        # Yılanı oluştur

        class Snake (pygame.sprite.Sprite):
            pass

            def __init__(self, x, y):

                super().__init__()

                self.image = pygame.Surface([10, 10])

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = x

                self.rect.y = y

                self.direction = "right"

                self.speed = 10

                self.body = []

                self.length = 1

            def move(self):

                if self.direction == "right":

                    self.rect.x += self.speed

                elif self.direction == "left":

                    self.rect.x -= self.speed

                elif self.direction == "up":

                    self.rect.y -= self.speed

                elif self.direction == "down":

                    self.rect.y += self.speed

            def grow(self):

                self.length += 1

                self.body.append((self.rect.x, self.rect.y))

            def update(self):

                if self.length > 1:

                    self.body.insert(0, (self.rect.x, self.rect.y))

                    self.body = self.body[:self.length - 1]

                self.move()

            def check_collision(self):

                if self.rect.x < 0 or self.rect.x > WIDTH - \
                        10 or self.rect.y < 0 or self.rect.y > HEIGHT - 10:

                    return True

                for segment in self.body:

                    if self.rect.x == segment[0] and self.rect.y == segment[1]:

                        return True

                return False

            # Elmaları oluştur

            class Apple (pygame.sprite.Sprite):

                def __init__(self):

                    super().__init__()

                    self.image = pygame.Surface([10, 10])

                    self.image.fill(RED)

                    self.rect = self.image.get_rect()

                    self.rect.x = random.randint(0, WIDTH - 10)

                    self.rect.y = random.randint(0, HEIGHT - 10)

                def update(self):
                    pass

                def reset(self):

                    self.rect.x = random.randint(0, WIDTH - 10)

                    self.rect.y = random.randint(0, HEIGHT - 10)

            # Oyun döngüsü

            snake = Snake(WIDTH / 2, HEIGHT / 2)

            apple = Apple()

            all_sprites = pygame.sprite.Group()

            all_sprites.add(snake, apple)

            clock = pygame.time.Clock()

            while True:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:

                        pygame.quit()

                        quit()

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RIGHT and snake.direction != "left":

                            snake.direction = "right"

                        elif event.key == pygame.K_LEFT and snake.direction != "right":

                            snake.direction = "left"

                        elif event.key == pygame.K_UP and snake.direction != "down":

                            snake.direction = "up"

                        elif event.key == pygame.K_DOWN and snake.direction != "up":

                            snake.direction = "down"

                # Yılanın büyümesi

                if snake.rect.colliderect(apple.rect):
                    apple.reset()

                    snake.grow()

                # Yılanın çarpışması

                if snake.check_collision():

                    pygame.quit()

                    quit()

                # Ekrana çizim işlemi

                screen.fill(BLACK)

                all_sprites.update()

                all_sprites.draw(screen)

                pygame.display.flip()

                # Oyun hızı

                clock.tick(15)

            # Pencereyi kapat

            pygame.quit()

    def space_invaders():

        # Gerekli kütüphaneler

        import pygame
        import random

        # Oyun sabitleri

        WIDTH = 600

        HEIGHT = 800

        FPS = 60

        # Renkler

        BLACK = (0, 0, 0)

        WHITE = (255, 255, 255)

        RED = (255, 0, 0)

        # Pencereyi başlat

        pygame.init()

        pygame.mixer.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Space Invaders")

        clock = pygame.time.Clock()

        # Oyuncu gemisi

        class Player (pygame.sprite.Sprite):

            def __init__(self):

                super().__init__()

                self.image = pygame.Surface([30, 30])

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = WIDTH / 2

                self.rect.y = HEIGHT - 50

                self.speed_x = 0

            def update(self):

                self.rect.x += self.speed_x

                if self.rect.left < 0:

                    self.rect.left = 0

                elif self.rect.right > WIDTH:

                    self.rect.right = WIDTH

            def shoot(self):

                bullet = Bullet(self.rect.centerx, self.rect.top)

                all_sprites.add(bullet)

                bullets.add(bullet)

        # Düşman uzaylıları

        class Enemy (pygame.sprite.Sprite):

            def __init__(self):

                super().__init__()

                self.image = pygame.Surface([30, 30])

                self.image.fill(RED)

                self.rect = self.image.get_rect()

                self.rect.x = random.randint(0, WIDTH - 30)

                self.rect.y = random.randint(-100, -40)

                self.speed_y = random.randint(1, 5)

            def update(self):

                self.rect.y += self.speed_y

                if self.rect.top > HEIGHT:

                    self.rect.x = random.randint(0, WIDTH - 30)

                    self.rect.y = random.randint(-100, -40)

                    self.speed_y = random.randint(1, 5)

        # Mermiler

        class Bullet (pygame.sprite.Sprite):

            def __init__(self, x, y):

                super().__init__()

                self.image = pygame.Surface([5, 10])

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.centerx = x

                self.rect.bottom = y

                self.speed_y = -10

            def update(self):

                self.rect.y += self.speed_y

                if self.rect.bottom < 0:
                    self.kill()

        # Oyun döngüsü

        player = Player()

        all_sprites = pygame.sprite.Group()

        enemies = pygame.sprite.Group()

        bullets = pygame.sprite.Group()

        all_sprites.add(player)

        for i in range(10):

            enemy = Enemy()

            all_sprites.add(enemy)
            enemies.add(enemy)

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:

                        player.speed_x = -5

                    elif event.key == pygame.K_RIGHT:

                        player.speed_x = 5

                    if event.key == pygame.K_SPACE:

                        player.shoot()

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT and player.speed_x < 0:

                        player.speed_x = 0

                    elif event.key == pygame.K_RIGHT and player:

                        # Oyun döngüsü

                        player = Player()

                        all_sprites = pygame.sprite.Group()

                        enemies = pygame.sprite.Group()

                        bullets = pygame.sprite.Group()

                        all_sprites.add(player)

                        for i in range(10):

                            enemy = Enemy()

                            all_sprites.add(enemy)
                            enemies.add(enemy)

                        while True:

                            for event in pygame.event.get():

                                if event.type == pygame.QUIT:

                                    pygame.quit()

                                    quit()

                                if event.type == pygame.KEYDOWN:

                                    if event.key == pygame.K_LEFT:

                                        player.speed_x = -5

                                    elif event.key == pygame.K_RIGHT:

                                        player.speed_x = 5

                                    if event.key == pygame.K_SPACE:

                                        player.shoot()

                                if event.type == pygame.KEYUP:

                                    if event.key == pygame.K_LEFT and player.speed_x < 0:

                                        player.speed_x = 0

                                    elif event.key == pygame.K_RIGHT and player.speed_x > 0:

                                        player.speed_x = 0

                            all_sprites.update()

                            hits = pygame.sprite.groupcollide(
                                enemies, bullets, True, True)

                            for hit in hits:

                                enemy = Enemy()

                                all_sprites.add(enemy)
                                enemies.add(enemy)

                            hits = pygame.sprite.spritecollide(
                                player, enemies, False)

                            if hits:

                                pygame.quit()

                                quit()

                            screen.fill(BLACK)

                            all_sprites.draw(screen)

                            pygame.display.flip()

                            clock.tick(FPS)

                        pygame.quit()

                        quit()

    def ball():

        import pygame
        import random

        # Ekran boyutu

        SCREEN_WIDTH = 400

        SCREEN_HEIGHT = 400

        # Renkler

        BLACK = (0, 0, 0)

        WHITE = (255, 255, 255)

        # Pygame modülünü başlat

        pygame.init()

        # Ekranı oluştur

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption("Basit Top Oyunu")

        # Saat objesi

        clock = pygame.time.Clock()

        # Top objesi

        class Ball (pygame.sprite.Sprite):

            def __init__(self):

                super().__init__()

                self.image = pygame.Surface((20, 20))

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

                self.rect.y = random.randint(
                    0, SCREEN_HEIGHT - self.rect.height)

                self.speed_x = 5

                self.speed_y = 5

            def update(self):

                self.rect.x += self.speed_x

                self.rect.y += self.speed_y

                # Topun ekranın kenarına çarptığı durum

                if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:

                    self.speed_x = -self.speed_x

                if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:

                    self.speed_y = -self.speed_y

        # Tüm sprite'ları içeren grup

        all_sprites = pygame.sprite.Group()

        # Top objesini oluştur ve gruba ekle

        ball = Ball()

        all_sprites.add(ball)

        # Oyun döngüsü

        running = True

        while running:

            # Tüm olayları yakala

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    running = False

            # Tüm sprite'ları güncelle

            all_sprites.update()

            # Ekranı siyah ile doldur

            screen.fill(BLACK)

            # Tüm sprite'ları ekrana çiz

            all_sprites.draw(screen)

            # Ekranı güncelle

            pygame.display.flip()

            # Oyun saatini güncelle

            clock.tick(60)

        # Pygame modülünü kapat

        pygame.quit()

    def running_game():

        import pygame
        import random

        # Ekran boyutu

        SCREEN_WIDTH = 800

        SCREEN_HEIGHT = 600

        # Renkler

        BLACK = (0, 0, 0)

        WHITE = (255, 255, 255)

        # Pygame modülünü başlat

        pygame.init()

        # Ekranı oluştur

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption("Subway Surfers Benzeri Oyun")

        # Saat objesi

        clock = pygame.time.Clock()

        # Oyuncu objesi

        class Player (pygame.sprite.Sprite):

            def __init__(self):

                super().__init__()

                self.image = pygame.Surface((50, 50))

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = 50

                self.rect.y = SCREEN_HEIGHT - self.rect.height - 50

                self.speed_y = 0

            def update(self):

                # Yön tuşlarına basıldığında karakteri hareket ettir

                keys = pygame.key.get_pressed()

                if keys[pygame.K_UP]:

                    self.speed_y = -10

                elif keys[pygame.K_DOWN]:

                    self.speed_y = 10

                else:

                    self.speed_y = 0

                # Karakterin yönünü güncelle

                self.rect.y += self.speed_y

                # Karakterin ekranın dışına çıkmamasını sağla

                if self.rect.bottom > SCREEN_HEIGHT - 50:

                    self.rect.bottom = SCREEN_HEIGHT - 50

                elif self.rect.top < 50:

                    self.rect.top = 50

        # Engeller

        class Obstacle (pygame.sprite.Sprite):

            def __init__(self, speed):

                super().__init__()

                self.image = pygame.Surface((50, 50))

                self.image.fill(WHITE)

                self.rect = self.image.get_rect()

                self.rect.x = SCREEN_WIDTH + 50

                self.rect.y = random.randint(
                    50, SCREEN_HEIGHT - self.rect.height - 50)

                self.speed_x = speed

            def update(self):

                self.rect.x -= self.speed_x

                # Engelin ekranın dışına çıktığını kontrol et

                if self.rect.right < 0:
                    self.kill()

        # Tüm sprite'ları içeren grup

        all_sprites = pygame.sprite.Group()

        # Oyuncu objesini oluştur ve gruba ekle

        player = Player()

        all_sprites.add(player)

        # Engelleri içeren grup

        obstacles = pygame.sprite.Group()

        # Oyun döngüsü

        running = True

        while running:

            # Tüm olayları yakala

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    running = False

            # Engeller oluştur

            if len(obstacles) < 5:

                obstacle_speed = random.randint(5, 15)

                obstacle = Obstacle(obstacle_speed)

                obstacles.add(obstacle)

                all_sprites.add(obstacle)

            # Tüm sprite'ları güncelle

            all_sprites.update()

            # Engellerle çarpışma kontrolü

            hits = pygame.sprite.spritecollide(player, obstacles, False)

            if hits:

                running = False

            # Arka plan rengi

            screen.fill(BLACK)

            # Tüm sprite'ları ekrana çiz

            all_sprites.draw(screen)

            # Ekrana güncellemeleri yansıt

            pygame.display.flip()

            # Saati güncelle

            clock.tick(60)

        # Oyunu kapat

        pygame.quit()

    print("HAZIR OYUNLAR\n \n 1-pong oyunu\n 2-yılan oyunu \n 3-space invadeters oyunu\n 4-ball\n 5-running game")

    oyun_seçim = input("oyun seçin:")

    if oyun_seçim == "1":

        pong_oyunu()

    elif oyun_seçim == "2":

        yılan_oyunu()

    elif oyun_seçim == "3":

        space_invaders()

    elif oyun_seçim == "4":

        ball()

    elif oyun_seçim == "5":

        running_game()

    else:
        anasayfayadon()


def homeapp():
    import datetime
    a = datetime.datetime.ctime()
    print(a)

    print("hoşgeldiniz\n home\\otomasyonlar")

    print("akıllı ev cihazlarınızı yönetin,senaryolar hazırlayın ve zamanlayın.")
    print(

        "akıllı ev cihazlarınızı homeapp'a eklemek için içerisinden çıkan kodu buraya yazın ya da karekodu buraya okutun."
        "\n eklediğiniz cihazlar burada görüntülenir.")
    print(

        " eklediğiniz cihazlarınızı istediğiniz zamanda ve istediğiniz şekilde çalışmak için programlayarak senaryolar oluşturun.")


def radio():
    import pyaudio
    import numpy as np

    # Radyo frekansı ve örnekleme frekansı

    frequency = 99.7  # FM radyonun frekansı

    sampling_rate = 44100  # Sesin örnekleme frekansı

    # Ses pencereleri için değerler

    duration = 5.0  # Her pencere için 5 saniye

    samples_per_window = int(duration * sampling_rate)

    # PyAudio örneği oluştur

    p = pyaudio.PyAudio()

    # Stream oluştur

    stream = p.open(format=pyaudio.paFloat32,

                    channels=1,

                    rate=sampling_rate,

                    output=True)

    # Radyo sinyali oluştur

    t = np.arange(samples_per_window) / float(sampling_rate)

    signal = np.sin(2.0 * np.pi * frequency * t)

    # Sınırsız döngü

    while True:

        # Sinyali oynat

        stream.write(signal.astype(np.float32).tobytes())
        anasayfayadon()


def vallet():
    print(

        "CÜZDAN\nÜzdan uygulamasına hoşgeldin, banka, kredi kartlarını, ulaşım, eğlence biletleri, pass geçişlerini ve araba anahtarlarını buraya ekleyebilirsin.\n")

    print("Kartlar ve biletler\n\n"

          "-------------\n"

          "| |\n"

          "| |\n"

          "-------------\n"

          "(+)\n")

    print("Dijital araba anahtarları\n"

          "-------------\n"

          "| |\n"

          "| |\n"

          "-------------\n(+)\n")
    anasayfayadon()


def görüntülü():

    def görüntülü_devam():

        print("\n\n\n\n\n\n")
        print(

            "görüşmeyi sonlandırmak için sonlandır diyebilirsiniz\n kamera değiştirmek için değiştir diyebilirisiniz."
            "\n mikrofonu veya görüntüyü kapatmak için mikrofon kapat,göeüntü kapat diyebilirsiniz"

            "görüntü ve arka plan efektleri için efektler diyebilirsiniz.")

        ayarla = input(
            "işlem:(kapat\\ efektler\\ kamera,mikrofon kapat\\kamera değiştir\\ ahizeye dön) ")

        if ayarla == "kapat":

            görüşmeyi_sonlandır()

        elif ayarla == "kamera değiştir":

            kamera_değiş()

        elif ayarla == "efektler":
            efektler()

        elif ayarla == "mikrofon kapat":

            mikrofonu_kapat()

        elif ayarla == "görüntüyü kapat":

            görüntüyü_kapat()

        elif ayarla == "ahizeye dön":

            ahize()

        else:

            görüntülü_devam()

    def görüntülü_başlat():

        numara = input("aramak istediğiniz kişi veya numara")
        print(numara)
        print("aranıyor.")

        görüntülü_devam()

    def görüşmeyi_sonlandır():

        print("görüşme sonlandırıldı.")

        değerlendirme = input(
            "görüntülü görüşmeden ne kadar memnun kaldınız (1-5)")

        print(değerlendirme)
        anasayfayadon()

    def kamera_değiş():

        print("tamam!")

    def mikrofonu_kapat():

        print("tamam!")

    def görüntüyü_kapat():

        print("tamam!")
        anasayfayadon()

    def efektler():

        print("1-video efekleri\n 2- arka plan efektletri \n 3- ses efektleri")

        ayarsaç = input(":")

        if ayarsaç == "1":

            print("efekt1\nefekt2\nefekt3\nefekt4\nefekt5\nefekt6\n iptal")

            hangisi = input(":")

            if hangisi == "1":

                print("uygulandı")

                görüntülü_devam()

            elif hangisi == "2":

                print("uygulandı")

                görüntülü_devam()

            elif hangisi == "3":

                print("uygulandı")

                görüntülü_devam()

            elif hangisi == "4":

                print("uygulandı")

                görüntülü_devam()

            elif hangisi == "5":

                print("uygulandı")

                görüntülü_devam()

            elif hangisi == "6":

                print("uygulandı")

                görüntülü_devam()

            elif hangisi == "iptal":

                print("efekt yok,görüşme devam ediyor.")

                görüntülü_devam()

            else:

                print("görüşme devam ediyor.")

                görüntülü_devam()

        elif ayarsaç == "2":

            print("efekt1\n efekt2\n efekt3 \n iptal")

            efekt_hngsi = input(":")

            if efekt_hngsi == "1":

                print("uygulandı")

                görüntülü_devam()

            elif efekt_hngsi == "2":

                print("uygulandı")

                görüntülü_devam()

            elif efekt_hngsi == "3":

                print("uygulandı")

                görüntülü_devam()

            elif efekt_hngsi == "iptal":

                print("efekt yok, görüşme devam ediyor")

                görüntülü_devam()

            else:

                görüntülü_devam()

        elif ayarsaç == "3":

            print("1-dijital gürültü engelleme\n 2-iptal")

            seshangisi = input(":")

            if seshangisi == "1":

                print("gürültü artık filtreleniyor.")

                görüntülü_devam()

            elif seshangisi == "iptal":
                print("efekt yok")

                görüntülü_devam()

            else:

                görüntülü_devam()

    def ahize():

        print("tamam!")

        görüntülü_devam()

    görüntülü_başlat()


kilitekranı()
