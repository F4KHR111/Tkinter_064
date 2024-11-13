import tkinter as tk
from tkinter import messagebox

#Fungsi menampilkan hasil prediksi dan validasi nilai
def prediksi_prodi():
    total = 0  # Inisialisasi variabel untuk menyimpan total nilai
    valid = True # Variabel untuk menandakan apakah semua input valid
    for entry in entries: # Loop untuk iterasi melalui setiap entry (input nilai)
        try:
            nilai = float(entry.get())
            if nilai < 0 or nilai > 100:
                messagebox.showerror("Input Error", "Pastikan nilai yang diinput dari angka 0-100")
                valid = False
                break
            total += nilai
        except ValueError:
            messagebox.showerror("Input Error", "Pastikan semua nilai yang dimasukkan adalah angka.")
            valid = False
            break

    if valid: 
        rata_rata = total / len(entries) # Menghitung rata-rata nilai
        hasil_label.config(text=f"Prodi Pilihan: Teknologi Informasi\nRata-rata Nilai: {rata_rata:.2f}")

#Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x800")

#Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 16))
judul_label.pack(pady=10)

#Membuat input untuk nilai mata pelajaran
entries = []
for i in range(1, 11):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:", font=("Times New Roman", 12))
    label.pack(anchor="w", padx=20)
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5, padx=20, fill="x")
    entries.append(entry)

#Button untuk mendapatkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi, font=("Times New Roman", 12))
prediksi_button.pack(pady=20)

#Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Times New Roman", 14), fg="black")
hasil_label.pack(pady=10)

#Menjalankan loop utama aplikasi
root.mainloop()