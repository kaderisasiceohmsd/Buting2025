import streamlit as st
import numpy as np
import pandas as pd
import time

def gauss_jordan_elimination(A, b):
    """
    Melakukan eliminasi Gauss-Jordan pada matriks A dan vektor b
    Mengembalikan solusi dan langkah-langkahnya dengan penjelasan detail
    """
    # Gabungkan matriks A dan vektor b menjadi augmented matrix
    augmented = np.hstack((A.astype(float), b.astype(float).reshape(-1, 1)))
    n = len(b)
    
    steps = []
    solution = None
    
    try:
        # Salin augmented matrix untuk proses
        current_matrix = augmented.copy()
        
        # Langkah 0: Tampilkan matrix awal
        steps.append(("Matrix Augmented Awal", current_matrix.copy(), "Matrix awal [A|b]"))
        
        # Eliminasi maju (forward elimination) dan backward elimination
        for i in range(n):
            # Pivoting partial: cari baris dengan nilai absolut terbesar di kolom i
            max_row = i
            for k in range(i + 1, n):
                if abs(current_matrix[k, i]) > abs(current_matrix[max_row, i]):
                    max_row = k
            
            # Tukar baris jika diperlukan
            if max_row != i:
                current_matrix[[i, max_row]] = current_matrix[[max_row, i]]
                steps.append((f"Pivoting: Tukar Baris", current_matrix.copy(), 
                             f"R_{i+1} ↔ R_{max_row+1} (Pivoting untuk elemen diagonal terbesar)"))
            
            # Jika pivot 0, matrix singular
            if abs(current_matrix[i, i]) < 1e-10:
                steps.append(("ERROR: Matrix singular", None, "Matrix singular - tidak ada solusi unik"))
                return None, steps
            
            # Buat pivot menjadi 1
            pivot = current_matrix[i, i]
            if abs(pivot - 1.0) > 1e-10:  # Hanya tampilkan jika perubahan diperlukan
                current_matrix[i] = current_matrix[i] / pivot
                steps.append((f"Normalisasi Pivot", current_matrix.copy(), 
                             f"R_{i+1} → R_{i+1} / {pivot:.2f} (Membuat a_{i+1}{i+1} = 1)"))
            
            # Eliminasi kolom i di semua baris lain (termasuk di atas dan bawah)
            for j in range(n):
                if j != i:
                    factor = current_matrix[j, i]
                    if abs(factor) > 1e-10:  # Hanya tampilkan jika perubahan signifikan
                        current_matrix[j] = current_matrix[j] - factor * current_matrix[i]
                        
                        # Tentukan notasi operasi baris
                        if factor > 0:
                            op_symbol = f" - {abs(factor):.2f}×"
                        else:
                            op_symbol = f" + {abs(factor):.2f}×"
                        
                        steps.append((f"Eliminasi Baris {j+1}", current_matrix.copy(), 
                                    f"R_{j+1} → R_{j+1}{op_symbol}R_{i+1} (Membuat a_{j+1}{i+1} = 0)"))
        
        # Ekstrak solusi
        solution = current_matrix[:, -1]
        
        # Langkah akhir: solusi
        steps.append(("Solusi Final", current_matrix.copy(), "Matrix dalam Reduced Row Echelon Form (RREF)"))
        
    except Exception as e:
        steps.append((f"ERROR: {str(e)}", None, f"Terjadi error: {str(e)}"))
    
    return solution, steps

def format_number(value):
    """Format angka: hilangkan koma jika bilangan bulat"""
    if abs(value - round(value)) < 1e-10:
        return str(int(round(value)))
    else:
        return f"{value:.6f}".rstrip('0').rstrip('.')

def format_matrix_step(step_title, matrix, explanation, decimals=2):
    """Format langkah untuk ditampilkan dengan penjelasan detail"""
    st.write(f"### 🔹 {step_title}")
    st.info(f"**Penjelasan:** {explanation}")
    
    if matrix is None:
        return
    
    n = matrix.shape[1] - 1  # Jumlah variabel
    
    # Buat DataFrame untuk tampilan yang rapi dengan subscript
    columns = [f"x{i+1}" for i in range(n)] + ['b']
    
    # Format angka dalam matrix
    formatted_data = []
    for i in range(matrix.shape[0]):
        row = []
        for j in range(matrix.shape[1]):
            row.append(format_number(matrix[i, j]))
        formatted_data.append(row)
    
    df = pd.DataFrame(formatted_data, columns=columns)
    
    st.write("**Matrix:**")
    st.dataframe(df, use_container_width=True)
    
    # Tampilkan dalam format LaTeX
    st.write("**Format LaTeX:**")
    latex_str = r"\begin{bmatrix}"
    for i in range(matrix.shape[0]):
        row = " & ".join([format_number(x) for x in matrix[i]])
        latex_str += row
        if i < matrix.shape[0] - 1:
            latex_str += r" \\ "
    latex_str += r"\end{bmatrix}"
    
    st.latex(latex_str)
    st.write("---")

def create_animated_title():
    """Membuat judul dengan efek warna bergerak"""
    # CSS untuk animasi gradient dan styling subscript
    st.markdown("""
    <style>
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .animated-title {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(270deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3);
        background-size: 1200% 1200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 30s ease infinite;
        margin-bottom: 0.5em;
    }
    
    .jordan-text {
        font-size: 1.2em;
        font-weight: bold;
        color: #ff6b6b;
        text-align: center;
        margin-bottom: 2em;
    }
    
    .solution-container {
        background-color: #f0f2f6;
        padding: 1.5em;
        border-radius: 10px;
        margin: 1em 0;
    }
    
    .solution-value {
        font-size: 1.3em;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin: 0.5em 0;
    }
    
    .variable-label {
        font-size: 1.1em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5em;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Judul dengan animasi
    st.markdown('<div class="animated-title">🧮 Kalkulator SPL</div>', unsafe_allow_html=True)
    st.markdown('<div class="jordan-text">Metode Eliminasi <span style="color:#4ecdc4;">Gauss</span>-<span style="color:#ff6b6b;">JORDAN</span></div>', unsafe_allow_html=True)

def main():
    # Judul dengan animasi
    create_animated_title()
    
    st.write("### Solusi Sistem Persamaan Linear $Ax = b$")
    
    # Input ukuran matrix
    st.sidebar.header("⚙️ Konfigurasi Matrix")
    n = st.sidebar.number_input("Ukuran Matrix (n × n)", min_value=2, max_value=6, value=3, step=1)
    
    st.sidebar.markdown("""
    **📋 Petunjuk:**
    1. Masukkan elemen matrix A
    2. Masukkan elemen vektor b  
    3. Klik **'Selesaikan SPL'**
    """)
    
    # Input matrix A
    st.header("📊 Matrix A (Koefisien)")
    st.write(f"Masukkan elemen-elemen matrix A ({n}×{n}):")
    
    # Buat grid input untuk matrix A
    cols = st.columns(n)
    A = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            with cols[j]:
                A[i, j] = st.number_input(
                    f"A[{i+1},{j+1}]",
                    value=1.0 if i == j else 0.0,
                    key=f"A_{i}_{j}",
                    step=0.1,
                    format="%.2f"
                )
    
    # Tampilkan matrix A dalam bentuk yang rapi dengan subscript
    st.write("**Matrix A:**")
    col_labels = [f"x{i+1}" for i in range(n)]
    row_labels = [f"Pers {i+1}" for i in range(n)]
    st.dataframe(pd.DataFrame(A, columns=col_labels, index=row_labels))
    
    # Input vektor b
    st.header("🎯 Vektor b (Konstanta)")
    st.write(f"Masukkan elemen-elemen vektor b ({n}×1):")
    
    b_cols = st.columns(n)
    b = np.zeros(n)
    
    for i in range(n):
        with b_cols[i]:
            b[i] = st.number_input(
                f"b[{i+1}]",
                value=0.0,
                key=f"b_{i}",
                step=0.1,
                format="%.2f"
            )
    
    # Tampilkan vektor b
    st.write("**Vektor b:**")
    st.dataframe(pd.DataFrame(b.reshape(-1, 1), columns=['b'], index=[f"Pers {i+1}" for i in range(n)]))
    
    # Tampilkan sistem persamaan dengan LaTeX untuk subscript
    st.header("📝 Sistem Persamaan Linear")
    for i in range(n):
        equation_parts = []
        for j in range(n):
            coef = A[i, j]
            if abs(coef) > 1e-10:  # Hanya tampilkan koefisien yang signifikan
                if j == 0:
                    if abs(coef - 1.0) < 1e-10:
                        equation_parts.append(f"$x_{{{j+1}}}$")
                    elif abs(coef + 1.0) < 1e-10:
                        equation_parts.append(f"$-x_{{{j+1}}}$")
                    else:
                        equation_parts.append(f"${format_number(coef)}x_{{{j+1}}}$")
                else:
                    sign = "+" if coef >= 0 else "-"
                    coef_abs = abs(coef)
                    if abs(coef_abs - 1.0) < 1e-10:
                        equation_parts.append(f" {sign} $x_{{{j+1}}}$")
                    else:
                        equation_parts.append(f" {sign} ${format_number(coef_abs)}x_{{{j+1}}}$")
        
        equation = "".join(equation_parts) + f" = ${format_number(b[i])}$"
        st.write(f"**({i+1})** {equation}")
    
    # Tombol solve dengan styling
    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🚀 **SELESAIKAN SPL**", type="primary", use_container_width=True):
            st.header("🔍 Proses Penyelesaian")
            st.write("### 📖 Langkah-langkah Eliminasi Gauss-Jordan")
            
            # Validasi input
            det_A = np.linalg.det(A)
            if abs(det_A) < 1e-10:
                st.error("❌ Matrix A singular! Determinan ≈ 0. Sistem tidak memiliki solusi unik.")
                return
            
            # Jalankan eliminasi Gauss-Jordan
            with st.spinner('Menghitung solusi...'):
                solution, steps = gauss_jordan_elimination(A, b)
            
            # Progress bar untuk simulasi proses
            progress_bar = st.progress(0)
            for i, (step_title, step_matrix, explanation) in enumerate(steps):
                format_matrix_step(step_title, step_matrix, explanation)
                progress_bar.progress((i + 1) / len(steps))
            
            # Tampilkan solusi
            if solution is not None:
                st.header("🎉 Solusi Sistem")
                
                # Container untuk solusi
                st.markdown('<div class="solution-container">', unsafe_allow_html=True)
                
                # Tampilkan solusi dalam cards dengan subscript LaTeX
                sol_cols = st.columns(n)
                for i in range(n):
                    with sol_cols[i]:
                        # Gunakan LaTeX untuk subscript
                        st.latex(f"x_{{{i+1}}}")
                        value_display = format_number(solution[i])
                        st.markdown(f'<div class="solution-value">{value_display}</div>', unsafe_allow_html=True)
                        st.caption(f"Variabel {i+1}")
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Verifikasi solusi
                st.subheader("✅ Verifikasi Solusi")
                verification = np.dot(A, solution)
                
                verify_cols = st.columns(2)
                with verify_cols[0]:
                    st.write("**$A × x =$**")
                    verify_data = []
                    for i in range(n):
                        verify_data.append([format_number(verification[i])])
                    st.dataframe(pd.DataFrame(verify_data, columns=['Hasil'], index=[f"Pers {i+1}" for i in range(n)]))
                
                with verify_cols[1]:
                    st.write("**$b =$**")
                    b_data = []
                    for i in range(n):
                        b_data.append([format_number(b[i])])
                    st.dataframe(pd.DataFrame(b_data, columns=['Target'], index=[f"Pers {i+1}" for i in range(n)]))
                
                # Hitung error
                error = np.linalg.norm(verification - b)
                st.write(f"**Error:** ${format_number(error)}$")
                
                if error < 1e-10:
                    st.success("✓ Solusi terverifikasi! Error sangat kecil.")
                else:
                    st.warning("⚠ Solusi memiliki error yang signifikan.")
    
    # Informasi tentang metode
    with st.expander("ℹ️ Tentang Metode Eliminasi Gauss-Jordan"):
        st.markdown("""
        **Eliminasi Gauss-Jordan** adalah metode untuk menyelesaikan Sistem Persamaan Linear (SPL) 
        dengan mengubah matrix augmented menjadi **Reduced Row Echelon Form (RREF)**.
        
        **Langkah-langkah:**
        1. **Pivoting** - Memilih elemen diagonal terbesar untuk stabilitas numerik
        2. **Normalisasi** - Membuat elemen diagonal menjadi 1
        3. **Eliminasi** - Membuat semua elemen di atas dan bawah diagonal menjadi 0
        
        **Notasi Operasi Baris:**
        - $R_i ↔ R_j$ : Menukar baris i dan j
        - $R_i → R_i / k$ : Membagi baris i dengan konstanta k
        - $R_i → R_i - k × R_j$ : Mengurangi baris i dengan k kali baris j
        
        **Keunggulan:**
        - Menghasilkan solusi langsung
        - Dapat digunakan untuk mencari inverse matrix
        - Mudah diimplementasikan secara komputasi
        """)

if __name__ == "__main__":
    main()