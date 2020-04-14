"""
查找当前目录所有文件
"""
import os


def get_all(cwd):
    result = []
    # 遍历当前目录，获取文件列表，自己调试看各个步骤的结果
    get_dir = os.listdir(cwd)
    print("当前目录下子目录中的文件：", get_dir)

    for i in get_dir:
        # 把第一步获取的文件加入路径，自己调试看各个步骤的结果
        print("当前目录下子目录中的第一个文件：", i)
        sub_dir = os.path.join(cwd, i)
        print(i, "文件的路径：", sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)
            result.append(file_name)

        return result


if __name__ == "__main__":
    # 获取当前目录：Python Basic grammar,拼上子目录
    cur_path = os.getcwd() + '/res'
    print("当前目录：", cur_path)
    # 调用函数，统计res目录下文件
    print('当前目录的所有文件', get_all(cur_path))
    # 自己扩展，比如按文件类型统计后绘制一个饼图
