# Same value, different bytes
# ---------------------------
# Demonstrates how Python stores the "same" value (5) in
# different types, and how many bytes each one consumes.

import sys

# 1. Four versions of "five"
# --------------------------
five_int   = 5
five_float = 5.0
five_str   = "5"
five_bool  = True       # True == 1; not literally five but useful here

# 2. Show the bit pattern (where it makes sense)
# ----------------------------------------------
# bin() returns the binary representation of an integer.
# zfill(8) pads to 8 bits so the byte boundary is visible.
print(f"int   5 -> {bin(five_int)[2:].zfill(8)}")
print(f"str   '5' -> char code {ord(five_str)} -> "
      f"{bin(ord(five_str))[2:].zfill(8)}")
print(f"bool  True -> {bin(five_bool)[2:].zfill(8)}")

# float bits require a separate trick (struct module)
import struct
float_bits = struct.pack('!f', five_float)
print(f"float 5.0 -> {float_bits.hex()}  (4 bytes, IEEE 754 sf32)")

# 3. Memory footprint with sys.getsizeof
# --------------------------------------
print("-" * 40)
print(f"sys.getsizeof(5)    = {sys.getsizeof(five_int)} bytes")
print(f"sys.getsizeof(5.0)  = {sys.getsizeof(five_float)} bytes")
print(f"sys.getsizeof('5')  = {sys.getsizeof(five_str)} bytes")
print(f"sys.getsizeof(True) = {sys.getsizeof(five_bool)} bytes")

# 4. The classic float surprise
# -----------------------------
print("-" * 40)
print(f"0.1 + 0.2 == 0.3 ?  {0.1 + 0.2 == 0.3}")
print(f"actual value      :  {0.1 + 0.2!r}")
