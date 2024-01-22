#Định nghĩa hàm printUnorderedPairs với tham số đầu vào là một mảng (array
def printUnorderedPairs(array):
    # Duyệt qua từng phần tử i trong mảng
    #Sử dụng vòng lặp for để duyệt qua từng phần tử i trong mảng, với i chạy từ 0 đến len(array) 

    for i in range(0, len(array)):
        # Duyệt qua từng phần tử j trong mảng từ i+1 đến cuối mảng
        #Sử dụng vòng lặp for thứ hai để duyệt qua từng phần tử j trong mảng, với j chạy từ i+1 đến len(array) - 1

        for j in range(i+1, len(array)):
             # In ra cặp không theo thứ tự (i, j)
            #In ra cặp phần tử không theo thứ tự (i, j) trong mảng, sử dụng hàm print() để hiển thị các phần tử liên tiếp nhau và dấu phẩy
        
            print(str(array[i]) + "," + str(array[j]))

# Mảng đầu vào
array_example = [1, 2, 3]
#Gọi hàm printUnorderedPairs với mảng đầu vào [1, 2, 3].
#In ra danh sách các cặp phần tử không theo thứ tự trong mảng
print("Danh sách các cặp không theo thứ tự:")
printUnorderedPairs(array_example)
