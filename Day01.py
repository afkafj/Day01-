countdown_list=[5,4,3,2,1, "Hey!"]
for countdown in countdown_list:
    print(countdown)
    print(countdown_list[3])
    print(countdown_list[-1])
    print('프로그램 종료')

win= tk.Tk()
win.geometry('400x300')
win.title("파이썬 1일차 Preview")
win.mainloop()
git config --global user.email "kk0412368@gmail.com"



fahrenheit = float(input('화씨 온도 : '))
celsius = (fahrenheit - 32.0) * (5.0/9.0)
print(f'화씨 온도 {fahrenheit}도는 섭씨 {celsius}온도 입니다')


countdown_list=[5,4,3,2,1, "Hey!"]
for countdown in countdown_list:
    print(countdown)

