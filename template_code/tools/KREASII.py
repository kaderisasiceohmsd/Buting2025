import random

# --- Membuat papan Sudoku ---
def print_board(board):
    print("\n================ Sudoku ================\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 33)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if board[i][j] == 0:
                print(". ", end="")
            else:
                print(str(board[i][j]) + " ", end="")
        print()
    print()

def is_valid(board, row, col, num):
    # Cek baris
    if num in board[row]:
        return False

    # Cek kolom
    for i in range(9):
        if board[i][col] == num:
            return False

    # Cek kotak 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # baris, kolom
    return None

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, row, col, i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# --- Puzzle awal (bisa diganti) ---
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# --- Game loop ---
while True:
    print_board(board)
    empty = find_empty(board)
    if not empty:
        print("🎉 Selamat! Kamu menyelesaikan Sudoku!")
        break

    print("Masukkan langkah (baris kolom angka), contoh: 1 3 9")
    print("Ketik '0 0 0' untuk keluar.")
    try:
        row, col, num = map(int, input("Langkahmu: ").split())
        if (row, col, num) == (0, 0, 0):
            print("Keluar dari permainan.")
            break

        row -= 1
        col -= 1

        if board[row][col] != 0:
            print("❌ Kotak ini sudah terisi!")
        elif not (1 <= num <= 9):
            print("❌ Angka harus 1-9!")
        elif is_valid(board, row, col, num):
            board[row][col] = num
            print("✅ Langkah valid!\n")
        else:
            print("⚠️ Angka itu tidak valid di posisi ini!\n")

    except ValueError:
        print("⚠️ Input tidak valid. Gunakan format: baris kolom angka.")
    except IndexError:
        print("⚠️ Baris/kolom di luar jangkauan (1-9).")