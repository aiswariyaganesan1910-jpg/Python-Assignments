# Q1. Extract only prime numbers from a list
a = [2, 3, 4, 5, 6, 7, 8, 9, 11]
b = []

for n in a:
    if n > 1:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            b.append(n)

print(b)

# Q2. Find word frequencies using a dictionary
s = "Python is a high-level and it is a easy programming language"

words = s.split()
d = {}

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# Q3. Find the most frequently occurring character
s = "banana"
maxi = 0
ch = ""
for i in s:
    count = s.count(i)
    if count > maxi:
        maxi = count
        ch = i
print(ch)

# Q4. Check whether two strings are anagrams
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

# Q5. Flatten a nested list
a = [[1, 2], [3, 4]]
b = []

for i in a:
    for j in i:
        b.append(j)

print(b)

# Q6. Convert CSV string into a list of dictionaries
s = "name,age\nAishu,20\nAdharv,22"
a = s.split("\n")
b = a[0].split(",")

for i in a[1:]:
    c = i.split(",")
    print({b[0]:c[0], b[1]:c[1]})

# Q7. Print only palindrome strings
a = ["madam", "hello", "love", "malayalam"]

for i in a:
    if i == i[::-1]:
        print(i)

# Q8. Remove duplicate dictionaries based on ID
a = [
    {"id": 1, "name": "Aishu"},
    {"id": 2, "name": "Riya"},
    {"id": 1, "name": "Adharv"}
]

b = []

for i in a:
    found = False

    for j in b:
        if i["id"] == j["id"]:
            found = True

    if found == False:
        b.append(i)

print(b)

# Q9. Find the topper
a = [("Aishu", 85), ("Riya", 92), ("Adharv", 78)]

maxi = 0
name = ""

for i in a:
    if i[1] > maxi:
        maxi = i[1]
        name = i[0]

print(name)

# Q10. Count unique words
s = "Python is easy and python is good"

a = s.lower().split()
b = []

for i in a:
    if i not in b:
        b.append(i)

print(len(b))

# Q11. Find the second highest number
a = [10,40,78,94,23,56]

a.sort()

print(a[-2])

# Q12. Count characters, digits and special characters
s = "Hello123@#"

a = 0
b = 0
c = 0

for i in s:
    if i.isalpha():
        a += 1
    elif i.isdigit():
        b += 1
    else:
        c += 1

print("Characters:", a)
print("Digits:", b)
print("Special:", c)

# Q13. Convert JSON string into dictionary and print keys
import json

s = '{"name":"Aishu","age":19}'

a = json.loads(s)

for i in a:
    print(i)

# Q14. Count each character occurrence
s = "banana"
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# Q15. Extract numbers from a mixed list and find their sum
a = [10, "Hi", 20, "Everyone", 5]

sum = 0

for i in a:
    if type(i) == int:
        sum += i

print(sum)