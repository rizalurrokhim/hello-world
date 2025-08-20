import tkinter as tk
from tkinter import messagebox
import random

# --- window setup ---
root = tk.Tk()
root.title("Yes atau No?")
root.geometry("520x320")   # ukuran awal jendela
root.minsize(360, 240)

# Pesan petunjuk
hint = tk.Label(root, text="Pilih Yes atau coba kejar tombol No 😄", font=("Segoe UI", 11))
hint.pack(pady=16)

# Buat tombol (pakai place agar bisa dipindah acak)
btn_yes = tk.Button(root, text="Yes", width=10, font=("Segoe UI", 10))
btn_no  = tk.Button(root, text="No",  width=10, font=("Segoe UI", 10))

def place_initial():
    """Posisikan tombol awalnya di tengah."""
    root.update_idletasks()
    y = root.winfo_height() // 2
    x_yes = root.winfo_width() // 2 - 110
    x_no  = root.winfo_width() // 2 + 30
    btn_yes.place(x=x_yes, y=y)
    btn_no.place(x=x_no, y=y)

def move_no():
    """Pindahkan tombol No ke posisi acak dalam jendela."""
    root.update_idletasks()
    w, h = root.winfo_width(), root.winfo_height()
    bw, bh = btn_no.winfo_width(), btn_no.winfo_height()

    # Batas aman supaya tidak keluar jendela
    max_x = max(0, w - bw - 10)
    max_y = max(0, h - bh - 10)
    new_x = random.randint(10, max_x)
    new_y = random.randint(10, max_y)
    btn_no.place(x=new_x, y=new_y)

def yes_clicked():
    """Tampilkan kalimat saat Yes ditekan, lalu nonaktifkan tombol."""
    messagebox.showinfo("Mantap!", "Kamu memilih YES! Semoga harimu menyenangkan 🌟")
    btn_yes.config(state="disabled")
    btn_no.config(state="disabled")

# Kaitkan aksi
btn_yes.config(command=yes_clicked)
btn_no.config(command=move_no)

# Tempatkan tombol awal
place_initial()

# Jalankan aplikasi
root.mainloop()
