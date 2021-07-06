from os import read


def swapFileData():
    fileName = input("Enter the File Name:")
    fileName2 = input("Enter the 2 File Name:")

    
    with open(fileName2, 'r') as b:
        dataB = b.read()

    
    with open(fileName, 'r') as a:
        dataA = a.read()

    with open(fileName2, 'w') as b:
        b.write(dataA)

    with open(fileName, 'w') as a:
        a.write(dataB)
   # print(dataB.read())
    # print(dataA.read())

swapFileData()