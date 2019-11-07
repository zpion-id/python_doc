## Format string


##### Format floats number
```py
f = 9876543210.123456789

print("%.1f"%f) # 9876543210.1
print("%.2f"%f) # 9876543210.12
print("%.3f"%f) # 9876543210.123
print("%.4f"%f) # 9876543210.1235
print("%.5f"%f) # 9876543210.12346
print("%.6f"%f) # 9876543210.123457
print("%.7f"%f) # 9876543210.1234570
print("%.8f"%f) # 9876543210.12345695
print("%.9f"%f) # 9876543210.123456955
print("%6f"%f)  # 9876543210.123457
print("%5f"%f)  # 9876543210.123457
print("%4f"%f)  # 9876543210.123457
print("%3f"%f)  # 9876543210.123457
print("%5.3f"%f) # 9876543210.123
print("%2.1f"%f) # 9876543210.1
print("%1.1f"%f) # 9876543210.1

print("{}".format(f)) # 9876543210.123457
print("{}".format("%.3f"%f)) # 9876543210.123
# tidak direkomendasikan
print("{0:.2}".format(f)) # 9.9e+09
print("{0:.3}".format(f)) # 9.88e+09
print("{0:.4}".format(f)) # 9.877e+09
print("{0:.5}".format(f)) # 9.8765e+09
print("{0:.6}".format(f)) # 9.87654e+09
print("{0:.7}".format(f)) # 9.876543e+09
print("{0:.8}".format(f)) # 9.8765432e+09
print("{0:.9}".format(f)) # 9.87654321e+09
print("{0:.1}".format(f)) # 1e+10

# new metode (direkomendasikan)
print("{:.2}".format(f)) # 9.9e+09
print("{:.3}".format(f)) # 9.88e+09
print("{:.4}".format(f)) # 9.877e+09
print("{:.5}".format(f)) # 9.8765e+09
print("{:.6}".format(f)) # 9.87654e+09
print("{:.7}".format(f)) # 9.876543e+09
print("{:.8}".format(f)) # 9.8765432e+09
print("{:.9}".format(f)) # 9.87654321e+09
print("{:.1}".format(f)) # 1e+10
#print("{1:.1}".format(f)) # IndexError: tuple index out of range
```
