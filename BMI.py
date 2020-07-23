weight = input('請輸入體重: ')
height = input('請輸入身高: ')
w = weight
w = float(w)
h = height
h = float(h)
h = h/100
b = w / h / h
if  b < 18.5:
    print('您的BMI為', b)
    print('體重過輕')
elif b < 24 and b >= 18.5:
    print('您的BMI為: ', b)
    print('屬於正常範圍')    
elif b >= 24 and b < 27:
    print('您的BMI為: ', b)
    print('體重過重')
elif b >= 30 and b < 35:
    print('您的BMI為: ', b)
    print('輕度肥胖')
elif b >= 35:
    print('您的BMI為: ', b)
    print('重度肥胖')