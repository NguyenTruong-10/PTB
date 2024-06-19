# Bài 1: In dãy số từ 1 đến 10
# for i in range(1, 11):
#     print(i)
# Bài 2: In số chẵn từ 1 đến 30
# Lưu ý làm 2 cách
# c1:
# for i in range(2,32,2):
#     print(i)
# C2:
# for i in range(1,31):
#     if (i % 2 == 0):
#         print(i)
# Bài 3:In số chẵn từ 1 đến 20
# for i in range(2,32,2):
#     print(i)
# C2:
# for i in range(1,31):
#     if (i % 2 == 0):
#         print(i)
# Lưu ý làm 2 cách
# Bài 4:In bảng cửu chương 5
for a in range(1,11):
    # print("5 x ",i, "=", 5*i)
    print(f"5 x {a} = {5*a}")
# Bài 5: In các số từ 10 đến 1
for reverse in range(10,0,-1):
    print(reverse)
# Yêu cầu: Sử dụng vòng lặp For để in ra các số từ 10 đến 1 (theo thứ tự ngược).
# Bài 6: Tính tổng các số từ 1 đến 100
sum = 0
for i in range(1,101):
    sum = sum + i
print("Tong la:", sum)