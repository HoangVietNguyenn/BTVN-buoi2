#Định nghĩa hàm powersOf2 nhận một tham số là n
def powersOf2(n):
    # Trường hợp cơ bản: nếu n < 1, trả về 0
    if n < 1:
        return 0
    # Trường hợp cơ bản: nếu n == 1, in ra 1 và trả về 1
    elif n == 1:
        print(1)
        return 1
 
    else:
        #hàm gọi đệ quy để tính lũy thừa của 2 cho n/2 thông qua dòng prev = powersOf2(int(n/2))
        prev = powersOf2(int(n/2))
       #hàm nhân kết quả prev với 2 để tính lũy thừa của 2 cho n và lưu vào biến curr
        curr = prev * 2
        #In ra giá trị của curr bằng lệnh print(curr)
        print(curr)
        #Trả về giá trị của curr.
        return curr

# Gọi hàm powersOf2 với n=8 và in ra các lũy thừa của 2 từ 1 đến 8
n = 8
print(powersOf2(n))
