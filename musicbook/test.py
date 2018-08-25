import re
partten = "^\[(.*)\]\s+(\d+)_(\d+)_(\d+.\d+)_(\d+)$"
compile_rule = re.compile(partten,re.M)
print(re.findall(compile_rule, open('musicbook.txt').read()))

