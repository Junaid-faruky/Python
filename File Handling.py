def read_and_write_file():
    # Write to file
    with open('example.txt', 'w') as file:
        file.write("Hello, World!\nThis is a test file.")
    
    # Read from file
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

read_and_write_file()
