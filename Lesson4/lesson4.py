# number1 = int(input("Nhap so nguyen 1: "))
# number2 = int(input("Nhap so nguyen 2: "))
# if number1 < number2:
#     print("So 1 nho hon so 2")
# elif number1 > number2:
#     print("So 1 lon hon so 2")
# elif number1 == number2:
#     print("So 1 va so 2 bang nhau")

# Nhập vào hai cạnh a và b, nếu a lớn hơn b thì in ra đây là hình 
#chữ nhật
# nếu a bằng b thì in ra đây là hình vuông

# numberA = float(input("Nhap vao so a: "))
# numberB = float(input("Nhap vao so B: "))
# if numberA > 0 and numberB > 0: # mo rong dieu kien
#     if numberA > numberB or numberA < numberB:
#         print("Day la hinh chu nhat")
#     elif numberA == numberB:
#         print("Day la hinh vuong")
# else:
#     print("Gia tri nhap chua duoc dung")

# Nhap vao 1 so va kiem tra so day la so chan hay so le
# number_check = float(input("Nhap vao so can kiem tra: "))
# if number_check % 2 == 0:
#     print("Day la so chan")
# else: 
#     print("Day la so le")

number_abs = float(input("Nhap va so can chuyen doi: "))
if number_abs < 0:
    number_abs = number_abs * (-1)
    print("Gia tri sau khi chuyen doi la",number_abs)
else:
    print("Gia tri cua ban khong phai doi")