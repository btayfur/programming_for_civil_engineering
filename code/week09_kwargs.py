# Beam design check with **kwargs and type hints
# -----------------------------------------------
# Demonstrates: type hints, default arguments, **kwargs,
# raising domain-specific errors, and the __main__ guard.


class StressExceedsYieldError(Exception):
    """Raised when computed stress exceeds material yield strength."""


def beam_design_check(
    force: float,
    area: float,
    yield_strength: float = 250.0,
    **opts,
) -> dict:
    """Verify axial stress against yield, with optional safety factor.

    Extra options accepted via **opts:
      safety_factor : float, default 1.5
      material      : str,   default "steel"
    """
    sf       = opts.get("safety_factor", 1.5)
    material = opts.get("material", "steel")

    if area <= 0:
        raise ValueError("area must be positive")

    sigma = force / area
    allowable = yield_strength / sf

    if sigma > yield_strength:
        raise StressExceedsYieldError(
            f"sigma={sigma:.1f} > F_y={yield_strength}"
        )

    return {
        "material": material,
        "stress": sigma,
        "allowable": allowable,
        "passes": sigma <= allowable,
    }


if __name__ == "__main__":
    # Force in N, area in mm^2, yield_strength in MPa (= N/mm^2)
    result = beam_design_check(force=15000, area=100,
                                yield_strength=275,
                                safety_factor=1.5,
                                material="S275 steel")
    print(result)
    # sigma = 15000 / 100 = 150 MPa < 275 -> passes
