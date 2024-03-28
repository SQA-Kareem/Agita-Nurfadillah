import time  # Import modul time untuk penanganan waktu
import unittest  # Import modul unittest untuk melakukan unit testing
from selenium import webdriver  # Import modul webdriver dari Selenium untuk mengotomatisasi browser
from selenium.webdriver.common.by import By  # Import modul By dari Selenium untuk menentukan metode pencarian elemen
from selenium.webdriver.support.ui import WebDriverWait  # Import modul WebDriverWait dari Selenium untuk menunggu hingga kondisi terpenuhi
from selenium.webdriver.support import expected_conditions as EC  # Import modul expected_conditions dari Selenium untuk mengevaluasi kondisi yang diharapkan
from selenium.webdriver.common.keys import Keys  # Import modul Keys dari Selenium untuk mengirim kunci keyboard

class SystemTest(unittest.TestCase):  # Definisikan kelas SystemTest untuk unit testing
    def setUp(self):  # Metode setUp akan dijalankan sebelum setiap metode pengujian
        # Inisialisasi WebDriver, dalam hal ini Chrome
        self.driver = webdriver.Chrome()

    def tearDown(self):  # Metode tearDown akan dijalankan setelah setiap metode pengujian selesai
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(10)

        # Menutup WebDriver
        self.driver.quit()

    def role(self):  # Metode role untuk melakukan tindakan sign up
        # Temukan elemen dropdown untuk memilih peran
        selected = self.driver.find_element(By.ID, "af-submit-app-category")
    
        selected.click()

        # Klik panah bawah di dalam dropdown
        selected.send_keys(Keys.ARROW_DOWN)
        selected.click()

        time.sleep(2)

        # Temukan tombol submit dan klik
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Temukan elemen input untuk masing-masing data sign up
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        confirmpass_input = self.driver.find_element(By.ID, "confirmpass")
        namalengkap_input = self.driver.find_element(By.ID, "namalengkap")
        tanggallahir_input = self.driver.find_element(By.ID, "tanggallahir")
        jeniskelamin_input = self.driver.find_element(By.ID, "jeniskelamin")
        jeniskelamin_input.click()
        nim_input = self.driver.find_element(By.ID, "nim")
        perguruan_tinggi = self.driver.find_element(By.ID, "perguruantinggi")
        prodi_input = self.driver.find_element(By.ID, "prodi")

        # Masukkan data ke dalam elemen input
        email_input.send_keys("najaemi11n@gmail.com")
        phone_input.send_keys("082246229980")
        password_input.send_keys("asdfghjkl")
        confirmpass_input.send_keys("asdfghjkl")
        namalengkap_input.send_keys("Muhammad11 Najaemin")
        tanggallahir_input.send_keys("06/06/2000")
        jeniskelamin_input.send_keys(Keys.ARROW_DOWN)
        nim_input.send_keys("1214034")
        perguruan_tinggi.send_keys("ULBI")
        prodi_input.send_keys("D4 Teknik Informatika")

        time.sleep(2)

        # Klik tombol sign up
        buttons = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        buttons.click()

        time.sleep(2)

        # Temukan dan klik tombol OK pada pop-up konfirmasi
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

        time.sleep(2)
        self.login("najaemi11n@gmail.com", "asdfghjkl")

    def login(self, username, password):
        # Temukan tombol login di dalam menu
        # button_login = self.driver.find_element(By.ID, "login")
        # button_login.click()

        # Mencari elemen input username dan password menggunakan ID
        # username_input = self.driver.find_element(By.ID, "username")
        # password_input = self.driver.find_element(By.ID, "password")

        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "hs-toggle-password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        # button = self.driver.find_element(By.ID, "btnLogin")

        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

    def logout(self):
        button = self.driver.find_element(By.XPATH, "//button[@id='profile-btn']")
        button.click()

        time.sleep(5)

        button = self.driver.find_element(By.XPATH, "//a[@onclick='logout()']")
        button.click()

        time.sleep(2)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

    def test_signup(self):  # Metode untuk melakukan pengujian proses sign up
        # Buka halaman web yang akan diuji
        self.driver.get("https://intermoni.my.id/")

        time.sleep(2)

        # Temukan tombol sign up dan klik
        button = self.driver.find_element(By.XPATH, "//a[@href='pages/signUp.html']")
        button.click()

        # Jalankan proses sign up dengan memanggil metode role
        self.role()

        time.sleep(2)

        self.logout()


if __name__ == "__main__":
    unittest.main()