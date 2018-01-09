x=set(range(0,10))

print('{0!r:50}'.format(x))

print('{0!s:-^50}'.format(x))
print('{0!s:+<50}'.format(x))
s='{0!s:\b>50s}'.format(x)
print(s,'\n%r'%s)
print('{0!r:>>50}'.format(x))
