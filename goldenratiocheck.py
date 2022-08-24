a = input('numero a (maior) ')
b = input('numero b (menor) ')
a = float(a)
b = float(b)
if round(a/b, 1) == round((a+b)/a, 1)== 1.6:
    print('golden ratio 🤌')
else:
    print('not golden ratio, here are the results:')
    print('a/b:',a/b)
    print('a+b/a: ',(a+b)/a)

input('')
