# JSON sensor log: read, filter, write back
# -----------------------------------------
# Demonstrates json.load, list-comprehension filter,
# and json.dump with pretty-printing.

import json
from pathlib import Path

# 1. Sample data -- in real life this would be an existing file.
# --------------------------------------------------------------
sample = {
    "site": "Bridge-A",
    "readings": [
        {"t": "08:00", "deflection_mm": 1.2, "temp_C": 18},
        {"t": "12:00", "deflection_mm": 4.8, "temp_C": 28},
        {"t": "16:00", "deflection_mm": 6.7, "temp_C": 31},
        {"t": "20:00", "deflection_mm": 2.1, "temp_C": 22},
    ],
}

src = Path("readings.json")
src.write_text(json.dumps(sample, indent=2))

# 2. Read JSON -> Python dict
# ---------------------------
with open(src) as f:
    log = json.load(f)

# 3. Filter high-deflection events
# --------------------------------
THRESHOLD_MM = 4.0
high_events = [r for r in log["readings"]
               if r["deflection_mm"] > THRESHOLD_MM]

print(f"{len(high_events)} reading(s) above {THRESHOLD_MM} mm:")
for ev in high_events:
    print(f"  {ev['t']}  -> {ev['deflection_mm']} mm")

# 4. Write filtered subset back as JSON
# -------------------------------------
out = Path("alarms.json")
with open(out, "w") as f:
    json.dump({"site": log["site"], "alarms": high_events}, f, indent=2)
print(f"Wrote {out.resolve()}")
