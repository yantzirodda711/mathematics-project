class ExampleClass:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def add(self, x, y):
        return x + y

    def multiply(self, a, b):
        return a * b

# Create an instance of the class
example_instance = ExampleClass()

# Add two numbers to the example instance's data
result1 = example_instance.add(5, 3)
print("Result 1:", result1)

# Multiply two numbers to the example instance's data
result2 = example_instance.multiply(4, 6)
print("Result 2:", result2)
