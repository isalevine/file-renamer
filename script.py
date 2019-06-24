with open('test-file.txt', 'a') as text:
    text.write(", isa")


with open('test-file.txt', 'r') as text:
    print(text.read())