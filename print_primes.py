primes = [1]

for num in range(1,10):
    print(f"checking {num}")
    for i in range(1,num+1):
        if i == 1:
            continue
        if num == i:
            primes.append(num)
            print(f"{num} is prime")
        if (num/i)%1 == 0:
            print(f"{num}/{i}%1={(num/i)%1}")
            break
        

    
input()

for j in range(1,len(primes)):
    print(primes[j])