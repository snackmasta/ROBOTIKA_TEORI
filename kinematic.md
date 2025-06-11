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
x = 8, y = 14, z = 10
l1 = 4 cm, l2 = 7 cm, l3 = 11 cm

### Penyelesaian

Dalam menyelesaikan permasalahan invers kinematik dapat menggunakan metode pendekatan geometri.
Untuk mendapatkan sudut posisi end-effector tertentu, metode ini menggunakan aturan kosinus, aturan segitiga (th. Pythagoras), dan aturan trigonometri.

Oleh karena itu, setiap link pada lengan robot dibagi menjadi bentuk segitiga, seperti gambar. Proses solusi:

#### Mencari sudut shoulder (θ1)

θ1 = tan⁻¹(y/x)
   = tan⁻¹(14/8)
   = 60,26°

#### Mencari r1, r2, r3

r1 = √(x² + y²)
   = √(8² + 14²)
   = √(64 + 196)
   = √260
   = 16,12

r2 = z - l1
   = 10 - 4
   = 6

r3 = √(r1² + r2²)
   = √(16,12² + 6²)
   = √(260 + 36)
   = √296
   = 17,2

#### Mencari θ3

θ3 = cos⁻¹((l2² + l3² - r3²) / (2 * l2 * l3))
    = cos⁻¹((7² + 11² - 17,2²) / (2 * 7 * 11))
    = cos⁻¹((49 + 121 - 295,84) / 154)
    = cos⁻¹((-125,84) / 154)
    = 144,90°

θ3 = -(180° - 144,90°)
    = -(180° - 144,90°)
    = -35,10°

#### Mencari θ2

θ3 = 144,90°

θ2 = θ4 + θ2_1

θ4 = tan⁻¹(r2/r1)
   = tan⁻¹(6/16,12)
   = 20,42°

θ2_1 = cos⁻¹((l2² + r3² - l3²) / (2 * l2 * r3))
     = cos⁻¹((7² + 17,2² - 11²) / (2 * 7 * 17,2))
     = cos⁻¹((49 + 295,84 - 121) / 240,8)
     = cos⁻¹(223,84 / 240,8)
     = 21,86°

θ2 = θ4 + θ2_1
   = 20,42° + 21,86°
   = 41,90°

### Jadi nilai θ1, θ2, θ3 adalah:
- θ1 = 60,26°
- θ2 = 41,90°
- θ3 = -35,10°