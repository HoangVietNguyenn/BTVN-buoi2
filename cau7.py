#Import toàn bộ mô-đun array 
#Dấu * có nghĩa là chúng ta muốn import tất cả các thành phần từ mô-đun này.
from array import *

# Tạo một mảng arr1 với kiểu dữ liệu 'i' và các phần tử là 1, 2, 3, 4, 5, 6
arr1 = array('i', [1, 2, 3, 4, 5, 6])

# Sử dụng phương thức remove() để loại bỏ phần tử có giá trị 4 khỏi mảng
arr1.remove(4)

# In ra mảng sau khi loại bỏ phần tử
print(arr1)
