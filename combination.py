def fact(n):
    ans = 1
    for i in range (1,n+1):
        ans *= i

    return ans;

print("Enter n & r below")
n = int(input())
r = int(input())

n_factorial = fact(n);
r_factorial = fact(r);
nr_factorial = fact(n-r);

print(n_factorial//(r_factorial * nr_factorial))
