# USGS earthquake feed import
# ---------------------------
# Fetches the "all earthquakes, past day" GeoJSON feed,
# converts the features list to a Pandas DataFrame,
# filters events with magnitude > 4, and prints a summary.

import requests
import pandas as pd

URL = ("https://earthquake.usgs.gov/earthquakes/feed/v1.0/"
       "summary/all_day.geojson")

# 1. Robust HTTP call with timeout and error handling
# ---------------------------------------------------
try:
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
except requests.exceptions.Timeout:
    raise SystemExit("USGS server too slow (timeout)")
except requests.exceptions.ConnectionError:
    raise SystemExit("No network or USGS unreachable")
except requests.exceptions.HTTPError as e:
    raise SystemExit(f"HTTP error: {e.response.status_code}")

payload = resp.json()
features = payload["features"]
print(f"Retrieved {len(features)} events.")

# 2. Flatten the GeoJSON into a clean DataFrame
# ---------------------------------------------
rows = []
for f in features:
    p = f["properties"]
    lon, lat, depth = f["geometry"]["coordinates"]
    rows.append({
        "time":  pd.to_datetime(p["time"], unit="ms"),
        "place": p["place"],
        "mag":   p["mag"],
        "depth_km": depth,
        "lon":   lon,
        "lat":   lat,
    })
df = pd.DataFrame(rows)

# 3. Filter and rank significant events
# -------------------------------------
strong = df[df["mag"] > 4.0].sort_values("mag", ascending=False)
print(f"\n{len(strong)} events with M > 4.0 in the past day:")
print(strong.head(10)[["time", "mag", "depth_km", "place"]]
                .to_string(index=False))

# 4. Quick statistics
# -------------------
print(f"\nMean magnitude (all events) : {df['mag'].mean():.2f}")
print(f"Max magnitude               : {df['mag'].max():.2f}")
print(f"Mean depth                  : {df['depth_km'].mean():.1f} km")
