import math

# Exercise 81:
def main():
    side_1 = float(input("Enter the length of the first side: "))
    side_2 = float(input("Enter the length of the second side: "))
    
    hypotenuse = calc_hypotenuse(side_1, side_2)

    print(f"The length of the hypotenuse is: {hypotenuse} units.")


def calc_hypotenuse(side_1: float, side_2: float):
    return math.sqrt((side_1 ** 2) + (side_2 ** 2))


if __name__ == "__main__":
    main()


# Exercise 82:
def main():
    kilometres = float(input("Enter the distance travelled (km): "))
    metres = kilometres * 1000
    total_fare = calc_total_fare(metres)

    print(f"The total fare is ${total_fare}.")

def calc_total_fare(metres: float):
    return 4 + ((metres / 140) * 0.25)

if __name__ == "__main__":
    main()


# Exercise 83:
def main():
    num_of_items = int(input("Enter the number of items ordered: "))
    shipping_charge = calc_shipping_charge(num_of_items)

    print(f"The shipping charge is: ${shipping_charge}")

def calc_shipping_charge(num_of_items: int):
    if num_of_items < 1:
        return 0
    else:
        return 10.95 + (2.95 * (num_of_items - 1))

if __name__ == "__main__":
    main()


# Exercise 84:
def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    median = median_three(a, b, c)

    print(f"The median of the three numbers is: {median}")

def median_three(a: float, b: float, c: float):
    if b < a and c > a or b > a and c < a:
        return a
    elif a < b and c > b or a > b and c < b:
        return b
    else:
        return c

if __name__ == "__main__":
    main()


# Exercise 85:
def main():
    int_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    for i in int_range:
        integer = int_range[i - 1]
        ordinal_num = convert_int(integer)
        print(ordinal_num)

def convert_int(integer: int):
    if integer < 1 or integer > 12:
        return ""
    else:
        if integer == 1:
            return "first"
        elif integer == 2:
            return "second"
        elif integer == 3:
            return "third"
        elif integer == 4:
            return "fourth"
        elif integer == 5:
            return "fifth"
        elif integer == 6:
            return "sixth"
        elif integer == 7:
            return "seventh"
        elif integer == 8:
            return "eighth"
        elif integer == 9:
            return "ninth"
        elif integer == 10:
            return "tenth"
        elif integer == 11:
            return "eleventh"
        elif integer == 12:
            return "twelfth"

if __name__ == "__main__":
    main()
