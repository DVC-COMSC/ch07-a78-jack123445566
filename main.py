
letters = ['a', 'r', 'e']


words = input("Enter a list of words: ").split()


result = []


for word in words:
  
  idx = [word.find(letter) for letter in letters]
  if idx == sorted(idx):
   
    result.append(word)


print(result)
