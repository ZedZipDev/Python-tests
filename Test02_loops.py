#1 
print('Test #1')
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
    
#2
# range(start, stop, step) - stop is not included
print('Test #2')
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
print(' Prints out 3,4,5')
# Prints out 3,4,5
for x in range(3, 6):
    print(x)

print(' Prints out 3,5,7')
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

        
#
print(' while')        
#
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1        
    
#
print('"break" and "continue" statements')        
# Prints out 0,1,2,3,4
print(' prints out 0,1,2,3,4')  
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print(' prints out only odd numbers - 1,3,5,7,9')  
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)    

print('"else" can be used in loops')        
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):    break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")    

#else belongs to loop but not if (!)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
            
#            
print('continue')            
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)            