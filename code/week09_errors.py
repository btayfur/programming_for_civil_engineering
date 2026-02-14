# Error Handling (Try-Except)
# -----------------------------
# Analogy: "The Safety Net". 
# If a trapeze artist falls (Error occurs), the net catches them (Except block), 
# so the show doesn't stop (Program doesn't crash).

def safe_division(load, area):
    try:
        stress = load / area
        return stress
    except ZeroDivisionError:
        print("CRITICAL ERROR: Area cannot be zero! Infinite stress!")
        return None
    except TypeError:
        print("ERROR: Please input numbers, not text!")
        return None

# Test 1: Normal
print(f"Test 1: {safe_division(100, 10)}")

# Test 2: Zero Area (Would normally crash the program)
print(f"Test 2: {safe_division(100, 0)}")

# Test 3: Wrong Input
print(f"Test 3: {safe_division(100, 'ten')}")

print("\nProgram continued running successfully after errors!")
