# Switch Statements (match-case)
# ------------------------------
# Introduced in Python 3.10, 'match-case' is the powerful equivalent
# of 'switch' statements in C/C++/Java.
# It is used when comparing a variable against a list of specific values.

# Example: Get the Partial Safety Factor (gamma) for different load types
# based on Eurocode / Local Standards.

load_type = input("Enter the load type (D, L, W, E): ")

gamma = 0.0
description = ""

match load_type:
    case "D":
        description = "Dead Load"
        gamma = 1.4 # or 1.35 per EC
    case "L":
        description = "Live Load"
        gamma = 1.6 # or 1.5 per EC
    case "W":
        description = "Wind Load"
        gamma = 1.0 # factor varies by combination, simplified here
    case "E":
        description = "Earthquake Load"
        gamma = 1.0
    case _:
        # The underscore (_) acts as a default/catch-all case
        description = "Unknown Load Type"
        gamma = 1.0

print("-" * 30)
print(f"Load: {description}")
print(f"Partial Safety Factor (gamma): {gamma}")
print("-" * 30)
