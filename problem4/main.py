def palindrome(input_string):
  # Ubah string menjadi huruf kecil
  input_string = input_string.lower()
  # Hapus spasi dan tanda baca jika ada
  input_string = "".join(c for c in input_string if c.isalnum())
  # Bandingkan string dengan kebalikannya
  return input_string == input_string[::-1]


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False