# script_with_issues.py

# --- Problem 1: Potential DivisionByZeroError ---
# This function calculates the average, but doesn't handle empty lists.
def calculate_average(numbers):
  """Calculates the average of a list of numbers."""
  total = 0
  for num in numbers:
    # --- Problem 2: Potential TypeError ---
    # This assumes all items in the list are numbers. What if one isn't?
    total += num
  # Problem 1 occurs here if numbers is empty
  avg = total / len(numbers)
  return avg

# --- Problem 3: Off-by-one Error / Logic Error ---
# This function tries to get numbers greater than a threshold, but misses the threshold itself.
def get_numbers_above_threshold(data, th):
  """Returns numbers strictly greater than the threshold."""
  results = []
  for item in data:
    # --- Problem 4: Bad Variable Name & Logic Error ---
    # 'th' is not very descriptive. The comparison should be '>' not '>='.
    if item >= th:
      results.append(item)
  return results

# --- Problem 5: Inefficient Code & Potential Error with Mixed Types ---
# Calculates sum using a loop instead of built-in sum()
# Also adds numbers and strings if list contains mixed types, causing TypeError
def calculate_sum_inefficiently(items):
    """Calculates the sum of items in a list."""
    # Problem 6: Unclear variable name 'd'
    d = 0 # Should be 'total_sum' or similar
    for i in items:
        d = d + i # Prone to TypeError if 'i' is not a number; less efficient than sum()
    return d


# --- Example Usage ---
if __name__ == "__main__":
  data_list = [1, 5, "6", 10, 15, 2] # Contains a string "6" which will cause issues
  threshold = 5

  print("Data:", data_list)
  print("Threshold:", threshold)

  # This line will likely cause a TypeError in calculate_sum_inefficiently
  try:
    total_sum = calculate_sum_inefficiently(data_list)
    print(f"Calculated Sum: {total_sum}")
  except TypeError as e:
    print(f"Error calculating sum: {e}")
    # Problem 7: The script prints an error but continues. Maybe it should exit?

  # This line will likely cause a TypeError in calculate_average
  try:
    average = calculate_average(data_list)
    print(f"Calculated Average: {average}")
  except TypeError as e:
    print(f"Error calculating average: {e}. Did you remember to clean the data?")

  # Demonstrating the threshold issue
  numbers_above = get_numbers_above_threshold(data_list, threshold)
  # Problem 8: This will also fail because of the string "6" during comparison if not handled.
  # If data_list only contained numbers, e.g. [1, 5, 6, 10, 15, 2],
  # it would return [5, 6, 10, 15] instead of the expected [6, 10, 15] (strictly greater than 5)
  print(f"Numbers above {threshold}: {numbers_above}")

  # Example of DivisionByZeroError (Problem 1)
  empty_list = []
  try:
    avg_empty = calculate_average(empty_list)
    print(f"Average of empty list: {avg_empty}")
  except ZeroDivisionError:
    print("Error: Cannot calculate the average of an empty list!")

  # Problem 9: Lack of docstrings/comments in some parts.
  # Problem 10: No input validation or data cleaning for data_list.
