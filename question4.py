def printUnorderedPairs(arrayA, arrayB):
    # Duyệt qua từng phần tử i trong mảng arrayA
    for i in range(len(arrayA)):
        # Duyệt qua từng phần tử j trong mảng arrayB
        for j in range(len(arrayB)):
            # Kiểm tra điều kiện: nếu phần tử tương ứng trong arrayA < phần tử tương ứng trong arrayB
            if arrayA[i] < arrayB[j]:
                # phần tử tương ứng trong arrayA nhỏ hơn phần tử tương ứng trong arrayB
                # In ra cặp không theo thứ tự (arrayA[i], arrayB[j])
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# Mảng đầu vào
arrayA = [2, 5, 6, 3]
arrayB = [4, 3, 8, 5]

# Gọi hàm printUnorderedPairs với hai mảng làm đối số
printUnorderedPairs(arrayA, arrayB)
