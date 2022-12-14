words = ['are', 'arrow', 'amore', 'aspire', 'assertive', 'arrogant', 'bartender', 'carter']

# Create an empty list to store the result
result = []

# Iterate over each word in the list
for word in words:
  # Use the find() method to search for the substring 'are' in the word
  index = word.find('are')
  
  # If the find() method returns a non-negative value, it means that the substring was found
  # in the word, so we can add the word to the result list
  if index >= 0:
    result.append(word)

# Print the result
print(result)
