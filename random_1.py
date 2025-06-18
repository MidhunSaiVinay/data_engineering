
import random

def generate_random_integer(min_value, max_value):
  """
  Generates a random integer within a specified inclusive range.

  Args:
    min_value: The minimum possible value for the random integer (inclusive).
    max_value: The maximum possible value for the random integer (inclusive).

  Returns:
    A random integer between min_value and max_value.
  """
  # The random.randint() function returns a random integer N
  # such that min_value <= N <= max_value.
  return random.randint(min_value, max_value)

# --- Example Usage ---

# Define the range for the random integer.
# You can change these values to fit your needs.
minimum = 0
maximum = 37

# Call the function to get a random integer.
random_number = generate_random_integer(minimum, maximum)

# Print the result to the console.
print(f"Generated Random Integer: {random_number}")
print(f"This number is between {minimum} and {maximum} (inclusive).")