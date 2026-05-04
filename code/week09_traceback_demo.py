# Traceback demo: this script is *meant* to crash.
# -------------------------------------------------
# Run it (`python week09_traceback_demo.py`), read the
# traceback, and identify which line is the real bug.

def axial_stress(force, area):
    # Line 8: the actual bug --- 'zero' is never defined.
    return force / area / zero


def report(member_id, force, area):
    sigma = axial_stress(force, area)   # Line 13
    print(f"{member_id}: stress = {sigma:.2f} MPa")


def main():
    members = [
        ("M1", 100, 0.005),
        ("M2", 150, 0.005),
    ]
    for mid, F, A in members:
        report(mid, F, A)               # Line 23


if __name__ == "__main__":
    main()                              # Line 27
