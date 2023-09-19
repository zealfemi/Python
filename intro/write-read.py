# with open('text.txt', mode='w') as f:
#     f.write('Hello World!')

with open('text.txt', mode='a') as f:
    f.write('\nThis is a newline with append')

with open('text.txt', mode='r') as f:
    print(f.read())