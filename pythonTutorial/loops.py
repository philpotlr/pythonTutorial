#Loops


#for loop
people = ['john', 'sarah', 'tim', 'bob']

for person in people:
    print('current person: ', person)


#iterate by sequence index
for i in range(len(people)):
    print('current person', people[i])

for i in range(0,10):
    print(i)


# While Loop
count = 0
while count < 10:
    print('Count: ', count)
    if count == 5:
        break
    count = count + 1