# god damnit where my changemaker go

# it was so cool ):

denomination_names = ["Hundred dollar bill","Fiftey dollar bill","Twenty dollar bill","Ten dollar bill","Five dollar bill","One dollar bill","Quarter","Dime","Nickle","Pennie"]
denomination_ammounts = [100,50,20,10,5,1,0.25,0.10,0.05,0.01]

final_amounts = []

while True:
    try:
        money = float(input("How much money?!!?!? "))
        break
    except:
        continue

for i in range(0,len(denomination_ammounts)):

    final_amounts.append((money - money%denomination_ammounts[i])/denomination_ammounts[i])
    money = money%denomination_ammounts[i]
    print(f"{final_amounts[i]} {denomination_names[i]}")

