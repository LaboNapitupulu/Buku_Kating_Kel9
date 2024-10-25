import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

# membuat jendela utama
root = tk.Tk()
root.title("Penghasil Gambar")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)
style = Style(theme="sandstone")

# mendefinisikan fungsi untuk mengambil dan menampilkan gambar berdasarkan kategori yang dipilih
def tampilkan_gambar(kategori):
    # membuat permintaan ke API Unsplash untuk mendapatkan gambar acak
    url = f"https://api.unsplash.com/photos/random?query={kategori}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    foto = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
    label.config(image=foto)
    label.image = foto

# fungsi untuk mengaktifkan / menonaktifkan tombol "Hasilkan Gambar"
def aktifkan_tombol(*args):
    tombol_hasilkan.config(state="normal" if kategori_var.get() != "Pilih Kategori" else "disabled")

# membuat elemen-elemen GUI
def buat_gui():
    global kategori_var, tombol_hasilkan, label

    # membuat menu dropdown untuk memilih kategori
    kategori_var = tk.StringVar(value="Pilih Kategori")
    opsi_kategori = ["Pilih Kategori", "Makanan", "Hewan", "Orang", "Musik", "Seni", "Kendaraan", "Acak"]
    dropdown_kategori = ttk.OptionMenu(root, kategori_var, *opsi_kategori, command=aktifkan_tombol)
    dropdown_kategori.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    dropdown_kategori.config(width=14)

    # membuat tombol untuk menghasilkan gambar
    tombol_hasilkan = ttk.Button(text="Hasilkan Gambar", state="disabled", command=lambda: tampilkan_gambar(kategori_var.get()))
    tombol_hasilkan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # membuat kolom/baris agar bisa diperluas
    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    buat_gui()
