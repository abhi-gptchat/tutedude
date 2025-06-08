def readSampleFile(fileName):
    try:
        with open(fileName, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('There is no such file.')


readSampleFile('sample1.txt')
