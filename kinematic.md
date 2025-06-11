# Perancangan Metode Invers Kinematik 3 DOF

Nama: Agung Rambujana
NIM: 221364002  
Kelas: 3B-T01

## Perancangan metode invers kinematik 3 DOF
Pada perancangan metode invers kinematik, didapatkan rumus dari perancangan link dan joint robot 3 DOF.

### Gambar Robot

![Robot 3 DOF]()

### Penjelasan

Perhitungan rumus bertujuan untuk mendapatkan nilai θ1, θ2, θ3, 
sebelum mencari ketiga nilai θ ditentukan terlebih dahulu nilai dan koordinat (x, y, z) dan panjang link (l1, l2, l3).
Terdapat 3 link pada robot, yaitu link antara A dan B, link antara B dan C, dan link antara C dan end effector. 
Masing-masing memiliki panjang 4cm, 7cm, 11cm.

#### Diketahui:
x = 5, y = 12, z = 14
l1 = 4 cm, l2 = 7 cm, l3 = 11 cm

### Penyelesaian

Dalam menyelesaikan permasalahan invers kinematik dapat menggunakan metode pendekatan geometri.
Untuk mendapatkan sudut posisi end-effector tertentu, metode ini menggunakan aturan kosinus, aturan segitiga (th. Pythagoras), dan aturan trigonometri.

Oleh karena itu, setiap link pada lengan robot dibagi menjadi bentuk segitiga, seperti gambar. Proses solusi:

#### Mencari sudut shoulder (θ1)

θ1 = tan⁻¹(y/x)
   = tan⁻¹(12/5)
   = 67,38°

#### Mencari r1, r2, r3

r1 = √(x² + y²)
   = √(5² + 12²)
   = √(25 + 144)
   = √169
   = 13

r2 = z - l1
   = 14 - 4
   = 10

r3 = √(r1² + r2²)
   = √(13² + 10²)
   = √(169 + 100)
   = √269
   = 16,40

#### Mencari θ3

θ3 = cos⁻¹((l2² + l3² - r3²) / (2 * l2 * l3))
    = cos⁻¹((7² + 11² - 16,40²) / (2 * 7 * 11))
    = cos⁻¹((49 + 121 - 268,96) / 154)
    = cos⁻¹((-98,96) / 154)
    = 129,00°

θ3 = -(180° - 129,00°)
    = -51,00°

#### Mencari θ2

θ3 = 129,00°

θ2 = θ4 + θ2_1

θ4 = tan⁻¹(r2/r1)
   = tan⁻¹(10/13)
   = 37,66°

θ2_1 = cos⁻¹((l2² + r3² - l3²) / (2 * l2 * r3))
     = cos⁻¹((7² + 16,40² - 11²) / (2 * 7 * 16,40))
     = cos⁻¹((49 + 268,96 - 121) / 229,6)
     = cos⁻¹(196,96 / 229,6)
     = 29,13°

θ2 = θ4 + θ2_1
   = 37,66° + 29,13°
   = 66,79°

### Jadi nilai θ1, θ2, θ3 adalah:
- θ1 = 67,38°
- θ2 = 66,79°
- θ3 = -51,00°