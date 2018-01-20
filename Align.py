# -*- coding:utf-8 -*-
# 一个用于格式化输出对齐的模块，实际使用并不好使
# 检测是否是中文字段，若不是，填补半角空格，若是，则填补全角空格
def myAlign(string, length=0):
    if length == 0:
        return string
    slen = len(string)
    re = string
    if isinstance(string, str):
        placeholder = ' '
    else:
        placeholder = u'　'
    while slen < length:
        re += placeholder
        slen += 1
    return re