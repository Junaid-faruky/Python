# Using a built-in context manager
with open('file.txt', 'r') as file:
    data = file.read()
# File is automatically closed here, even if an exception occurred

# Creating a custom context manager class
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using the custom context manager
with ManagedFile('hello.txt', 'w') as f:
    f.write('Hello, context manager!')
