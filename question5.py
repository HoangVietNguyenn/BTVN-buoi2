def printUnorderedPairs(arrayA, arrayB):
    # Duyệt qua từng phần tử i trong mảng arrayA
    for i in range(len(arrayA)):
        # Duyệt qua từng phần tử j trong mảng arrayB
        for j in range(len(arrayB)):
            # Duyệt qua từng phần tử k từ 0 đến 4 (tổng cộng 5 giá trị)
            for k in range(0, 5):
                #mỗi cặp được in ra 5 lần, do có vòng lặp for k in range(0, 5)
                # In ra cặp không theo thứ tự (arrayA[i], arrayB[j])
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# Mảng đầu vào
arrayA = [2, 5, 6, 8]
arrayB = [4, 3, 8, 9]

# Gọi hàm printUnorderedPairs với hai mảng làm đối số
printUnorderedPairs(arrayA, arrayB)
