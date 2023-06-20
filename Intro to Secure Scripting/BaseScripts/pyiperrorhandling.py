import pyinputplus as pyip

# Define a function that uses pyinputplus to get user input
def get_user_input():
    # Use pyinputplus to get a valid integer input from the user
    num = pyip.inputInt(prompt="Enter a number: ")

    # Use pyinputplus to get a valid yes or no input from the user
    choice = pyip.inputYesNo(prompt="Do you want to continue? ")

    # Return the user's input as a tuple
    return (num, choice)

# Use a try-except block to handle any errors that may occur during execution
try:
    # Call the get_user_input function to get user input
    user_input = get_user_input()

    # Print the user's input
    print(f"You entered {user_input[0]} and chose {'yes' if user_input[1] else 'no'}.")
except pyip._exceptions.RetryLimitException:
    # Handle RetryLimitException if the user exceeds the maximum number of retries
    print("Error: Maximum number of retries exceeded.")
except pyip._exceptions.TimeoutException:
    # Handle TimeoutException if the user does not provide input within the specified time
    print("Error: Input timed out.")
except Exception as e:
    # Handle any other exceptions that may occur
    print(f"Error: {str(e)}")

