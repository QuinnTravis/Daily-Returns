def dailyReturns(x):
    
    lenArray = len(x)
    newArray = []
    
    for i in range(lenArray-1):
        
        dReturns = (x[i+1] - x[i]) / x[i]
        
        dReturns *= 100
        
        if dReturns > 0:
            dReturns = "+" + str(dReturns) + "%"
        elif dReturns <0:
            dReturns = "-" + str(dReturns) + "%"
        else:
            dReturns = "0%"

        
        newArray.append(dReturns)
            

    return newArray



returnArray = []

size = int(input("Enter size of array: "))

for i in range(size):
    num = float(input("Enter value to be input: "))
        
    returnArray.append(num)
        
print(dailyReturns(returnArray))
        