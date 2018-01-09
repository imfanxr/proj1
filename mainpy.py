import random

a=9**190
s=str(a)
b=int(s[::-1])
c=abs(b-a)

s=sum(int(x) for x in str(a))

print('{0:10d}-{1:10d}={2:10d}\n{3:<20d}{4!r:+^40}'.format(a,b,c,s, {int(x) for x in str(a)}))

# cnt=dict.fromkeys(range(0,10),0)
# cnt=list(range(0,10))
cnt=[0]*10

for x in str(a):
    cnt[int(x)]+=1

print('{0!r}'.format(cnt))
print(cnt)

s=0
i=0
for x in cnt:
    s+=x*i
    i+=1

print(s)


cnt={}

print(cnt)

for x in range(0,20):
    cnt[(int(random.random()*10),int(random.random()*10),int(random.random()*10))]=int(random.random()*10)

print(cnt)

for x in sorted(cnt.keys()):
    print('{0}: {1}'.format(x,cnt[x]))

cnt={}
