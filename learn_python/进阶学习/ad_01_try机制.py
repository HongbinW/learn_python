try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:	#有错误会被执行，且except可以有好多种
    print('except:', e)
finally:	#一定会执行
    print('finally...')
print('END')