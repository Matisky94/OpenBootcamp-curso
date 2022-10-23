def digitize(n):
    numberToStr = str(n)
    numberLenght = len(numberToStr)
    numberToArray = []
    for i in range(numberLenght):
        numberToArray.append(numberToStr[numberLenght-(i+1)])

    print(numberToArray)
    

digitize(5850)