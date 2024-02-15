# A function that returns True if one of its inputs is the square of the other one, 
# and False otherwise. Sample runs would be as follows.

# print(is_square(3,2))
## False

# print(is_square(2,3))
## False

# print(is_square(2,2))
## False

# print(is_square(2,4))
## True

# print(is_square(9,3))
## True

class SquareCalc:
    
    # make sure we can instantiate itselt here for the square method
    def is_square(self, numOne, numTwo):
        return numOne == numTwo**2 or numTwo == numOne**2

    # create a new method to validate user input and ensure it's accepting 2 valid integers
    def get_user_input(self):
        while True:
            try:
                numOne = int(input("Please enter a number (whole number) for initial value: "))
                break  # Exit the loop if successfully converted to int
            except ValueError:
                print("Please enter a valid integer.")

        while True:
            try:
                numTwo = int(input("Please enter a number (whole number)  for the comparison of square: "))
                break  # Exit the loop if successfully converted to int
            except ValueError:
                print("Please enter a valid integer.")

        print(self.is_square(numOne, numTwo))

# Creating an instance and calling the method to handle user input
calc = SquareCalc()
calc.get_user_input()

