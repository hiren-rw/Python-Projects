# Global Variables :

data = []       # Store 1D or 2D array (list)
is_2d = False       # tells us whether it is a 2D array or not
total = 0       # global summary: total number of elements
avg = 0.0       # global summary: overall average


# FUNCTIONS :
#=========================================================================================

def input_data():
    
    global data, is_2d      # Take a 1D or 2D array and store it.

    print("\nWhich type of array you want to Input?")
    print("1. 1D Array \n2. 2D Array")
    arr_ch = input("Enter Your Choice : ")

    match arr_ch:
        case "1":
            is_2d = False
            text = input("Enter data for a 1D array (separated by spaces) : \n")
            data = [float(val) for val in text.split()]
            print("\nData has been stored successfully!")

        case "2":
            is_2d = True
            data = []
            n = int(input("How many rows? : "))
            for i in range(n):
                text = input(f"Enter row {i + 1} values (separated by spaces) : \n")
                row = [float(val) for val in text.split()]
                data.append(row)
            print("\nData has been stored successfully!")
            show_grid()

        case _:
            print("\nInvalid Choice! Select 1 or 2.")
 

def show_grid():
    """Display the 2D array in a neat, formatted grid."""
    print("\n2D Data Grid : ")
    for row in data:
        line = ""
        for val in row:
            line += f"{val:>8}"
        print(line)


def flatten(lst):
    """Convert a 2D list into a plain 1D list (helper function)."""
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


def get_flat():
    """Return the current data as a flat 1D list, whether it is 1D or 2D."""
    if is_2d:
        return flatten(data)
    return data


def calc_average(lst):
    """User-defined function to calculate the average of a list."""
    return sum(lst) / len(lst)


def find_duplicates(lst):
    """User-defined function to find duplicate values in a list."""
    seen = []
    dupe = []
    for val in lst:
        if val in seen and val not in dupe:
            dupe.append(val)
        else:
            seen.append(val)
    return dupe


def find_unique(lst):
    """User-defined function to find unique values in a list."""
    uniq = []
    for val in lst:
        if val not in uniq:
            uniq.append(val)
    return uniq


def show_extra_values(*args):
    """Accept multiple extra values using *args and display them."""
    print("\nExtra values entered : ", args)
    for val in args:
        print("-", val)


def show_summary_info(**kwargs):
    """Accept dataset details as **kwargs and print them as key-value pairs."""
    print("\nDataset Summary Info : ")
    for key, val in kwargs.items():
        print(f"{key} : {val}")


def display_summary():
    """Show data summary using built-in functions (len, sum, min, max)."""
    global total, avg

    flat = get_flat()
    if not flat:
        print("\nNo data available. Please input data first.")
        return

    total = len(flat)  # built-in function: len()
    total_sum = sum(flat)  # built-in function: sum()
    small = min(flat)  # built-in function: min()
    large = max(flat)  # built-in function: max()
    avg = calc_average(flat)  # user-defined function

    dupe = find_duplicates(flat)  # user-defined function
    uniq = find_unique(flat)  # user-defined function

    print("\nData Summary : ")
    print(f"- Total elements : {total}")
    print(f"- Minimum value : {small}")
    print(f"- Maximum value : {large}")
    print(f"- Sum of all values : {total_sum}")
    print(f"- Average value : {round(avg, 2)}")
    print(f"- Duplicate values : {dupe if dupe else 'None'}")
    print(f"- Unique values : {uniq}")

    show_summary_info(
        total=total, average=round(avg, 2), data_type="2D" if is_2d else "1D"
    )

    text = input("\nEnter a few extra numbers to test *args (separated by spaces) : ")
    nums = [float(val) for val in text.split()] if text.strip() else []
    show_extra_values(*nums)


def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    """Ask user for a number and display its factorial using recursion."""
    n = int(input("\nEnter a number to calculate its factorial : "))
    if n < 0:
        print("\nFactorial is not defined for negative numbers.")
        return
    result = factorial(n)
    print(f"\nFactorial of {n} is : {result}")


def filter_data():
    """Filter data above a threshold using lambda with filter() and map()."""
    flat = get_flat()
    if not flat:
        print("\nNo data available. Please input data first.")
        return

    thr = float(
        input("\nEnter a threshold value to filter out data above this value : ")
    )
    filtered = list(filter(lambda val: val >= thr, flat))  # lambda + filter()
    doubled = list(map(lambda val: val * 2, filtered))  # lambda + map()  # noqa: C417

    print(f"\nFiltered Data (values >= {thr}) : ")
    print(", ".join(str(val) for val in filtered))
    print("Doubled version of filtered data (map demo) : ")
    print(", ".join(str(val) for val in doubled))


def sort_data():
    """Sort 1D list in place using sort(), or sort 2D rows using sorted()."""
    if not data:
        print("\nNo data available. Please input data first.")
        return

    print("\nChoose sorting option : ")
    print("1. Ascending \n2. Descending")
    sort_ch = input("Enter Your Choice : ")

    match sort_ch:
        case "1" | "2":
            reverse = sort_ch == "2"
            order = "Descending" if reverse else "Ascending"

            if is_2d:
                new_rows = sorted(data, reverse=reverse)  # sorted() -> new list
                print(f"\nRows Sorted in {order} Order (original list unchanged) : ")
                for row in new_rows:
                    print(row)
            else:
                data.sort(reverse=reverse)  # sort() -> in place
                print(f"\nSorted Data in {order} Order : ")
                print(", ".join(str(val) for val in data))

        case _:
            print("\nInvalid Choice! Select 1 or 2.")


def get_stats():
    # minimum, maximum and average value.
    flat = get_flat()
    small = min(flat)
    large = max(flat)
    average = calc_average(flat)
    return small, large, average  # returning multiple values


def display_statistics():
    """Show dataset statistics using get_stats() and the global summary values."""
    if not data:
        print("\nNo data available. Please input data first.")
        return

    low, high, average = get_stats()  # unpacking multiple returned values

    print("\nDataset Statistics : ")
    print(f"- Minimum value : {low}")
    print(f"- Maximum value : {high}")
    print(f"- Average value : {round(average, 2)}")
    print(f"- (From global variable) Total elements counted earlier : {total}")
    print(f"- (From global variable) Average stored earlier : {round(avg, 2)}")


def docstrings():

    # Shows the doctstrings of all function using __doc__

    print(f"\n1. Input Data - {input_data.__doc__}")
    print(f"2. Display Data Summary (Built-in Functions) - {display_summary.__doc__}")
    print(f"3. Calculate Factorial (Recursion) - {calculate_factorial.__doc__}")
    print(f"4. Filter Data by Threshold (Lambda Function) - {filter_data.__doc__}")
    print(f"5. Sort Data - {sort_data.__doc__}")
    print(f"6. Display Dataset statistics (Return Multiple Values) - {display_statistics.__doc__}")


# MAIN PROGRAM

print("Welcome to the Data Analyzer and Transformer Program : ")

while True:
    print("\nMain Menu : ")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset statistics (Return Multiple Values)")
    print("7. Show DockStrings")
    print("8. Exit Program")
    ch = input("\nEnter Your Choice : ")

    match ch:
        case "1":       # Input Data
            input_data()

        case "2":       # Display Data Summary (Built-in Functions)
            display_summary()

        case "3":       # Calculate Factorial (recursion)
            calculate_factorial()

        case "4":       # Filter Data by Threshold (Lambda Function)
            filter_data()

        case "5":       # Sort Data
            sort_data()

        case "6":       # Display Dataset statistics (Return Multiple Values)
            display_statistics()

        case "7":
            docstrings()

        case "8":       # Exit Program
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        case _:
            print("\nInvalid Choice! Select from 1 to 7.")
