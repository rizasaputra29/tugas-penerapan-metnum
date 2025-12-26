import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== Program Prediksi Harga Rumah (Regresi Linear) ===")
    print("Oleh: Muhammad Riza Saputra - 21120123140117\n")

    # 1. Data Sampel (Luas Tanah dalam m2, Harga dalam Juta Rupiah)
    x_luas = np.array([60, 72, 90, 100, 120, 150, 200])  # Variable X (Independent)
    y_harga = np.array([300, 450, 550, 600, 750, 900, 1200]) # Variable Y (Dependent)

    # 2. Menghitung Komponen Rumus Regresi Linear
    n = len(x_luas)
    sum_x = np.sum(x_luas)
    sum_y = np.sum(y_harga)
    sum_xy = np.sum(x_luas * y_harga)
    sum_x2 = np.sum(x_luas ** 2)

    # 3. Menghitung Slope (m) dan Intercept (c)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    c = (sum_y - m * sum_x) / n

    print(f"Hasil Perhitungan:")
    print(f"Slope (m): {m:.2f}")
    print(f"Intercept (c): {c:.2f}")
    print(f"Persamaan Regresi: Y = {m:.2f}X + {c:.2f}")

    # 4. Demonstrasi Prediksi
    print("\n--- Demonstrasi Prediksi ---")
    input_luas = float(input("Masukkan luas tanah yang ingin diprediksi (m2): "))
    prediksi_harga = m * input_luas + c
    print(f"Estimasi harga untuk tanah {input_luas} m2 adalah: Rp {prediksi_harga:.2f} Juta")

    # 5. Visualisasi Data
    plt.scatter(x_luas, y_harga, color='blue', label='Data Aktual')
    
    # Membuat garis regresi
    garis_x = np.linspace(min(x_luas), max(x_luas), 100)
    garis_y = m * garis_x + c
    plt.plot(garis_x, garis_y, color='red', label='Garis Regresi')
    
    # Plot titik prediksi user
    plt.scatter(input_luas, prediksi_harga, color='green', marker='x', s=100, label='Prediksi User')

    plt.title('Regresi Linear: Luas Tanah vs Harga Rumah')
    plt.xlabel('Luas Tanah (m2)')
    plt.ylabel('Harga (Juta Rp)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()