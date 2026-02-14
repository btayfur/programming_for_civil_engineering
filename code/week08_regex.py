import re # Import the Regex module

# Regular Expressions (Regex)
# ---------------------------
# The "Smart Find" tool. 
# Used when .split() is too complicated because the text is inconsistent.

# Scenario: Extracting error codes from messy logs
log_entry = "Error happened at [Disk-1] with Code: #404 (Timeout)"
print(f"Log: {log_entry}")

# Goal: Find the number "404"
# Naive way (splitting by space) would fail because of "#" or "("

# 1. re.search (Find the first match)
# -----------------------------------
# Pattern: #\d+ 
# #   -> Look for a hashtag
# \d  -> Look for a digit (0-9)
# +   -> Look for ONE or MORE digits
match = re.search(r"#\d+", log_entry)

if match:
    print(f"Found code string: {match.group()}") # Returns "#404"
    # To get just the number, we can slice:
    print(f"Code number: {match.group()[1:]}")   # Returns "404"
else:
    print("No code found.")


# 2. re.findall (Find ALL matches)
# --------------------------------
# Scenario: Extracting beam dimensions from a text
# "Beam A is 300x500 mm and Beam B is 400x600 mm"
text = "Section 1: 300x500mm, Section 2: 25.5x40.0cm"

# Pattern Explanation:
# \d+    -> Digits
# \.?    -> Optional dot (for decimals like 25.5)
# \d*    -> Optional decimals after dot
# x      -> The letter 'x'
pattern = r"\d+\.?\d*x\d+\.?\d*" 

dimensions = re.findall(pattern, text)
print(f"\nText: {text}")
print(f"Found Dimensions: {dimensions}")

# 3. Simple Patterns Guide
# ------------------------
# \d  : Any digit (0-9)
# \w  : Any letter or number (A-Z, 0-9)
# .   : Any character (dot means 'anything')
# +   : One or more
# *   : Zero or more
