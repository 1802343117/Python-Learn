'''
保留字是Python语言中已经被赋予特定意义的一些单词，
开发程序时，不可以作为变量、函数、类、模块和其他对象的名称来使用。
'''

# 通过模块提供的方法查看Python的保留字
import keyword
print(keyword.kwlist)
# 注：保留字是区分大小写的

"""
_标识符     ——>   保护变量
__标识符    ——>   类的私有成员
__标识符__  ——>   专用标识（如：__init__()表示构造方法）
"""