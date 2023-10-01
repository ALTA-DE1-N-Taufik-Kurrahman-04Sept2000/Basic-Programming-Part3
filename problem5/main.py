def pangkat(base, pangkat):
  # inisialisasi hasil
  result = 1
  # perulangan
  for i in range(pangkat):
    # kalikan hasil dengan base
    result = result * base
  # kembalikan hasil
  return result

if __name__ == '__main__':
    print(pangkat(2, 3)) # 8
    print(pangkat(5, 3)) # 125
    print(pangkat(10, 2)) # 100
    print(pangkat(2, 5)) # 32
    print(pangkat(7, 3)) # 343