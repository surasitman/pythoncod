print('----------คำนวนขนาด UPS --------')
nodevice = int(input('ระบุจำนวนเครื่องใช้ไฟฟ้าที่ใช้งานกับ UPS เครื่องนี้: '))
va=0.00
try :
    for i in range(nodevice):
        typedevice = input(f'ระบุหน่วยของเครื่องที่ {i+1}  เป็น Watt หรือ VoltกับAmp [W/A]')
        if typedevice == 'w' or  typedevice == 'W':
            watt = float(input(f'ระบุจำนวน Watt เครื่องใช้ไฟฟ้าที่ {i+1}: ' ))
            va= va +(watt*1.4)
        else:
            volt = float(input(f'ระบุจำนวน Volt เครื่องใช้ไฟฟ้าที่ {i+1}: '))
            amp = float(input(f'ระบุจำนวน Amp เครื่องใช้ไฟฟ้าที่ {i+1}: '))
            va = va + (volt * amp)
except:
    for i in range(nodevice):
        typedevice = input('หน่วยเป็น Watt หรือ VoltกับAmp [W/A]')
        if typedevice == 'w' or  typedevice == 'W':
            watt = float(input(f'ระบุจำนวน Watt เครื่องใช้ไฟฟ้าที่ {i+1}: ' ))
            va= va +(watt*1.4)
        else:
            volt = float(input(f'ระบุจำนวน Volt เครื่องใช้ไฟฟ้าที่ {i+1}: '))
            amp = float(input(f'ระบุจำนวน Amp เครื่องใช้ไฟฟ้าที่ {i+1}: '))
            va = va + (volt * amp)
    
print(f'ขนาด UPS ต้องไม่น้อยกว่า {va} VA')

        
