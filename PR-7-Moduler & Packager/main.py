"""Module & Packager: a beginner-friendly multi-utility toolkit."""

import datetime
import math
import random
import time
import uuid

from toolkit import file_utils, math_utils

LOG_FILE = "toolkit_log.txt"


def save_log(message):
    """Store an operation's result or error using our custom file module."""
    try:
        file_utils.append_file(LOG_FILE, message + "\n")
    except OSError as error:
        print(f"Could not save log: {error}")


def show_result(message, log=True):
    """Display a result and usually save it to a text log."""
    print(message)
    if log:
        save_log(message)


def positive_integer(prompt):
    """Ask for a whole number greater than zero."""
    value = int(input(prompt))
    if value <= 0:
        raise ValueError("Enter a positive whole number.")
    return value


def get_number(prompt, minimum=None):
    """Read a finite number, optionally requiring a minimum value."""
    value = float(input(prompt))
    if not math.isfinite(value) or (minimum is not None and value < minimum):
        raise ValueError("Enter a valid number in the requested range.")
    return value


def clock_minutes(text):
    """Convert HH:MM clock time into minutes after midnight."""
    clock = time.strptime(text, "%H:%M")
    return clock.tm_hour * 60 + clock.tm_min


def elapsed_clock_minutes(start, end):
    """Treat an earlier end time as the following day (overnight)."""
    return (clock_minutes(end) - clock_minutes(start)) % (24 * 60)


def datetime_menu():
    while True:
        print("""
Datetime and Time Operations
1. Display Current Date and Time
2. Difference Between Two Dates or Times
3. Format a Date (strftime)
4. Stopwatch
5. Countdown Timer
6. Calculate Working Hours
7. Back to Main Menu""")
        choice = input("Enter your choice: ").strip()
        try:
            match choice:
                case "1":
                    now = datetime.datetime.now()
                    show_result("Current Date and Time: " + now.strftime("%Y-%m-%d %H:%M:%S"))
                case "2":
                    kind = input("1. Dates  2. Times: ").strip()
                    match kind:
                        case "1":
                            first = datetime.datetime.strptime(input("First date (YYYY-MM-DD): "), "%Y-%m-%d")
                            second = datetime.datetime.strptime(input("Second date (YYYY-MM-DD): "), "%Y-%m-%d")
                            show_result(f"Difference: {abs((second - first).days)} day(s)")
                        case "2":
                            print("If the second time is earlier, it means the next day.")
                            first = input("First time (HH:MM): ")
                            second = input("Second time (HH:MM): ")
                            minutes = elapsed_clock_minutes(first, second)
                            show_result(f"Difference: {minutes // 60} hour(s), {minutes % 60} minute(s)")
                        case _:
                            show_result("Invalid option.")
                case "3":
                    date = datetime.datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d")
                    print("Example formats: %d/%m/%Y or %B %d, %Y")
                    format_text = input("Enter format: ")
                    if not format_text:
                        raise ValueError("Format cannot be empty.")
                    show_result("Formatted Date: " + date.strftime(format_text))
                case "4":
                    input("Press Enter to start stopwatch...")
                    start = time.perf_counter()
                    input("Press Enter to stop stopwatch...")
                    show_result(f"Elapsed Time: {time.perf_counter() - start:.2f} seconds")
                case "5":
                    seconds = positive_integer("Countdown seconds: ")
                    for remaining in range(seconds, 0, -1):
                        show_result(f"Time remaining: {remaining} second(s)")
                        time.sleep(1)
                    show_result("Countdown completed!")
                case "6":
                    print("Use 24-hour time. Overnight shifts are supported.")
                    first = input("Start time (HH:MM): ")
                    second = input("End time (HH:MM): ")
                    minutes = elapsed_clock_minutes(first, second)
                    show_result(f"Working Hours: {minutes // 60} hour(s), {minutes % 60} minute(s)")
                case "7":
                    return
                case _:
                    show_result("Invalid choice. Try again.")
        except (ValueError, OverflowError) as error:
            show_result(f"Invalid input: {error}")


def math_menu():
    while True:
        print("""
Mathematical Operations
1. Arithmetic (+, -, *, /)
2. Factorial
3. Compound Interest
4. Trigonometry (sin, cos, tan)
5. Logarithm
6. Area of Geometric Shapes
7. Unit Conversions (Custom Module)
8. Back to Main Menu""")
        choice = input("Enter your choice: ").strip()
        try:
            match choice:
                case "1":
                    first = get_number("First number: ")
                    operator = input("Operator (+, -, *, /): ").strip()
                    second = get_number("Second number: ")
                    match operator:
                        case "+": answer = first + second
                        case "-": answer = first - second
                        case "*": answer = first * second
                        case "/": answer = first / second
                        case _:
                            show_result("Invalid operator.")
                            continue
                    if not math.isfinite(answer):
                        raise ValueError("Result is too large.")
                    show_result(f"Result: {answer:.2f}")
                case "2":
                    number = int(input("Enter a non-negative whole number: "))
                    if number < 0:
                        raise ValueError("Factorial requires a non-negative integer.")
                    show_result(f"Factorial: {math.factorial(number)}")
                case "3":
                    principal = get_number("Principal amount: ", minimum=0)
                    rate = get_number("Annual interest rate (%): ", minimum=0)
                    years = get_number("Time in years: ", minimum=0)
                    amount = principal * (1 + rate / 100) ** years
                    if not math.isfinite(amount):
                        raise ValueError("Result is too large.")
                    show_result(f"Final Amount: {amount:.2f} | Interest Earned: {amount - principal:.2f}")
                case "4":
                    degrees = get_number("Angle in degrees: ")
                    angle = math.radians(degrees)
                    sine, cosine = math.sin(angle), math.cos(angle)
                    tangent = "undefined" if abs(cosine) < 1e-10 else f"{math.tan(angle):.4f}"
                    show_result(f"sin: {sine:.4f} | cos: {cosine:.4f} | tan: {tangent}")
                case "5":
                    number = get_number("Positive number: ")
                    base = get_number("Logarithm base (e.g., 10): ")
                    show_result(f"Logarithm: {math.log(number, base):.4f}")
                case "6":
                    shape = input("1. Circle  2. Rectangle  3. Triangle: ").strip()
                    match shape:
                        case "1":
                            radius = get_number("Radius: ", minimum=0)
                            area = math.pi * radius ** 2
                        case "2":
                            length = get_number("Length: ", minimum=0)
                            width = get_number("Width: ", minimum=0)
                            area = length * width
                        case "3":
                            base = get_number("Base: ", minimum=0)
                            height = get_number("Height: ", minimum=0)
                            area = base * height / 2
                        case _:
                            show_result("Invalid shape.")
                            continue
                    if not math.isfinite(area):
                        raise ValueError("Result is too large.")
                    show_result(f"Area: {area:.2f} square units")
                case "7":
                    conversion = input("1. Kilometers to Miles  2. Celsius to Fahrenheit: ").strip()
                    match conversion:
                        case "1":
                            km = get_number("Kilometers: ", minimum=0)
                            miles = math_utils.km_to_miles(km)
                            if not math.isfinite(miles):
                                raise ValueError("Result is too large.")
                            show_result(f"Miles: {miles:.2f}")
                        case "2":
                            celsius = get_number("Celsius: ")
                            fahrenheit = math_utils.celsius_to_fahrenheit(celsius)
                            if not math.isfinite(fahrenheit):
                                raise ValueError("Result is too large.")
                            show_result(f"Fahrenheit: {fahrenheit:.2f}")
                        case _:
                            show_result("Invalid option.")
                case "8":
                    return
                case _:
                    show_result("Invalid choice. Try again.")
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            show_result(f"Invalid input: {error}")


def random_menu():
    # SystemRandom comes from random and is appropriate for passwords and OTPs.
    secure_random = random.SystemRandom()
    while True:
        print("""
Random Data Generation
1. Generate Random Number
2. Generate Random List
3. Generate Random Password
4. Generate Random OTP
5. Sample Items from a Dataset
6. Dice Guessing Game
7. Back to Main Menu""")
        choice = input("Enter your choice: ").strip()
        try:
            match choice:
                case "1":
                    low = int(input("Minimum: "))
                    high = int(input("Maximum: "))
                    show_result(f"Random Number: {random.randint(low, high)}")
                case "2":
                    count = positive_integer("How many numbers? ")
                    low = int(input("Minimum: "))
                    high = int(input("Maximum: "))
                    numbers = [random.randint(low, high) for _ in range(count)]
                    show_result(f"Random List: {numbers}")
                case "3":
                    length = positive_integer("Password length: ")
                    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
                    password = "".join(secure_random.choice(characters) for _ in range(length))
                    show_result("Generated Password: " + password, log=False)
                    save_log("Password generated (password not saved for privacy).")
                case "4":
                    length = positive_integer("OTP length: ")
                    otp = "".join(str(secure_random.randint(0, 9)) for _ in range(length))
                    show_result("Generated OTP: " + otp, log=False)
                    save_log("OTP generated (OTP not saved for privacy).")
                case "5":
                    dataset = [item.strip() for item in input("Items separated by commas: ").split(",") if item.strip()]
                    count = positive_integer("How many items to sample? ")
                    if count > len(dataset):
                        raise ValueError("Sample size cannot exceed number of items.")
                    show_result("Random Sample: " + ", ".join(random.sample(dataset, count)))
                case "6":
                    guess = int(input("Guess the dice roll (1-6): "))
                    if guess < 1 or guess > 6:
                        raise ValueError("Guess must be from 1 to 6.")
                    rolled = random.randint(1, 6)
                    result = "You win!" if guess == rolled else "Try again!"
                    show_result(f"Your guess: {guess} | Dice rolled: {rolled} | {result}")
                case "7":
                    return
                case _:
                    show_result("Invalid choice. Try again.")
        except ValueError as error:
            show_result(f"Invalid input: {error}")


def uuid_menu():
    while True:
        print("""
Generate Unique Identifiers (UUID4)
1. File Identifier
2. Record / Invoice Identifier
3. User Session Identifier
4. Back to Main Menu""")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1": show_result(f"File UUID4: {uuid.uuid4()}")
            case "2": show_result(f"Record UUID4: {uuid.uuid4()}")
            case "3": show_result(f"Session UUID4: {uuid.uuid4()}")
            case "4": return
            case _: show_result("Invalid choice. Try again.")


def file_menu():
    while True:
        print("""
File Operations (Custom Module)
1. Create a New File
2. Write / Replace File Content
3. Read a File
4. Append / Update a File
5. Back to Main Menu""")
        choice = input("Enter your choice: ").strip()
        if choice == "5":
            return
        if choice not in ("1", "2", "3", "4"):
            show_result("Invalid choice. Try again.")
            continue
        filename = input("Enter file name (e.g., notes.txt): ").strip()
        if not filename:
            show_result("File name cannot be empty.")
            continue
        if filename == LOG_FILE:
            show_result("This filename is reserved for the toolkit log.")
            continue
        try:
            match choice:
                case "1":
                    file_utils.create_file(filename)
                    show_result(f"File created: {filename}")
                case "2":
                    content = input("Enter text to write: ")
                    file_utils.write_file(filename, content + "\n")
                    show_result(f"Data written to: {filename}")
                case "3":
                    content = file_utils.read_file(filename)
                    show_result(f"File Content ({filename}):\n{content}")
                case "4":
                    content = input("Enter text to append: ")
                    file_utils.append_file(filename, content + "\n")
                    show_result(f"Data appended to: {filename}")
        except (OSError, UnicodeError, ValueError) as error:
            show_result(f"File error: {error}")


def explore_menu():
    """Inspect any importable standard or custom module using dir()."""
    print("Examples: datetime, time, math, random, uuid, toolkit.file_utils, toolkit.math_utils")
    name = input("Module name to explore: ").strip()
    if not name:
        show_result("Module name cannot be empty.")
        return
    try:
        # __import__ dynamically loads a module named by the user.
        module = __import__(name, fromlist=["*"])
        show_result(f"Available attributes of {name}:\n" + ", ".join(dir(module)))
    except (ImportError, ValueError) as error:
        show_result(f"Cannot explore module: {error}")


def main():
    while True:
        print("""
==============================
 Welcome to Multi-Utility Toolkit
==============================
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
==============================""")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1": datetime_menu()
            case "2": math_menu()
            case "3": random_menu()
            case "4": uuid_menu()
            case "5": file_menu()
            case "6": explore_menu()
            case "7":
                show_result("Thank you for using the Multi-Utility Toolkit!")
                break
            case _:
                show_result("Invalid choice. Try again.")


if __name__ == "__main__":
    main()