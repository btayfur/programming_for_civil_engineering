def calculate_integral(x1, x2, *coeffs):
    """
    Calculates the definite integral of a polynomial function between x1 and x2.
    
    The function form depends on the number of coefficients provided:
    1 arg (a)          -> f(x) = ax
    2 args (a, b)      -> f(x) = ax + b
    3 args (a, b, c)   -> f(x) = ax^2 + bx + c
    4 args (a, b, c, d)-> f(x) = ax^3 + bx^2 + cx + d
    5 args (a..e)      -> f(x) = ax^4 + bx^3 + cx^2 + dx + e
    
    Parameters:
    x1 (float): Lower limit of integration.
    x2 (float): Upper limit of integration.
    *coeffs: Coefficients of the polynomial (a, b, c, ...).
    
    Returns:
    float: The value of the definite integral.
    None: If the number of coefficients is not supported.
    """
    
    # Helper function to calculate F(x) (Antiderivative value at x)
    def antiderivative(x, c):
        n = len(c)
        val = 0
        
        # Case 1: f(x) = ax (Special case per instructions)
        if n == 1:
            a = c[0]
            # Integral of ax is (a/2)x^2
            val = (a / 2) * x**2

        # Case 2: Linear f(x) = ax + b
        elif n == 2:
            a, b = c
            val = (a / 2) * x**2 + b * x
            
        # Case 3: Quadratic f(x) = ax^2 + bx + c
        elif n == 3:
            a, b, c_const = c
            # Integral: (a/3)x^3 + (b/2)x^2 + cx
            val = (a / 3) * x**3 + (b / 2) * x**2 + c_const * x
            
        # Case 4: Cubic f(x) = ax^3 + bx^2 + cx + d
        elif n == 4:
            a, b, c_const, d = c
            val = (a / 4) * x**4 + (b / 3) * x**3 + (c_const / 2) * x**2 + d * x
            
        # Case 5: Quartic f(x) = ax^4 + ... + e
        elif n == 5:
            a, b, c_const, d, e = c
            val = (a / 5) * x**5 + (b / 4) * x**4 + (c_const / 3) * x**3 + (d / 2) * x**2 + e * x
            
        else:
            raise ValueError(f"Unsupported number of coefficients: {n}. Please provide 1 to 5 coefficients.")
            
        return val

    try:
        # Calculate F(x2) - F(x1)
        # We pass 'coeffs' tuple to our inner helper function
        result = antiderivative(x2, coeffs) - antiderivative(x1, coeffs)
        return result

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError:
        print("Error: Inputs must be numbers.")
        return None

# Main Execution Block
# --------------------
if __name__ == "__main__":
    print("--- Integral Calculator ---")
    
    # 1. Linear Special: f(x) = 5x, from 0 to 10
    res1 = calculate_integral(0, 10, 5)
    print(f"Integral of 5x (0 to 10): {res1}")

    # 2. Linear Standard: f(x) = 2x + 3, from 0 to 5
    # Integral = x^2 + 3x = (25+15) - 0 = 40
    res_lin = calculate_integral(0, 5, 2, 3)
    print(f"Integral of 2x + 3 (0 to 5): {res_lin}")
    
    # 3. Quadratic: f(x) = 1x^2 + 0x + 0, from 0 to 3
    res2 = calculate_integral(0, 3, 1, 0, 0)
    print(f"Integral of x^2 (0 to 3): {res2}")
    
    # 4. Error Case (Unsupported length, e.g., 6 coefficients)
    print("\n--- Testing Error Handling ---")
    calculate_integral(0, 5, 1, 2, 3, 4, 5, 6) # Should print error


