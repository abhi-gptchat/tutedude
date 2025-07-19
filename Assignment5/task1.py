dict = {'Abhi': 85, 'Binit':90,'Ravi': 95}

name = input("Enter the student's name: ")

if name in dict:
    print(f'{name}\'s marks:', dict.get(name))
else:
    print('Student not found.')
