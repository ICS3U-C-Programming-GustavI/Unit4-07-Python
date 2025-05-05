# Author: Gustav Ihlenfeld
# Date: 2025-05-05
# Description:
# This program prints the integers from 1000 to 2000 using
# one for loop and one if statement. It displays five numbers
# per line, with each number separated by a space.


def main():
    # Loop through numbers from 1000 to 2000 (inclusive)
    for i in range(1000, 2001):

        # Print the current number with a space, but don't go to the next line yet
        print(i, end=" ")

        # Check if we've printed 5 numbers on the current line
        if (i - 999) % 5 == 0:
            # Print a newline after every 5 numbers
            print()


# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
