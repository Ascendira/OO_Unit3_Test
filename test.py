import subprocess

max_test_num = 1

data_generator_path = 'check\dataGenerator.jar'
check_jar_path = 'check\oo_homework9_check.jar'
stdin_path = 'check\stdin.txt'
check_output_path = 'check\stdout.txt'
set_parameter_path = 'check\set_parameter.txt'
test_jar_path = 'oohomework_2024_22371027_hw_9.jar'
test_output_path = 'stdout.txt'
commandsNum = 3000
valueUnEffec = 5
currectCommand = 10
apPro = 7
arPro = 7
mrPro = 7
qvPro = 3
qciPro = 3
qbsPro = 1
qtsPro = 1

def set_parameters():
    with open(set_parameter_path, 'w') as fl:
        fl.write(str(commandsNum) + '\n')
        fl.write(str(valueUnEffec) + '\n')
        fl.write(str(currectCommand) + '\n')
        fl.write(str(apPro) + '\n')
        fl.write(str(arPro) + '\n')
        fl.write(str(mrPro) + '\n')
        fl.write(str(qvPro) + '\n')
        fl.write(str(qciPro) + '\n')
        fl.write(str(qbsPro) + '\n')
        fl.write(str(qtsPro) + '\n')

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
        print("test num: ", cur_test_num)
        with open(set_parameter_path, 'r') as input_file, open(stdin_path, 'w') as output_file:
            data_generator_process = subprocess.Popen(['java', '-jar', data_generator_path], stdin=input_file, stdout=output_file,
                                                      stderr=subprocess.STDOUT)
            data_generator_process.wait()
        with open(stdin_path, 'r') as input_file, open(check_output_path, 'w') as output_file:
            check_process = subprocess.Popen(['java', '-jar', check_jar_path], stdin=input_file, stdout=output_file,
                                             stderr=subprocess.STDOUT)
            check_process.wait()

        with open(stdin_path, 'r') as input_file, open(test_output_path, 'w') as output_file:
            test_process = subprocess.Popen(['java', '-jar', test_jar_path], stdin=input_file, stdout=output_file,
                                            stderr=subprocess.STDOUT)
            test_process.wait()
        if compare_files(check_output_path, test_output_path):
            print("\033[32;47mAccepted!\033[0m")
        else:
            print("\033[31;43mWrong Answer!\033[0m")
            break

main()
