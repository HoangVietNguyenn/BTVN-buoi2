def allFib(n):
    # Duyệt qua các số từ 0 đến n-1 và in ra số Fibonacci tương ứng
    for i in range(n):
        print(str(i) + ":, " + str(fib(i)))
#Hàm fib tính số Fibonacci tại vị trí n
def fib(n):
    # Trường hợp cơ bản: nếu n <= 0, trả về 0
    if n <= 0:
        return 0
    # Trường hợp cơ bản: nếu n == 1, trả về 1
    elif n == 1:
        return 1
    # Trường hợp chung: tính số Fibonacci bằng cách cộng hai số Fibonacci trước đó
    return fib(n-1) + fib(n-2)

# Gọi hàm allFib với n=2 và in ra dãy số Fibonacci từ 0 đến 1
n = 2
print(allFib(n))
