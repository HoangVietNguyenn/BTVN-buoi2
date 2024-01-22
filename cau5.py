#import thư viện array và đặt tên ngắn gọn là arr để thuận tiện khi sử dụng các hàm từ thư viện này
import array as arr

# Tạo một mảng my_array với kiểu dữ liệu 'i' (integer) và các phần tử là 1, 2, 3, 4, 5
my_array = arr.array('i', [1, 2, 3, 4, 5])

# Tạo một mảng my_array_2 tương tự như my_array, nhưng chứa các phần tử 6, 7, 8, 9, 10
my_array_2 = arr.array('i', [6, 7, 8, 9, 10])

# Sử dụng phương thức extend để mở rộng my_array bằng cách thêm các phần tử từ my_array_2
my_array.extend(my_array_2)

# In ra mảng my_array sau khi đã được mở rộng
print(my_array)
 