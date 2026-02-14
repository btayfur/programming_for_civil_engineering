# For Loops
# ---------
# Iterate over a known sequence or range.

# Example 1: Summing loads acting on a beam
point_loads = [10.5, 20.0, 5.0, 15.0] # kN
total_load = 0.0

print("Calculating Total Load...")
for load in point_loads:
    print(f"Adding load: {load} kN")
    total_load += load

print(f"Total Point Load: {total_load} kN")
print("-" * 30)

# Example 2: Iterating with an index using range()
# Calculating moment at specific intervals
# Moment M(x) = w * x^2 / 2 (Cantilever under dist. load)
w = 10.0 # kN/m
length = 5.0 # m
steps = 6 # 0, 1, 2, 3, 4, 5

print("Moment Distribution along Cantilever:")
for x in range(steps):
    moment = (w * x**2) / 2
    print(f"Distance x={x}m -> Moment={moment} kNm")
