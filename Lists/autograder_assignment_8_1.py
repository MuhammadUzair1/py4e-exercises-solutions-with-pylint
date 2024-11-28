'''
This program reads the file and parses the file line by line 
and then splits the line into words and then appends the words into a list. 
If the word is already in the list, it will skip the word and move to the next word. 
Finally, it will sort the list and print the list.
'''

file_name = input("Enter file name: ")

LST = []
with open(f'./files/{file_name}', encoding="utf-8") as fh:
    for line in fh:
        x = line.rstrip().split(' ')
        for i in x:
            if i not in LST:
                LST.append(i)
            else:
                continue

LST.sort()
print(LST)
