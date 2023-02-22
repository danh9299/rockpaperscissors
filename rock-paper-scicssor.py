# Dự án cá nhân: Chương trình game oẳn tù tì
# Họ tên: Nguyễn Duy Anh
# Ngày sinh: 9/2/1999
# Email: nguyenduyanh.tit@gmail.com
# Github: danh9299

import random
import re


while(True):
    print()
    print("************************")
    print("Oẳn Tù Tì Ra Cái Gì Nào!")
    print()
    
    # Nhận lựa chọn oẳn tù tì của người chơi
    playerDecision = input("Bạn ra cái [Đ]ấm], [L]á, hoặc [K]éo: ")
    
    # Dùng regex để bắt lỗi khi người dùng nhập sai kí tự
    if not re.match("[ĐđLlKk]", playerDecision):
        print("Bạn chỉ được chọn 1 trong 3 vũ khí dưới đây:")
        print("[Đ]ấm], [L]á, hoặc [K]éo.")
        continue
    print("Bạn chọn: " + playerDecision)

    # Random lựa chọn của máy
    options = ['Đ', 'L', 'K']
    opponenetDecision = random.choice(options)
    print("Tôi chọn: " + opponenetDecision)
    
    # So sánh kết quả và thông báo
    if opponenetDecision == str.upper(playerDecision):
        print("Hòa! ")
    elif opponenetDecision == 'Đ' and playerDecision.upper() == 'K':      
        print("Đấm thua kéo rồi, Tôi thắng! ")
        continue
    elif opponenetDecision == 'K' and playerDecision.upper() == 'L':      
        print("Lá sao thắng được kéo! Tôi xin phần thắng nhé! ")
        continue
    elif opponenetDecision == 'L' and playerDecision.upper() == 'Đ':      
        print("Lá thắng đấm, bạn thua rồi! ")
        continue
    else:       
        print("Bạn thắng rồi! Ôi không :(")
