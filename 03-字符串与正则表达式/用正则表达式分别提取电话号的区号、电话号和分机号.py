# q1
import re

m = re.search('(\d{3})-(\d{7,})-(\d{3,})','我的公司座机是024-12345678-5432')# re.search 扫描整个字符串并返回第一个成功的匹配。
if m is not None:
    print(m.group())
    print(m.groups())
    print(m.groups()[0])
    print(m.groups()[1])
    print(m.groups()[2])
