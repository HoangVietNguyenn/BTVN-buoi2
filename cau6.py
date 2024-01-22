#Import array từ mô-đun array
#from array import array, chúng ta có thể sử dụng array trực tiếp mà không cần phải thêm tiền tố array. khi gọi các phương thức của lớp array
from array import array

# Khởi tạo mảng với kiểu dữ liệu 'i' (integer)
my_array = array('i', [1, 2, 3, 4, 5])

# Danh sách chứa các phần tử cần thêm vào mảng
elements_to_add = [6, 7, 8, 9, 10]

# Sử dụng phương thức fromlist() để thêm các phần tử từ danh sách vào mảng
my_array.fromlist(elements_to_add)

# In ra mảng sau khi thêm các phần tử
print(my_array)
