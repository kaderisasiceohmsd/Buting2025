(function() {
  try {
    const pilihan = "Sangat Setuju";
    const radios = document.querySelectorAll('input[type="radio"]');
    
    if (!radios.length) {
      alert("Tidak ditemukan tombol radio di halaman ini.");
      return;
    }

    let filledCount = 0;
    radios.forEach(radio => {
      const label = radio.nextElementSibling?.textContent?.trim() || radio.value || "";
      if (label.toLowerCase().includes(pilihan.toLowerCase())) {
        radio.checked = true;
        filledCount++;
      }
    });

    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    alert(`Berhasil mengisi ${filledCount} pertanyaan dengan pilihan "${pilihan}".`);
  } catch (error) {
    alert("Terjadi kesalahan: " + error.message);
  }
})();