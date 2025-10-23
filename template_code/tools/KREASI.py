import streamlit as st
import numpy as np
import pandas as pd

# Fungsi untuk memproses string persamaan menjadi koefisien (menggunakan x, y, z)
def parse_equation(eq_str, num_vars=3):
    try:
        # Pisahkan LHS dan RHS
        parts = eq_str.split('=')
        if len(parts) != 2:
            raise ValueError("Persamaan harus mengandung satu tanda '='.")
        
        lhs = parts[0].strip()
        rhs = float(parts[1].strip()) # Konstanta (b)

        # Urutan koefisien: [x, y, z]
        coeffs = [0.0] * num_vars
        
        # Ganti tanda minus dengan "+-" agar mudah di-split
        clean_lhs = lhs.replace('-', '+-').replace(' ', '')
        
        # Split berdasarkan '+'
        terms = [t for t in clean_lhs.split('+') if t]
        
        for term in terms:
            term = term.strip()
            if not term:
                continue

            # Cari variabel dan indeksnya
            idx = -1
            var_str = ''
            
            if 'x' in term and 'x' == term[-1] or ('x' in term and term.find('x') < term.find('y') and term.find('x') < term.find('z')):
                # Ini adalah koefisien x (idx 0)
                idx = 0
                var_str = 'x'
            elif 'y' in term:
                # Ini adalah koefisien y (idx 1)
                idx = 1
                var_str = 'y'
            elif 'z' in term:
                # Ini adalah koefisien z (idx 2)
                idx = 2
                var_str = 'z'
            else:
                continue # Abaikan jika tidak ada variabel

            # Ekstraksi koefisien
            coeff_part = term.replace(var_str, '').strip()
            
            if coeff_part == '':
                coeff = 1.0  # Kasus: x
            elif coeff_part == '-':
                coeff = -1.0 # Kasus: -y
            else:
                coeff = float(coeff_part)
            
            coeffs[idx] = coeff
        
        return coeffs, rhs
    except ValueError as e:
        st.error(f"Error parsing persamaan: {eq_str}. Pastikan variabel yang digunakan hanya x, y, dan z. Pesan: {e}")
        return None, None
    except Exception as e:
        st.error(f"Error tidak terduga saat parsing: {e}")
        return None, None

# Fungsi untuk mengecek Dominasi Diagonal (Tidak berubah, karena bekerja pada Matriks A)
def check_diagonal_dominance(A):
    n = A.shape[0]
    is_dominant = True
    results = []
    for i in range(n):
        diag_val = abs(A[i, i])
        sum_off_diag = np.sum(abs(A[i, :])) - diag_val
        
        if diag_val > sum_off_diag:
            status = "**TERPENUHI** :material/check:"
            row_dominant = True
        else:
            status = "**TIDAK TERPENUHI** :material/report_problem:"
            row_dominant = False
            is_dominant = False
            
        # Catatan: Variabel x, y, z diwakili oleh kolom 1, 2, 3
        
        results.append({
            "Baris": i + 1,
            "Syarat": f"$|a_{{{i+1}{i+1}}}| > \sum_{{j \neq {i+1}}} |a_{{{i+1}j}}|$",
            "Perhitungan": f"$|{A[i, i]}| > |{A[i, 0] if i!=0 else ''}| + |{A[i, 1] if i!=1 else ''}| + |{A[i, 2] if i!=2 else ''}|$ \n\n {diag_val} > {sum_off_diag}",
            "Status": status
        })
        
    return is_dominant, results

# Fungsi utama Metode Jacobi (Tidak berubah, karena bekerja pada vektor dan matriks)
def jacobi_iteration(A, b, max_iter, tolerance, x0):
    n = len(b)
    
    # Ganti nama kolom output
    history = pd.DataFrame(columns=['Iterasi', 'x', 'y', 'z', 'Error (max)'])
    
    x_current = np.array(x0, dtype=float)
    
    for k in range(max_iter):
        x_new = np.zeros(n)
        
        # Hitung nilai x_new
        for i in range(n):
            sum_val = 0
            for j in range(n):
                if i != j:
                    sum_val += A[i, j] * x_current[j]
            
            x_new[i] = (b[i] - sum_val) / A[i, i]
            
        # Hitung error (galat)
        error = np.max(np.abs(x_new - x_current))
        
        # Tambahkan ke history
        new_row = [k + 1] + x_new.tolist() + [error]
        history.loc[k] = new_row
        
        # Cek konvergensi
        if error < tolerance:
            break
            
        x_current = x_new
        
    return history, x_current

# --- Streamlit UI ---
st.title("Metode Iterasi Jacobi untuk SPL $3 \\times 3$")
st.markdown("""
Aplikasi ini menyelesaikan Sistem Persamaan Linear (SPL) $3 \\times 3$ menggunakan Metode Iterasi Jacobi.
Input format persamaan: :blue[a*x + b*y + c*z = d] (contoh: :blue[5x + 1y + 2z = 19]).
""")

# Input Persamaan
st.header("1. Input Persamaan Linear")

# Mengganti placeholder input
eq1 = st.text_input("Persamaan 1:", "5x + 1y + 2z = 19")
eq2 = st.text_input("Persamaan 2:", "x + 4y - 2z = 20")
eq3 = st.text_input("Persamaan 3:", "2x - 3y + 8z = 37")

st.header("2. Pengaturan Iterasi")
col1, col2, col3 = st.columns(3)
max_iter = col1.number_input("Max Iterasi", min_value=1, value=7, step=1)
tolerance = col2.number_input("Toleransi ($\epsilon$)", min_value=1e-10, value=0.07, format="%.6f")
# Mengganti placeholder input
initial_guess = col3.text_input("Tebakan Awal (x, y, z)", "0, 0, 0")

if st.button("Hitung Solusi Jacobi"):
    # Parsing input
    coeffs1, b1 = parse_equation(eq1)
    coeffs2, b2 = parse_equation(eq2)
    coeffs3, b3 = parse_equation(eq3)

    # Validasi Parsing
    if None in [coeffs1, b1, coeffs2, b2, coeffs3, b3]:
        st.error("Periksa kembali format input persamaan Anda.")
    else:
        A = np.array([coeffs1, coeffs2, coeffs3])
        b = np.array([b1, b2, b3])
        
        try:
            x0 = [float(val.strip()) for val in initial_guess.split(',')]
            if len(x0) != 3:
                 st.error("Tebakan Awal harus berupa 3 angka yang dipisahkan koma.")
                 st.stop()
        except ValueError:
            st.error("Tebakan Awal tidak valid.")
            st.stop()


        st.header("3. Bentuk Matriks")
        st.latex(f"\\mathbf{{A}} = \\begin{{bmatrix}} {A[0,0]} & {A[0,1]} & {A[0,2]} \\\\ {A[1,0]} & {A[1,1]} & {A[1,2]} \\\\ {A[2,0]} & {A[2,1]} & {A[2,2]} \\end{{bmatrix}}, \\quad \\mathbf{{b}} = \\begin{{bmatrix}} {b[0]} \\\\ {b[1]} \\\\ {b[2]} \\end{{bmatrix}}")

        
        # Cek Dominan Diagonal
        st.header("4. Cek Syarat Dominan Diagonal")
        is_dominant, dd_results = check_diagonal_dominance(A)
        
        dd_df = pd.DataFrame(dd_results)
        st.table(dd_df[['Baris', 'Syarat', 'Status']])
        
        if is_dominant:
            st.success(":heavy_check_mark: **Matriks Dominan Diagonal.** Metode Jacobi dijamin konvergen.")
        else:
            st.warning(":material/report_problem: **Matriks TIDAK Dominan Diagonal.** Metode Jacobi mungkin tidak konvergen. Coba susun ulang persamaannya.")
        
        st.divider()

        # Mulai Iterasi
        st.header("5. Hasil Iterasi Metode Jacobi")
        
        # Jalankan Jacobi
        history_df, final_solution = jacobi_iteration(A, b, max_iter, tolerance, x0)
        
        # Format angka dalam tabel
        history_df['x'] = history_df['x'].round(6)
        history_df['y'] = history_df['y'].round(6)
        history_df['z'] = history_df['z'].round(6)
        history_df['Error (max)'] = history_df['Error (max)'].round(8)
        
        st.dataframe(history_df, use_container_width=True)
        
        # Tampilkan solusi akhir
        if history_df['Error (max)'].iloc[-1] < tolerance:
            st.success(f"**Solusi ditemukan** pada iterasi ke-{len(history_df)} (dengan toleransi $\epsilon = {tolerance}$):")
        else:
            st.info(f"Proses dihentikan setelah {max_iter} iterasi (batas maksimum).")
            
        st.markdown(f"**x ≈ {final_solution[0]:.6f}, y ≈ {final_solution[1]:.6f}, z ≈ {final_solution[2]:.6f}**")