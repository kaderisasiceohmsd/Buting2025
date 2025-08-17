PENJELASAN SINGKAT SETIAP FOLDER

- Folder .streamlit 
Berisi file config.toml untuk mengubah warna website.

- Folder Buku Kating
Berisi file pyhton (.py) masing-masing anggota kelompok untuk menyimpan data diri kating beserta foto bersama kating
penambahan data diri berada dalam variabel "data_list" dan penambahan data kating berada dalam variabel "gambar_urls"

- Folder Halaman Utama
Berisi file halaman_utama.py. file ini berguna untuk menangani tampilan utama websita. Perubahan dilakukan di 2 page yaitu Home dan About Us.
Home:
  - Data yang perlu diubah adalah bagian st.markdown yang memuat kata lore ipsum. Bagian ini dibah menjadi deskripsi anggota kelompok
  - Variabel foto_kelompok perlu diubah data fotonya.
About Us:
  - Data diri dan foto anggota perlu diubah ddatanya.

- Folder tools
Berisi file KREASI.py dan KREASII.py, file ini merupakan file yang akan digunakan kelompok untuk membuat tugas kelompok 
yang akan diinfokan lebih lanjut terkait tugasnya.

- File main.py
Merupakan file utama dari website ini. Setiap anggota perlu menambahkan file mereka sendiri untuk buku kating, 
dengan membuat variabel Mahasiswa1, Mahasiswa2 dst.
Pada bagian if st.session_state.pindah terdapat dictionary dengan key "Buku kating", Key ini perlu berisikan value yaitu variabel Mahasiswa(1-n)

- File requirements.txt
Sebuah file untuk menuliskan library python apa saja yang digunakan pada pengerjaan website ini.
untuk mengecek versi library yang digunakan, 
ketik pip freeze di cmd, setelah itu cari nama library yang digunakan untuk mengetahui versi library tersebut.
