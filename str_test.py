#python 访问字符串中的值
var1='pengmanyi'
var2='19891006'
print 'var1[0]:',var1[0]
print 'var2[1:5]',var2[1:5]
#python 更新已有字符串
print '更新字符串：-',var1[:6]+'Runoob!'
#python 转义符
print '\x0a'
print R'\n'
print r'\n'
if 'abs' in 'absc':
    print 'in'
else:
    print 'not in'
#python 字符串格式化
print 'my name is %s and weight is %dkg!' %('pengmanyi',55)