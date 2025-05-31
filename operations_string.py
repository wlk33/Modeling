
s1 = "Hello"
s2 = "world"
print(s1 + " " + s2)
print(3*s2)
print((10//2)*s1)
#len function gives you the size of the string
print(s1, len(s1))
print(3*s2, len(3*s2))

for c in s2:
    print(c*4)

print("zzzzz")

for c in s2:
    print(c*4, end = " ")

new_string = ""
for c in s2:
    new_string += c*4
print(new_string)
