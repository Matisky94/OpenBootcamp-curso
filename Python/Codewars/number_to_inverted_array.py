def digitize(n):
    numberToStr = str(n)
    numberLenght = len(numberToStr)
    numberToArray = []
    for i in range(numberLenght):
        numberToArray.append(int(numberToStr[numberLenght-(i+1)]))

    print(numberToArray)
    
digitize(1573)

#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.