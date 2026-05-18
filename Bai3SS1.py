# Phân tích 
# Đầu vào của bệnh viện yêu cầu là nhập vào tên bệnh nhân, mã bệnh án, chuyển tới đâu từ đó in ra phiếu điện tử đúng với định dạng, dữ liệu trùng khớp với dữ liệu trùng lặp  
# Giải pháp là tạo input và lưu vào 3 biến khác nhau từ đó dùng print để in ra 

# Viết code 

name_patient =  input("Nhập tên bệnh nhân: ")
code_id = input("Nhập mã bệnh án: ")
room = input("Nhập phòng khám: ") 

print(f"Bệnh nhân: {name_patient} - Mã BA: {code_id} - Chuyển tới: {room}")