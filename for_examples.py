
for i in range(1, 10, 2):
    print(i)
    #Last one (second number) is not included. if we print this, 1 through 9 is included
    # the third number defines the steps. in this example it is every 2 numbers

print("zzzzzzzzz")

s = 0
for i in range(1, 11):
    s += i
#s = s + i
print(s)

print("zzzzzzz")

s = 0
i = 1
while i <= 10:
    s += i
    i += 1
print(i)
print(s)
