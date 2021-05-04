def cube(number):
    try:
        return number ** 3
    except Exception:
        return None

# print("The cube of entered is: ", cube(number= float(input(" Specify a value for cube : "))))