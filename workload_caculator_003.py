# --------用户输入进行参数传递--------------------

import math

def estimated(size=1,number=None,time=None):
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
if choice == '1':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = None
    time = float(input('请输入工时数量：（可以输入小数）'))
    estimated(size,number,time)
elif choice == '2':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = int(input('请输入人力数量：（请输入整数）'))
    time = None
    estimated(size,number,time)



#-------------------------------函数封装---------------------------------------------
#myinput()函数负责跟用户采集信息，estimated()函数负责完成计算，而main()函数把其他两个函数打包放在一起并传递了参数。
#所以只要调用main()函数就能让整个程序跑起来
import math

# 采集信息的函数
def myinput():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
        # 这里返回的是一个元组
    elif choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time
        # 这里返回的数据是一个元组

# 完成计算的函数
def estimated(my_input):
    # 把元组中的数据取出来
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # 人力计算
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number)) 
    # 工时计算
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

# 主函数
def main():
    my_input = myinput()
    estimated(my_input)

# 调用主函数
main()

#-------------------------------加一个功能“让程序循环运行，直到用户选择结束”。那么，就可以在程序中加上一个again函数------------
import math

#增加变量key代表循环运行程序的开关
key = 1

def myinput():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
    elif choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time

def estimated(my_input):
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))

#询问是否继续的函数
def again():
	# 声明全局变量key，以便修改该变量
	global key
	a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
	if a != 'y':
		key = 0
		#如果不输入y，则把key赋值为0

#主函数
def main():
	print('欢迎使用工作量计算小程序！')
	while key == 1:
		my_input = myinput()
		estimated(my_input)
		again()
	print('感谢使用工作量计算小程序！')

main()
