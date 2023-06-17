def recur_fibonacci(n):
    if(n<=1):
        return n
    else:
        return(recur_fibonacci(n-1)+recur_fibonacci(n-2))
        
n_terms=int(input("Enter the number of terms you want: "))

#Checking if the number of terms is valid
if(n_terms<=0):
    print("Incorrect, you have to enter a positive integer")
else:
    print("Fibonacci Sequence:")
    for i in range(n_terms):
        print(recur_fibonacci(i)) 
