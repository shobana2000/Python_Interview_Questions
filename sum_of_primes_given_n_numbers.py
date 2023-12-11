def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+1)==0:
            return False
    return True

def primedigits(n):

    prime=0

    while n>0:
        digits=n%10
        if is_prime(digits):
            prime+=digits
        n//=10
    return prime
N = int(input("Enter a number: "))

result = primedigits(30)
print(result)











