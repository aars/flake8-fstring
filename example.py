amount = "one"  # OK
empty = f""  # FST0001
wrong = f"this does not contain any interpolation"  # FST0001
right = f"but this {amount} does"  # OK
