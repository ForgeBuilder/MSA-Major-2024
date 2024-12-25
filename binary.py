binary = [128,64,32,16,8,4,2,1]
result = [0,0,0,0,0,0,0,0]

while True:
    result = [0,0,0,0,0,0,0,0]
    while True:
        try:
            Input = input("What's the number?")
            if Input == "end":
                break
            Input = int(Input)
            break
        except:
            print("failed.")

    if Input == "end":
                break
    remainding = Input
    for i in range(0,len(binary)):
        if Input > binary[0]*2-1:
            print("Number too large!")
            break
        if remainding - binary[i] >= 0:
            remainding -= binary[i]
            result[i] = 1
        

        toprint = ""
        for i in range(0,len(result)):
            toprint = toprint+str(result[i])
        print("removing = "+str(remainding))
    print(toprint)


