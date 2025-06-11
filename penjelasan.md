# Penjelasan Inner Mekanisme Fungsi Script `inverse_kinematics_3dof_3dplot.py`

## 1. `inverse_kinematics_3dof(x, y, z, l1, l2, l3)`
Fungsi ini menghitung sudut-sudut sendi (θ1, θ2, θ3) agar end effector mencapai posisi (x, y, z) tertentu.
- **θ1**: Sudut rotasi dasar, dihitung dengan `atan2(y, x)`.
- **r1**: Jarak horizontal dari pusat ke target (`sqrt(x² + y²)`).
- **r2**: Selisih ketinggian target dengan link pertama (`z - l1`).
- **r3**: Jarak lurus dari pangkal link kedua ke target (`sqrt(r1² + r2²)`).
- **cos_theta3**: Dihitung dengan hukum cosinus, di-clamp agar tetap dalam domain [-1, 1] untuk menghindari error.
- **θ3**: Sudut antara link kedua dan ketiga, hasil dari `acos(cos_theta3)` lalu disesuaikan orientasinya.
- **θ4**: Sudut elevasi ke target (`atan2(r2, r1)`).
- **cos_theta2_1**: Hukum cosinus untuk sudut antara link kedua dan garis ke target, juga di-clamp.
- **θ2_1**: Sudut antara link kedua dan garis ke target.
- **θ2**: Penjumlahan θ4 dan θ2_1.
- **Output**: θ1, θ2, θ3 (radian).

---

## 2. `forward_kinematics_3dof(theta1, theta2, theta3, l1, l2, l3)`
Fungsi ini menghitung posisi setiap sendi dan end effector berdasarkan sudut dan panjang link.
- **Base**: (0, 0, 0)
- **Joint 1**: (0, 0, l1)
- **Joint 2**: 
  - x2 = l2 * cos(θ2) * cos(θ1)
  - y2 = l2 * cos(θ2) * sin(θ1)
  - z2 = l1 + l2 * sin(θ2)
- **End Effector**:
  - x3 = x2 + l3 * cos(θ2 + θ3) * cos(θ1)
  - y3 = y2 + l3 * cos(θ2 + θ3) * sin(θ1)
  - z3 = z2 + l3 * sin(θ2 + θ3)
- **Output**: List tuple posisi [(x0, y0, z0), ..., (x3, y3, z3)].

---

## 3. `plot_robot(joints)`
Fungsi ini menampilkan visualisasi statis lengan robot berdasarkan posisi sendi.
- Ekstrak koordinat X, Y, Z dari list `joints`.
- Membuat plot 3D dan menggambar garis antar sendi dengan marker.
- Menandai end effector dengan warna merah.
- Menambahkan label sumbu, judul, legend, dan aspek rasio proporsional.
- Menampilkan plot.

---

## 4. `interactive_robot(l1, l2, l3, start_x, start_y, start_z)`
Fungsi ini menyediakan antarmuka interaktif untuk mengatur posisi end effector dan melihat hasilnya secara real-time.
- Membuat figure dengan dua subplot: 3D plot dan tabel parameter.
- Menampilkan info penulis di bawah plot.
- Mengatur label, batas, dan aspek plot 3D.
- Membuat objek garis dan marker end effector untuk update dinamis.
- Membuat tabel untuk menampilkan X, Y, Z, θ1, θ2, θ3.
- Membuat slider untuk X, Y, Z, elevasi, dan azimuth view.
- Membuat textbox untuk input X, Y, Z secara manual.
- **Fungsi `update`:**
  - Membaca nilai slider.
  - Hitung inverse kinematics → dapatkan sudut.
  - Hitung forward kinematics → dapatkan posisi sendi.
  - Update posisi garis dan marker di plot.
  - Update tampilan tabel dengan nilai terbaru.
  - Sinkronisasi nilai textbox dengan slider.
  - Redraw canvas.
- **Fungsi `submit_x/y/z`:**
  - Mengubah nilai slider jika textbox diubah.
- Menghubungkan slider dan textbox ke fungsi update/submit.
- Memanggil `update()` pertama kali, lalu menampilkan plot.

---

Setiap fungsi saling terhubung untuk membentuk simulasi robot 3 DOF yang interaktif dan informatif.
