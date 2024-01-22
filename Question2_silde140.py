def find_pairs(nums, target_sum):
    pairs = set()  # Để lưu trữ các cặp số duy nhất
    seen_nums = set()  # Để theo dõi các số đã xuất hiện

    for num in nums:
        complement = target_sum - num

        if complement in seen_nums:
            # Kiểm tra xem cặp số đã có trong tập hợp chưa để tránh trùng lặp
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)

        seen_nums.add(num)

    return list(pairs)

# Đầu vào mẫu
nums = [2, 6, 3, 9, 11]
target_sum = 9

# Gọi hàm và in kết quả
result = find_pairs(nums, target_sum)
print(result)
