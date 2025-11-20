val = 0xCAFE

lsb4 = val & 0xF              
three_on = bin(lsb4).count("1") >= 3
print("3+ LSB bits ON:", three_on)

rev_bytes = ((val & 0xFF) << 8) | (val >> 8)
print("Reversed bytes:", hex(rev_bytes))

rot4 = ((val >> 4) | (val << 12)) & 0xFFFF
print("4-bit rotate:", hex(rot4))
