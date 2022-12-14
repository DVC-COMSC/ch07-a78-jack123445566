
letters = ['a', 'r', 'e']


words = input().split()


result = []


for word in words:
  
  indices = [word.find(letter) for letter in letters]
  
  
  if indices == sorted(indices):
    
    result.append(word)


result_string = " ".join(result)


print(result_string)
