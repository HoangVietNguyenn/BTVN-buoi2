# Tạo một mảng ví dụ
my_array = [1, 2, 3, 4, 5]
#trong python  không thể dùng tostring() trực tiếp để chuyển đổi một mảng thành chuỗi
# Sử dụng phương thức join để nối các phần tử của mảng thành chuỗi

#map(str, my_array) được sử dụng để chuyển đổi mỗi phần tử của mảng thành chuỗi
#join() được sử dụng để nối chúng bằng dấu phẩy và khoảng trắng (hoặc bất kỳ ký tự nào bạn muốn)
array_as_string = ', '.join(map(str, my_array))

# In ra chuỗi đã được tạo
print("Mảng như một chuỗi:", array_as_string)
