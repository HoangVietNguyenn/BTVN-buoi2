# định nghĩa hàm reverse với tham số đầu vào là một mảng (array)
def reverse(array):
    # Duyệt qua nửa đầu của mảng
    #Sử dụng vòng lặp for để duyệt qua nửa đầu của mảng, với i chạy từ 0 đến len(array)/2 - 1
    for i in range(0, int(len(array)/2)):
        # Tính chỉ số của phần tử simetric
        other = len(array) - i - 1
        # Tráo đổi giá trị giữa phần tử hiện tại và phần tử simetric
        #Sử dụng biến tạm (temp) để tráo đổi giá trị giữa phần tử hiện tại (array[i]) và phần tử simetric (array[other]
        temp = array[i]
        array[i] = array[other]
        array[other] = temp

    # In ra mảng sau khi đảo ngược
    print(array)

# Mảng đầu vào
array = [2, 5, 6, 8]

# Gọi hàm reverse với mảng làm đối số
reverse(array)
