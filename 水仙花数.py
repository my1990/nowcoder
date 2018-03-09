'''
题目描述
春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的： “水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。 现在要求输出所有在m和n范围内的水仙花数。
输入描述:
输入数据有多组，每组占一行，包括两个整数m和n（100 ≤ m ≤ n ≤ 999）。
输出描述:
对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n，如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开;
如果给定的范围内不存在水仙花数，则输出no;
每个测试实例的输出占一行。
示例1
输入

100 120
300 380
输出

no
370 371
'''
import sys
#获取2个数 m,n
def get_num():
    list = []
    flower_list = []   #最终水仙花数
    flag = 1
    while flag != 0:   #获取输入的每一行
        num = input("")
        flag = len(num)
        list.append(num)  #把输入的每一行加入list列表

    for x in range(len(list)-1):  #循环list每一行
        m,n = map(int,str(list[x]).split(' '))   #得到每一行的俩个数m,n
        for i in range(int(m),int(n)+1):         #得到m ,n之间的所有数
            if flower(str(i)) != 0:              #通过flower函数计算每一个数是不是水仙花数，返回0就不是
                flower_list.append(i)            #是水仙花数就加到flower_list列表里
        if len(flower_list) == 0:                #列表空，说明没有水仙花数，返回no
            print('no')
        else:
            string = str(flower_list).replace('[','').replace(']','').replace(',',' ')
            print(string)                        #打印m,n范围内的所有水仙花数


#判断一个数是否为水仙花数,返回0说明不是
def flower(num):
    num_list = list(num)
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    result = [x**3 for x in num_list]
    sum = 0
    for j in result:
        sum += j
    if sum == int(num):
        return sum
    else:
        return 0

get_num()
