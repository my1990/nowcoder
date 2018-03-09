'''
题目描述
继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替 （"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"）， 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
输入描述:
第一行是一个整数T（1 ≤ T ≤ 100)表示测试样例数；接下来T行，每行给定一个分身后的电话号码的分身（长度在3到10000之间）。
输出描述:
输出T行，分别对应输入中每行字符串对应的分身前的最小电话号码（允许前导0）。
示例1
输入

4
EIGHT
ZEROTWOONE
OHWETENRTEO
OHEWTIEGTHENRTEO
输出

0
234
345
0345
'''


dict = {
    0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'
}

#计算字符串s里包括哪些字符，如：ONE TWO
def chage_str(s):
    list = []
    while len(s) != 0:
        for i in dict:                        #循环字典
            s1 = set(s) & set(dict[i])         #字典里每一个值与字符串s求并集
            if len(s1) == len(set(dict[i])):  # 并集长度等于字典里某个值长度，说明字典里某个值存在于字符串中
                for j in dict[i]:
                    s = s.replace(j,'',1)      #存在则去掉这个
                list.append(dict[i])
            else:
                if len(s) == 0:
                    break
    for x in list:
        for i in dict:
            if dict[i] == x:
                list[list.index(x)] = i
    list.sort()
    return list


def main_1():
    num = int(input(''))  #输入几行字符串
    flag = 0
    str_list = []
    while flag < num:
        string = input('')
        str_list.append(string)
        flag += 1
    for s in str_list:  #循环每一行字符串
        list_yuan = chage_str(s)          #替换字符为数字，比如把ONE 替换成1  TWO替换成2
        for y in range(len(list_yuan)):  #得到原始数字
            if list_yuan[y] < 8:
                list_yuan[y] = str(list_yuan[y] + 2)
            else:
                list_yuan[y] = str(list_yuan[y] - 8)
        list_yuan.sort()  #排序
        str_result = ''.join(list_yuan)
        print(str_result)
main_1()
