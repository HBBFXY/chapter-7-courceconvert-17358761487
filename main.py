import keyword

# 读取原文件
with open('random_int.py', 'r') as f:
    content = f.read()

# 处理字符
converted_content = ''
for char in content:
    if char.islower() and char not in keyword.kwlist:
        converted_content += char.upper()
    else:
        converted_content += char

# 写入新文件
with open('random_int_converted.py', 'w') as f:
    f.write(converted_content)
