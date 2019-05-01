import os

data = []

# 退出文本编辑器
def exitEditor():
    print("exit editor !")
    os.system('cls')

# 文本编辑模式
# 将编辑的内容暂时保存在一个列表中
def textEditor():
    os.system('cls')
    print("如果需要退出编辑，回车后输入  :q  ")
    while True:
        input_ch=input()
        if input_ch == ':q':
            #os.system('cls')
            break
        else:
            data.append(input_ch)
    #print(data)
    return data

# 文本保存模式
def saveText():
    os.system('cls')
    filename_w = input("Please input the file name: ")
    with open(filename_w,'w')as fw:
        for item in data:
            fw.writelines(item)
    print("The file has saved !" + "\t" + "filename is : " + filename_w)

# 读取文件
def readFile():
    os.system('cls')
    filename_r = input("Please input the file name: ")
    try:
        with open(filename_r)as fr:
            read_data = fr.read()
        print(read_data)
        input("输入任意键结束")
    except IOError:
        print("The file can not find !")
    

#### 实现 switch 功能 ####
fun_dict =  {'i': textEditor, 'w': saveText, 'r': readFile, 'q':exitEditor}    # 用于分类的字典
# 缺省函数
def findNone():
    print("Can not find the Key !")

def switch(x):
    return fun_dict.get(x, findNone)()


#### 主界面 ####
def welcom():
    print("Welcome to Simple VIM Editor 1.0 !")
    print("Please input: i to editor, r to read, w to save, q to quit. ")

def main_fun(command):
    switch(command)
    os.system('cls')

while True:
    welcom()
    command = input("input: ")
    if(command == 'q'):
        break
    if(command == 'w' or command == 'r' or command == 'i'):
        main_fun(command)
