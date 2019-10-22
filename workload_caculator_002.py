#计算人力时向上取整
import math

# 工时计算
def estimated_time(size,number):
    time = size * 80 / number
    print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))

# 人力计算
def estimated_number(size,time):
    number = math.ceil(size * 80 / time)
    print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))

# 调用工时计算函数
estimated_time(1.5,2)
# 调用人力计算函数
estimated_number(1,60)


#精简代码
