'''
you have new models, and old models
newmodels begin with number as second element
old models begin with string as second element


sort second

4
mi2 jog mid pet
wz3 34 54 398
al alps cow bar
x4 45 21 7


'''
arr = ['mi2 jog mid pet', 'wz3 34 54 398', 'al alps cow bar', 'x4 45 21 7']

arr.sort(key=lambda item: (item[1], item[0]))
print(arr)