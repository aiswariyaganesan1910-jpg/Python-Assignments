# Q1. Take two integer inputs and print their product.
a = int(input())
b = int(input())
print(a * b)

# Q2. Round a float to 2 decimal places.
x = 12.34567
print(round(x, 2))

# Q3. Count the number of vowels in a string.
s = input()
count = 0

for i in s:
    if i in "aeiouAEIOU":
        count += 1

print(count)

# Q4. Remove all even numbers from a list.
a = [10, 15, 20, 25, 30, 35]

b = []

for i in a:
    if i % 2 != 0:
        b.append(i)

print(b)

# Q5. Check whether an input is an integer or float.
num = input()

if "." in num:
    print("Float")
else:
    print("Integer")

# Q6. Count the number of words in a sentence.
s = input()
words = s.split()
print(len(words))

# Q7. Find the sum and average of a list.
a = [10, 20, 30, 40, 50]

total = sum(a)
average = total / len(a)

print("Sum:", total)
print("Average:", average)

# Q8. Print names of people older than 18 using a dictionary.
people = {
    "Aishu": 19,
    "Adharv": 20,
    "Riya": 25,
    "Adhu": 17
}

for n, a in people.items():
    if a > 18:
        print(n)

# Q9. Convert a float into integer and string.
num = float(input())

a = int(num)
b = str(num)

print(a, type(a))
print(b, type(b))

# Q10. Sort 5 strings in reverse alphabetical order.
a = ["watermelon", "mango", "blackberry", "orange", "kiwi"]

a.sort(reverse=True)

print(a)

# Q11. Print year, month and day separately.
date = input()

year, month, day = date.split("-")

print("Year:", year)
print("Month:", month)
print("Day:", day)

# Q12. Convert tuple into list and append an item.
a = (10, 20, 30, 40, 50)

b = list(a)
b.append(60)

print(b)

# Q13. Print student names whose scores are greater than 50.
students = [ ["Aishu", 57], ["Adharv", 98], ["Riya", 45], ["Adhu", 30] ]
for i in students:
    if i[1] > 50:
        print(i[0])

# Q14. Check whether a string is a palindrome.
s = input()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q15. Replace spaces with underscores.
s = input()

s = s.replace(" ", "_")

print(s)