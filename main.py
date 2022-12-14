# Define the list of letters to search for
letters = ['a', 'r', 'e']

# Ask the user to input a list of words
words = input("Enter a list of words: ").split()

# Create an empty list to store the result
result = []

# Iterate over each word in the list
for word in words:
  # Create a list of the indices of the letters in the word
  indices = [word.find(letter) for letter in letters]
  
  # Check if the indices are in ascending order
  if indices == sorted(indices):
    # If the indices are in ascending order, it means that the word contains
    # the letters in the correct sequence, so we can add it to the result list
    result.append(word)

# Use the join() method to concatenate the strings in the result list
# into a single string, separated by spaces
result_string = " ".join(result)

# Print the result
print(result_string)
