n = int(input("Type a number: "))

count = 0
for i in range(3, n + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
        
            
    if is_prime:
        print(i)
        count += 1

print("\n\nNumber of counts:", count)