"""
for i in [0,1,2]:
    print('meow')
"""
"""
for _ in range(3): #use _ if you are not going to use the variable
    print('meow')

print('meow\n' * 3,end='')
"""

while True:
    n = int(input('What''s n? ' ))
    """
    if n <= 0:
        continue
    else:
        break
    """
    if n > 0:
        break

for i in range(n):
    print('meow')