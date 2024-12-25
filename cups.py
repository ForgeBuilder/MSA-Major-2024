while True:
    layer = 1 #we start from the top. layer 1 is the top.
    while True:
        try:
            Input = int(input("how many cups?"))
            break
        except:
            pass
    cups = Input
    while True:
        if cups >= layer:
            cups = cups - layer
        if cups > layer:
            pass
        else:
            print(f"layers = {layer}")
            print(f"cups = {cups}")
            break

        layer = layer+1