value = 0
for i in range(11):
    value +=i
    print(f"i is {i}, value is {value}")

print(f"Final value is {value}")

print("#####################################################")

#while loop
count = 1
while count < 10:
    count += 1
    print(f"count is {count}")
print("#####################################################")



#breakk statement

for i in range(10):
    if i == 5:
        break
    print(f" {i}")
print("#####################################################")

#continue statement
for odd in range(10):
    if odd % 2 == 0:
        continue
    print(f"odd is {odd}")

print("#####################################################")

#nested loops 

for i in range(5):
    for j in range (5):
        print(f"sum is {i + j}")


