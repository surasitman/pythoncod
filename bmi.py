print('---------โปรแกรมคำนวน ค่าดัชนีมวลกาย หรือ BMI (Body Mass Index)----------')
weight = float(input('โปรดระบุ น้ำหนักตัว (กิโลกรัม): '))
height = float(input('โปรดระบุ ส่วนสูง (เมตร): '))
bmi = weight/(height**2)
print('BMI ของคุณ = {:.2f}'.format(bmi))

if bmi<18.5 :
    print('คุณต่ำกว่าเกณฑ์')
elif bmi>=18.5 and bmi<=22.90:
    print('คุณปกติสมส่วน')
elif bmi>=23 and bmi<=24.90:
    print('คุณน้ำหนักเกิน')
elif bmi>=25 and bmi<=29.90:
    print('คุณอ้วนระดับ 1')
else:
    print('คุณอ้วนระดับ 2')

