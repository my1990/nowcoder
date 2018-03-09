'''
输入为两行内容，第一行是正整数number，1 ≤ length(number) ≤ 1000。第二行是希望去掉的数字数量cnt  1 ≤ cnt < length(number)。
'''

def get_num():
    while True:
        number = input('')
        if 1<len(number) and len(number)<=1000:
            if number.isdigit():
                while True:
                    cnt = input('')
                    if cnt.isdigit():
                        cnt = int(cnt)
                        if 1<= cnt and cnt < len(number):
                            num_1 = cnt_num(number,cnt)
                            print(num_1)
                            return num_1
                    else:
                        print('no number')

def cnt_num(num,cnt):
    num_list = list(str(num))
    flag = 1
    while flag <= cnt:
        num_list.remove(min(num_list))
        flag += 1
    num_1 = int(''.join(num_list))
    return num_1
get_num()