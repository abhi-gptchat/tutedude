text = input('Enter text to write to the file: ')

with open('output.txt', 'w') as file:
    file.write(text)
    print('Data successfully writtent to output.txt.')

text1 = input('Enter additional text to append: ')

with open('output.txt', 'a') as file:
    file.write(f"\n{text1}")
    print('Data successfully appeneded')

with open('output.txt', 'r') as file:
    print('Final content of output.txt.:')
    print(file.read())
    
