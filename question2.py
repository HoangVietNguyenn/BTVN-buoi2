def printPairs(array):
    # Duyệt qua từng phần tử i trong mảng
    for i in array:
        # Duyệt qua từng phần tử j trong mảng
        for j in array:
            # In ra cặp (i, j)
            print(str(i) + "," + str(j))

# Mảng đầu vào
sampleArray = [2, 4, 5, 3, 1]

# Gọi hàm printPairs  để thực hiện chương trình 
printPairs(sampleArray)
# hàm dùng lệnh for lồng nhau 
# for i chạy phần tử đầu tiên thì for j chạy hết các phần tử có trong mãng  
# chạy lần lượt tăng for i lên cho đến phần tử cuối cùng của for i thì ngừng và in ra