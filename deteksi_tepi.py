import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== Program Turunan Numerik: Edge Detection ===")
    print("Oleh: Muhammad Riza Saputra - 21120123140117\n")

    # 1. MEMBUAT DATA CITRA SINTETIS
    # Matriks 100x100, latar hitam (0), objek kotak putih (255)
    img_size = 100
    image = np.zeros((img_size, img_size))
    image[25:75, 25:75] = 255 # Membuat kotak di tengah

    # Inisialisasi array hasil
    gradien_x = np.zeros_like(image)
    gradien_y = np.zeros_like(image)
    magnitude = np.zeros_like(image)

    # 2. IMPLEMENTASI METODE SELISIH TENGAH
    rows, cols = image.shape
    
    # Iterasi setiap pixel (kecuali batas pinggir)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            
            # Turunan terhadap x (Horizontal)
            # Rumus: (f(x+1) - f(x-1)) / 2
            gx = (image[i, j+1] - image[i, j-1]) / 2.0
            gradien_x[i, j] = gx

            # Turunan terhadap y (Vertikal)
            # Rumus: (f(y+1) - f(y-1)) / 2
            gy = (image[i+1, j] - image[i-1, j]) / 2.0
            gradien_y[i, j] = gy

            # Menghitung Magnitude
            magnitude[i, j] = np.sqrt(gx**2 + gy**2)

    # 3. VISUALISASI HASIL
    plt.figure(figsize=(12, 4))

    # Citra Asli
    plt.subplot(1, 4, 1)
    plt.imshow(image, cmap='gray')
    plt.title("1. Citra Asli")
    plt.axis('off')

    # Gradien X
    plt.subplot(1, 4, 2)
    plt.imshow(gradien_x, cmap='gray')
    plt.title("2. Turunan dF/dx")
    plt.axis('off')

    # Gradien Y
    plt.subplot(1, 4, 3)
    plt.imshow(gradien_y, cmap='gray')
    plt.title("3. Turunan dF/dy")
    plt.axis('off')

    # Magnitude
    plt.subplot(1, 4, 4)
    plt.imshow(magnitude, cmap='gray')
    plt.title("4. Hasil Deteksi Tepi")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()