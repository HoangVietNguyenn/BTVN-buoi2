#slice elemnets from an array
#Cú pháp chung là [start:stop:step], trong đó:
#start: Chỉ số của phần tử bắt đầu cắt.
#stop: Chỉ số của phần tử kết thúc cắt (không bao gồm phần tử này).
#step: Bước nhảy giữa các chỉ số.

# Tạo một mảng ví dụ
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cắt từ chỉ số 2 đến 5 (không bao gồm phần tử ở chỉ số 5)
sub_array_1 = my_array[2:5]
print("Cắt từ 2 đến 5:", sub_array_1)

# Cắt từ đầu đến chỉ số 7 (không bao gồm phần tử ở chỉ số 7)
sub_array_2 = my_array[:7]
print("Cắt từ đầu đến 7:", sub_array_2)

# Cắt từ chỉ số 3 đến cuối với bước nhảy là 2
sub_array_3 = my_array[3::2]
print("Cắt từ 3 đến cuối với bước nhảy là 2:", sub_array_3)
