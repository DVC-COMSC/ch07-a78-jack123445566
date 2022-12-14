words = ['are', 'arrow', 'amore', 'aspire', 'assertive', 'arrogant', 'bartender', 'carter']

# Create an empty list to store the result
result = []

# Define the list of letters to search for
letters = ['a', 'r', 'e']

# Iterate over each word in the list
for word in words:
  # Create a list of the indices of the letters in the word
  indices = [word.find(letter) for letter in letters]
  
  # Check if the indices are in ascending order
  if indices == sorted(indices):
    # If the indices are in ascending order, it means that the word contains
    # the letters in the correct sequence, so we can add it to the result list
    result.append(word)

# Print the result
print(result)
