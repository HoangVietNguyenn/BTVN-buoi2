#định nghĩa hàm factorial với tham số đầu vào là một số nguyên n
def factorial(n):
    # Kiểm tra nếu n là số âm, trả về -1 vì giai thừa không được xác định cho số âm
    if n < 0:
        return -1
    # Trường hợp cơ bản: nếu n bằng 0, giai thừa là 1
    elif n == 0:
        return 1
    else:
        # Trường hợp chung: tính giai thừa bằng cách nhân n với giai thừa của (n-1)
        return n * factorial(n-1)

# Gọi hàm factorial với n=4 và in ra kết quả
n = 4
print(factorial(n))
