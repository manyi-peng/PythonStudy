#python 列表
var1=['peng','man','yi']
var2='peng'
if var2 in var1:
    print 'in'
else:
    print 'not in'
print var1
var1[1]='man'
print var1
var3=['19891006',29]
print var1+var3
for x in var1:
    print x
#python截取列表
print var1[1:]
print len(var1)
print max(var1)
print min(var1)
var4=[20,30,10,34,53]
print max(var4)
print min(var4)
print var4.index(10)
var4.sort()
print var4