n=int(input("Enter no. of terms: "))
x=-1
y=1
i=0
Fibo=[]
while i<n: 
    s = x+y
    Fibo.append(s)
    x=y
    y=s
    i+=1
print("Fibonacci series upto ",n," terms is : " ,Fibo)
