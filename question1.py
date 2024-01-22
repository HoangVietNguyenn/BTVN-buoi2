def foo(array):
    # Khởi tạo biến sum và product với giá trị ban đầu là 0 và 1
    sum = 0
    product = 1

    # Duyệt qua từng phần tử trong mảng và cộng vào biến sum
    for i in array:
        sum += i

    # Duyệt qua từng phần tử trong mảng và nhân vào biến product
    for i in array:
        product *= i

    # In ra kết quả tổng và tích cùa chuỗi trong array
    print("Sum = " + str(sum) + ", Product = " + str(product))

# Mảng đầu vào
array = [1, 4, 7, 3, 5, 8]

# Gọi hàm foo để thực hiện chương trình 
foo(array)