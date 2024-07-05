students = ['Hermoine','Harry','Ron']

"""
for i in students:
    print(i)
"""

for i in range(len(students)):
    print(i + 1, students[i])

#----------------------------------------#

results = ['Mario', 'Luigi']

results.append('Princess')

results.append('Yoshi')

results.extend(['Toad','Bowser','Donkey Kong Jr.'])

results.remove('Donkey Kong Jr.')

results.insert(0,'Donkey Kong Jr.')

print(results)