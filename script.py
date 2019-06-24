with open('test-file.txt', 'r') as text:
    contents = text.read() + " isa"

    print(contents)