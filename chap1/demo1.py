#可以输出数字
print(520)
print(1314)

#可以输出字符串
print('hello world!')

#含有运算符的表达式
print(3+4)

#将数据输出文件中
fp=open('/Users/aojiaoxiaozhiwei/Desktop/xiaozhiwei/text.txt','a+')#a+如果文件不存在就创建，存在就在文件内容后面继续追加
print('hello world',file=fp)
fp.close()

#不进行换行输出(输出内容在一行当中)
print('hello','world','python')


