import subprocess

max_test_num = 100

data_generator_path = 'check\dataGenerator.jar'
check_jar_path = 'check\oo_homework9_check.jar'
stdin_path = 'check\stdin.txt'
check_output_path = 'check\stdout.txt'
test_jar_path = 'your_code.jar'
test_output_path = 'stdout.txt'

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
    while (cur_test_num < max_test_num):
        cur_test_num += 1
        print("test num: ", cur_test_num)
        with open(stdin_path, 'w') as output_file:
            process = subprocess.Popen(['java', '-jar', data_generator_path], stdout=output_file, stderr=subprocess.PIPE)
        with open(stdin_path, 'r') as input_file, open(check_output_path, 'w') as output_file:
            process = subprocess.Popen(['java', '-jar', check_jar_path], stdin=input_file, stdout=output_file, stderr=subprocess.STDOUT)
        with open(stdin_path, 'r') as input_file, open(test_output_path, 'w') as output_file:
            process = subprocess.Popen(['java', '-jar', test_jar_path], stdin=input_file, stdout=output_file, stderr=subprocess.STDOUT)
            # 等待程序运行结束
            process.wait()
        if compare_files(check_output_path, test_output_path):
            print("\033[32;47mAccepted!\033[0m")
        else:
            print("\033[31;43mWrong Answer!\033[0m")
            break

main()
