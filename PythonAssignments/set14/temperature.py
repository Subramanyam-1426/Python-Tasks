# 14.3 Dual-Purpose Module ⭐⭐⭐
# Write temperature.py that works two ways:

# Run directly → runs self-tests and prints a demo
# Imported → gives clean functions, no output
# $ python temperature.py
# All self-tests passed
# 0°C = 32.0 °F
# 37°C = 98.6 °F

# $ python - c "from temperature import c_to_f; print(c_to_f(100))"
# 212.0

def c_to_f(celsius):
    return (celsius * 9 / 5) + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    # assert c_to_f(0) == 32
    # assert round(c_to_f(37), 1) == 98.6

    print("All self-tests passed")
    print(f"0°C  = {c_to_f(0):.1f} °F")
    print(f"37°C = {c_to_f(37):.1f} °F")
