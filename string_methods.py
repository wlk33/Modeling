
print(dir("hello"))
print(help("hi" .capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize())
print("hello".center(50,"x"))
print("gmail.com.".find("."))
print("gmail.com".find("john"))
s = "i see a cat who like to cat while i cat on a cat"
# find all occurrences
position = 0
while True:
    position = s.find("cat", position)
    if position == -1:
        break
    print("found cat on position ", position)
    position += 1

# join - we will come back later
s = "I SEE A LOT OF THINGS!"
print(s.lower())

# replace
s = "i see a cat who like to eat a rat. what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s = "Hello, kind sir! How are you today?"

# split
s = "I like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted))

# title
s = "i like the mountains"
print(s.title())

# upper
s = "i see a lot of things"
print(s.upper().capitalize())
