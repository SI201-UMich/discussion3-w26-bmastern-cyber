import math

class Rectangle():
    # Create the constructor "__init__" method

    # YOUR CODE HERE
    def __init__(self, length, width):
        self.length = length
        self.width = width


    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"Length: {self.length} Width: {self.width}"


    # Create the "area_calculator" method

    # YOUR CODE HERE
    def area_calculator(self):
        area = self.length * self.width
        return area

    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE
    def __eq__(self, other):
        return (self.length == other.length) and (self.width == other.width)

    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print(r1.__eq__(r2))

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    r3 = Rectangle(10,10)
    print(r1.__eq__(r3))

if __name__ == "__main__":
    main()