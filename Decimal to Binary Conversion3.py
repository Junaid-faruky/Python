# 12. Decimal to Binary Conversion
def dec_to_bin(n):
    return bin(n).replace("0b", "")

print(dec_to_bin(25))
