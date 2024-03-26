class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    @staticmethod
    def print_data_mahasiswa(mahasiswa):
        i = 1
        # Urutkan mahasiswa berdasarkan NIM sebelum mencetak
        sorted_mahasiswa = sorted(mahasiswa, key=lambda x: x.nim)
        for mhs in sorted_mahasiswa:
            print("--- Data Mahasiswa", i, "---")
            print("Nama:", mhs.nama)
            print("NIM:", mhs.nim)
            print("Nilai:", mhs.nilai)
            print()
            i += 1

def main():
    mahasiswa = [
        Mahasiswa("Fairuz Maulidya", "064002030018", 100),
        Mahasiswa("Reyhan Arnas", "064002300002", 99),
        Mahasiswa("Calista Azzahra", "064002300008 ", 95),
        Mahasiswa(" Zahwa Nur Azkia", "064002300038", 80)
    ]
    # Panggil metode print_data_mahasiswa menggunakan looping
    Mahasiswa.print_data_mahasiswa(mahasiswa)

main()
