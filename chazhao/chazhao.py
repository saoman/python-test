import os
import re


def gci(filepath, word):
    global sum
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d, word)
        else:
            if 'api.txt' in fi_d:
                continue
            if fi_d.endswith('.js'):
                print(fi_d)
                with open(fi_d, 'r', encoding='utf-8') as ff:
                    data = ff.read()
                    sum += data.count(word)
    return sum


# 递归遍历/root目录下所有文件
with open('api_sum.txt', 'w', encoding='utf-8') as f:
    for line in open('api.txt', 'r', encoding='utf-8'):
        word = re.sub(r'\n', '', line)
        sum = 0
        gci('./', word)
        f.write(word + '   ' + str(sum) + '\n')
