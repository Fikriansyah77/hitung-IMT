# PROGRAM_MENGHITUNG_IMT
def hitung_IMT(weight, height):
    imt = weight / (height ** 2)
    return imt

def kategori_IMT(imt):
    if imt < 18.5:
        return "Kurus"
    elif 18.5 <= imt < 25:
        return "Normal"
    elif 25 <= imt < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def main():
    hasil_imt = [] 
    
    jumlah_orang = int(input("Masukkan jumlah orang: "))
    
    for i in range(jumlah_orang):
        print(f"\nOrang ke-{i + 1}")
        weight = float(input("Masukkan berat badan (kg): "))
        height = float(input("Masukkan tinggi badan (meter): "))
        
        if weight == 0.0 and height == 0.0:
            print("Input dihentikan.")
            break
        
        imt = hitung_IMT(weight, height )  
        kategori = kategori_IMT(imt)  
        hasil_imt.append((weight, height, imt, kategori))  
        
        print(f"Berat: {weight} kg \nTinggi: {height} cm")
        print(f"IMT: {imt:.2f} \nKategori: {kategori}")
        
    print("\nRingkasan:")
    for idx, (weight, height, imt, kategori) in enumerate(hasil_imt, start=1):
        print(f"Orang ke-{idx}: Berat = {weight} kg, Tinggi = {height} cm, IMT = {imt:.2f}, Kategori = {kategori}")

# menjalankan program
if __name__ == "__main__":
    main()
