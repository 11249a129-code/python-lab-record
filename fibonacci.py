//aim:to write aprogram on fibonacci sequence

//algorithm
Start
2. Read the value of N from the user.
3. Check if N > 0.
If not, display: "Error: N must be greater than 0" and stop.
4. Call the function fibonacci(N).
5. Inside the function:
If N == 1, return 0
If N == 2, return 1
Otherwise:
Initialize a = 0, b = 1
Loop from 3 to N:
c = a + b
Update: a = b, b = c
Return b 

//program
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b
N = int(input("Enter a value for N (N > 0): "))

if N <= 0:
    print("Error: N must be greater than 0")
else:
    result = fibonacci(N)
    print(f"Fibonacci number F{N} =", result)
