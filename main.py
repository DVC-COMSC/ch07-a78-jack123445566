
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
for i in range(len(words)):
    for j in range(len(are)):
        prev_idx = 0 if j == 0 else idxlst[j-1]
        ret = words[i].find(are[j], prev_idx)
        if ret == -1:
            break
        else:	
            print (words[i], end=' ')
print()
