def welcomeMes():
    print("โปรดเลือกสิ่งที่ท่านต้องการรวจสอบ")
    print("ชื่อ/นามสกุล/ชื่อเล่น กด 1")
    print("เบอร์โทร/เลขต่างๆ กด 2")


def chooseFunction():
    try:
        x = int(input("ฉันเลือก : "))
        while (x != 1) or (x != 2):
            print("กรุณาเลือกให้ถูกต้อง!")
            chooseFunction()
    except:
        print("กรุณาเลือกให้ถูกต้อง!")
        chooseFunction()
    

