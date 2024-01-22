def two_sum(nums, target):
    num_indices = {}  # Sử dụng một từ điển để lưu giữ giá trị và chỉ số của nó

    for i, num in enumerate(nums):
        complement = target - num  # Tìm giá trị bổ sung cần để có tổng bằng target

        if complement in num_indices:
            # Nếu giá trị bổ sung đã tồn tại trong từ điển, nghĩa là chúng ta đã tìm thấy cặp số
            return [num_indices[complement], i]
        
        # Nếu không tìm thấy, thêm giá trị hiện tại và chỉ số của nó vào từ điển
        num_indices[num] = i

    # Nếu không có cặp số nào thỏa mãn, trả về một danh sách trống hoặc giá trị khác để thể hiện không tìm thấy
    return []

# Example
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
