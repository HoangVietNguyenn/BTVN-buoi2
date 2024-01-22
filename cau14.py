#Import thư viện NumPy: Dòng này import thư viện NumPy và đặt tên ngắn gọn là np để thuận tiện khi sử dụng các hàm từ thư viện này.
import numpy as np

# Tạo một mảng NumPy
array = np.array([1, 2, 0, 4])

# Chuyển đổi mảng thành danh sách bằng phương thức tolist()
list_from_array = array.tolist()

# In ra danh sách
print(list_from_array)
