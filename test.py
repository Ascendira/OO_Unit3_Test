import subprocess

max_test_num = 1000

data_generator_path = 'check\dataGenerator.jar'
check_jar_path = 'check\oo_homework11_check.jar'
stdin_path = 'check\stdin.txt'
check_output_path = 'check\stdout.txt'
set_parameter_path = 'check\set_parameter.txt'
test_jar_path = [
    '.\\your_code.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\2\\out\\artifacts\\2_jar\\2.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\3\\out\\artifacts\\3_jar\\3.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\4\\out\\artifacts\\4_jar\\4.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\5\\out\\artifacts\\5_jar\\5.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\6\\out\\artifacts\\6_jar\\6.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\7\\out\\artifacts\\7_jar\\7.jar',
    'D:\\Files\\Code\\IDEA\\second year down\\OO\\Unit_3\\hw10_mutual_test\\7\\out\\artifacts\\7_jar\\7.jar']
test_output_path = 'stdout.txt'

# 是否进行检查（不对stdin.txt进行修改）
check = 0
# 从test_jar_path中获取检测对象，指定测试对象数
test_num = 1
# 参数设置
# 总指令数
commandsNum = 10000
# 范围 [0,10]
# 生成ln指令的可能性
lnPro = 10
# ln指令生成的人数
lnNum = 90
# 范围 [0,10]
# 生成ln指令时，无效value(值为0)可能性
valueUnEffec = 5
# 范围 [0,10]
# 生成除了复合指令的指令时，正确指令（不报异常）可能性
correctCommand = 10
# 参数反应对应指令的占比，如下参数的作用会相互影响
# ap指令举例：
# 实际ap指令的占比 apPro / 如下参数和
# = (7 / ( 7 + 7 + 7 + 3 + 3 + 1 + 1))
apPro = 20
arPro = 15
mrPro = 2
qvPro = 1
qciPro = 0
qbsPro = 0
qtsPro = 0
atBound = 10
dtBound = 2
attBound = 10
dftBound = 2
qtvsBound = 0
qtavBound = 0
qbaBound = 0
qcsBound = 0
qspBound = 0
amBound = 10
smBound = 10
qsvBound = 2
qrmBound = 2
aremBound = 10
anmBound = 10
cnBound = 1
aemBound = 10
seiBound = 8
qpBound = 1
dceBound = 1
qmBound = 3

def set_parameters():
    with open(set_parameter_path, 'w') as fl:
        fl.write(str(commandsNum) + '\n')
        fl.write(str(valueUnEffec) + '\n')
        fl.write(str(correctCommand) + '\n')
        fl.write(str(apPro) + '\n')
        fl.write(str(arPro) + '\n')
        fl.write(str(mrPro) + '\n')
        fl.write(str(qvPro) + '\n')
        fl.write(str(qciPro) + '\n')
        fl.write(str(qbsPro) + '\n')
        fl.write(str(qtsPro) + '\n')
        fl.write(str(lnPro) + '\n')
        fl.write(str(lnNum) + '\n')
        fl.write(str(atBound) + '\n')
        fl.write(str(dtBound) + '\n')
        fl.write(str(attBound) + '\n')
        fl.write(str(dftBound) + '\n')
        fl.write(str(qtvsBound) + '\n')
        fl.write(str(qtavBound) + '\n')
        fl.write(str(qbaBound) + '\n')
        fl.write(str(qcsBound) + '\n')
        fl.write(str(qspBound) + '\n')
        fl.write(str(amBound) + '\n')
        fl.write(str(smBound) + '\n')
        fl.write(str(qsvBound) + '\n')
        fl.write(str(qrmBound) + '\n')
        fl.write(str(aremBound) + '\n')
        fl.write(str(anmBound) + '\n')
        fl.write(str(cnBound) + '\n')
        fl.write(str(aemBound) + '\n')
        fl.write(str(seiBound) + '\n')
        fl.write(str(qpBound) + '\n')
        fl.write(str(dceBound) + '\n')
        fl.write(str(qmBound) + '\n')

def compare_files(file1, file2):
    lineNum = 1
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()

            # 如果其中一个文件已经读取完毕，而另一个文件还有内容，则内容不同
            if not line1 and line2:
                return False
            if line1 and not line2:
                return False

                # 逐行比较内容
            if line1 != line2:
                print("\033[31;43mDifferent Line: {}\033[0m".format(lineNum))
                return False

                # 当两个文件都读取到文件末尾时，跳出循环
            if not line1 and not line2:
                return True

            lineNum += 1
            # 使用函数比较两个大文件
def main():
    cur_test_num = 0
    set_parameters()
    while (cur_test_num < max_test_num):
        cur_test_num += 1
        print("cur_test_num num: ", cur_test_num)
        if (check == 0) :
            with open(set_parameter_path, 'r') as input_file, open(stdin_path, 'w') as output_file:
                data_generator_process = subprocess.Popen(['java', '-jar', data_generator_path], stdin=input_file,
                                                          stdout=output_file,
                                                          stderr=subprocess.STDOUT)
                data_generator_process.wait()
        with open(stdin_path, 'r') as input_file, open(check_output_path, 'w') as output_file:
            check_process = subprocess.Popen(['java', '-jar', check_jar_path], stdin=input_file, stdout=output_file,
                                             stderr=subprocess.STDOUT)
            check_process.wait()
        for i in range(test_num):
            with open(stdin_path, 'r') as input_file, open(test_output_path, 'w') as output_file:
                test_process = subprocess.Popen(['java', '-jar', test_jar_path[i]], stdin=input_file, stdout=output_file,
                                                stderr=subprocess.STDOUT)
                test_process.wait()
            print("test name: ", i + 1)
            if compare_files(check_output_path, test_output_path):
                print("\033[32;47mAccepted!\033[0m")
            else:
                print("\033[31;43mWrong Answer!\033[0m")
                cur_test_num = max_test_num
                break


main()
