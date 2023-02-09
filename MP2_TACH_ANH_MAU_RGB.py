import cv2          # Sử dụng thư viện OpenCV cho Python
import numpy as np  # Thư viện toán học để tính toán 

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Khua Ao Xanh.png',cv2.IMREAD_COLOR) #img là biến, trong Python khai báo biến không cần chú trọng đến kiểu dữ liệu
# cv2.imread đọc ảnh màu vào cái biến img 

# Lấy kích thước của ảnh, tạo 2 biến height và width để chứa kích thước của ảnh 
# len() lấy kích thước  
height = len(img[0]) # Lấy kích thước chiều cao của ảnh ở thứ tự số 0 ?????
width  = len(img[1]) # Lấy kích thước chiều ngang của ảnh

# Khai báo 3 biến để chứa hình 3 kênh R-G-B
# Sử dụng thư viện numpy tạo ma trận, 3 biến red, green, blue chứa ma trận, ma trận 3 lớp có 3 kênh màu R G B, mỗi kênh có 8 bit từ 0 đến 255
# Tạo ra ma trận 
red     = np.zeros((width, height, 3), np.uint8)
green   = np.zeros((width, height, 3), np.uint8)
blue    = np.zeros((width, height, 3), np.uint8)

# Ban đầu set zero cho tất cả ma trận (tất cả điểm ảnh) có trong cả 3 kênh trong mỗi hình (mỗi hình có 3 kênh) ? Tại sao lại set về zero
red[:]      = [0, 0 ,0]
green[:]    = [0, 0, 0]
blue[:]     = [0, 0, 0]

# Mỗi hình là một ma trận 2 chiều nên sẽ dùng 2 vòng for 
# Để đọc hết các điểm ảnh (pixel) có trong hình 
for x in range(width): # Vòng for chạy theo chiều ngang
    for y in range(height): # Vòng for chạy theo chiều dọc, quét từng cột từng cột đến cột cuối cùng
        # Lấy giá trị điểm ảnh tại vị trí (x, y)
        R = img[x, y, 0] # Biến R để đọc giá trị red, red chứa ở kênh số 2
        G = img[x, y, 0] # Biến G để dọc giá trị green, green chứa ở kênh số 1 
        B = img[x, y, 0] # Biến B để đọc giá trị blue, blue chứa ở kênh sô 0

        # Thiết lập màu cho các kênh red, green, blue
        # Gán giá trị đặt cho từng giá trị  red, green, blue tại các vị trí (x, y)
        red[x, y, 2]    = G # red có 3 kênh 
        green[x, y, 1]  = G # ??? Gán cùng 1 biến tại sao ko có thay đổi
        blue[x, y, 0]   = G

# Hiển thị hình dùng thư viện OpenCVS
cv2.imshow('Hinh mau RGB goc khua ao xanh - HoDangTu - 20146150', img)
cv2.imshow('Kenh RED - HoDangTu - 20146150', red)
cv2.imshow('Kenh Green - HoDangTu - 20146150', green)
cv2.imshow('KenhBlue - HoDangTu - 20146150', blue)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị hình 
cv2.waitKey(0)

# Giải phóng bộ nhớ cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows() 