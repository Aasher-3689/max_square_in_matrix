try:
    from colorama  import Fore
except ImportError:
    print("⚠️ Colorama is not installed! Install it using: pip install colorama")

# Question----

"""
A farmer wants to farm their land with maximum area
where good land is present. The land is represented
as a matrix with ones and zeros where once means good land
and zeros mean Bad land. the farmer only wants to form in a
square of good land with maximum area. please help the
farmer to find the maximum area of the land they can farm in good land.

 EXAMPLE (6 x 5)

 0  1  1  0  1
 1  1  0  1  0
 0  1  1  1  0
 1  1  1  1  0
 1  1  1  1  1
 0  0  0  0  0

 """

# Starting Here----

rows: int  = None
columns: int = None
row_number: int = 1
all_rows_values = []
end_line = "---------------------------"

# compass
def compass():
    compass = ["N", "W", "◯", "E", "S"]
    print(f"{Fore.MAGENTA}COMPASS")
    print(f"   {compass[0]}")
    print(f" {compass[1]} {compass[2]} {compass[3]}")
    print(f"   {compass[4]}")
    print(Fore.RESET)


# collecting no. of rows----
def collecting_total_rows():
    global rows

    compass()

    # giving example of rows
    rows_example = ["*", "*", "*", f"{Fore.RED}<--{Fore.RESET}"]

    for _ in range(3):
        for rows_example_no in rows_example:
            print(f"{rows_example_no}", end="  ")
        print("\n", end="")

    # getting value of rows
    while True:
        rows = input("\nEnter the number of rows of your area: ")
        print(end_line)

        # confirming input is integer
        try:
            rows = int(rows)
            if rows == 0:
                print(f"{Fore.RED}Rows can't not be 0{Fore.RESET}")
            else:
                break
        except ValueError:
            print(f"{Fore.RED}Invalid Number{Fore.RESET}")


# collecting no. of columns----
def collecting_total_columns():
    global columns

    compass()

    # giving example of columns
    columns_example = ["*", "*", "*"]

    print(f"{Fore.RED}⬇  ⬇  ⬇{Fore.RESET}")
    for _ in range(3):
        for columns_example_no in columns_example:
            print(f"{columns_example_no}", end="  ")
        print("\n", end="")

    # getting value of columns
    while True:
        columns = input("\nEnter the number of columns of your area: ")
        print(end_line)

        # confirming input is integer
        try:
            columns = int(columns)
            if columns == 0:
                print(f"{Fore.RED}columns can't not be 0{Fore.RESET}")
            else:
                break
        except ValueError:
            print(f"{Fore.RED}Invalid Number{Fore.RESET}")


# showing area----
def showing_area():

    compass()

    # showing land
    print(f"This is the look of your land ({rows} x {columns}):\n")

    for _ in range(rows):
        for _ in range(columns):
            print("*", end="  ")
        print("\n", end="")

    # story
    print("\nNow each '*' should be replaced by '0' or '1'\n0 --> bad patch of land \n1 --> good patch of land")
    print(end_line)

    # getting permission
    permission_ready = (input("Are you ready? (y): ")).upper()
    if permission_ready == "Y":
        updating_area()
    else:
        showing_area()


# updating area with 0 and 1-----
def updating_area():
    global row_number

    # collecting data of 0 and 1 in
    while row_number <= rows:
        compass()

        print(f"{Fore.RED}Note: {Fore.RESET}Format does not matter! You have to write '0's and '1's of \nasked row number either separated by space or not.\nMixture of 1st '{columns}' 0s and 1s will be automatically collected.\n")

        r_values = input(f"Write values of {Fore.LIGHTYELLOW_EX}Row No. {row_number}: {Fore.RESET}")

        # filtering data
        r_values = [zero_one for zero_one in r_values
                    if zero_one =='0' or zero_one == '1']

        r_values = r_values[0:columns]
        # converting to int
        r_values = [int(item) for item in r_values]

        # putting in list
        if len(r_values) == columns:
            all_rows_values.append(r_values)
            row_number += 1
            print(end_line)

        else:
            print(f"{Fore.LIGHTRED_EX}Row number {row_number} has not sufficient 0s and 1s.\nTry Again{Fore.RESET}")
            print(end_line)


# showing updated area-----
def showing_updated_area():
    compass()

    print(f"\nHere is the updated view of your area.\n0 --> bad patch\n1 --> good patch\n")

    index_showing = 0
    while index_showing < rows:
        for patch_code in all_rows_values[index_showing]:
            print(patch_code, end="  ")
        index_showing += 1
        print("\n", end="")
    print(end_line)

    # final permission to show the largest patch
    final_perm = (input(f"{Fore.LIGHTYELLOW_EX}\nIt's time to see the square of largest combination of good patches (1).\nARE YOU READY? (y): {Fore.RESET}")).upper()
    if final_perm == "Y":
        getting_largest_square_area()
    else:
        showing_updated_area()


# getting the largest square with good area-----
def getting_largest_square_area():
    print(end_line)
    compass()

    max_square_frm_bottm_right = 0
    top_left_loc = []
    dp = [[0]*columns for _ in range(rows)]

    # max square
    for i in range(rows):
        for j in range(columns):
            if all_rows_values[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_square_frm_bottm_right = max(dp[i][j], max_square_frm_bottm_right)

    if max_square_frm_bottm_right == 0:
        return print(f"{Fore.RED}No Good Area found :({Fore.RESET}")

    # location/s
    for k in range(rows):
        for l in range(columns):
            if dp[k][l] == max_square_frm_bottm_right:
                top_left_loc.append([f"Row No: {k-max_square_frm_bottm_right+2}", f"Column No: {l-max_square_frm_bottm_right+2}"])
            else:
                pass

    # plotting Final Area-----
    print(f"{Fore.LIGHTYELLOW_EX}The largest square is: {Fore.LIGHTBLUE_EX}{max_square_frm_bottm_right} x {max_square_frm_bottm_right}")
    print(f"{Fore.LIGHTYELLOW_EX}Top Left Location/s: {Fore.LIGHTBLUE_EX}{top_left_loc}")
    print(f"{Fore.LIGHTYELLOW_EX}\n<<<THANKS FOR TRUSTING US !!>>>{Fore.RESET}")


# Running----
def main():
    collecting_total_columns()
    collecting_total_rows()
    showing_area()
    showing_updated_area()

if __name__ == "__main__":
    main()