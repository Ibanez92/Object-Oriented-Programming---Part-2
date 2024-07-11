# Shape Class Hierarchy

## Overview

This project implements a class hierarchy to represent various shapes, such as circles, rectangles, and triangles. It demonstrates the use of inheritance, method overriding, and polymorphism to achieve code flexibility and extensibility.

## Class Hierarchy

### Shape (Base Class)

- **Attributes:**
  - `color` (string): The color of the shape
- **Methods:**
  - `__init__(self, color)`: Constructor to initialize the shape with the given color
  - `calculate_area(self)`: Abstract method to calculate the area of the shape (raises `NotImplementedError`)
  - `calculate_perimeter(self)`: Abstract method to calculate the perimeter of the shape (raises `NotImplementedError`)
  - `get_color(self)`: Method to retrieve the color of the shape
  - `set_color(self, color)`: Method to set the color of the shape

### Circle (Derived Class)

- **Attributes:**
  - `radius` (float): The radius of the circle
- **Methods:**
  - `__init__(self, color, radius)`: Constructor to initialize the circle with the given color and radius
  - `calculate_area(self)`: Overrides the base class method to calculate the area of the circle (`πr²`)
  - `calculate_perimeter(self)`: Overrides the base class method to calculate the perimeter (circumference) of the circle (`2πr`)

### Rectangle (Derived Class)

- **Attributes:**
  - `length` (float): The length of the rectangle
  - `width` (float): The width of the rectangle
- **Methods:**
  - `__init__(self, color, length, width)`: Constructor to initialize the rectangle with the given color, length, and width
  - `calculate_area(self)`: Overrides the base class method to calculate the area of the rectangle (`length * width`)
  - `calculate_perimeter(self)`: Overrides the base class method to calculate the perimeter of the rectangle (`2 * (length + width)`)

### Triangle (Derived Class)

- **Attributes:**
  - `side1` (float): The length of the first side of the triangle
  - `side2` (float): The length of the second side of the triangle
  - `side3` (float): The length of the third side of the triangle
- **Methods:**
  - `__init__(self, color, side1, side2, side3)`: Constructor to initialize the triangle with the given color and side lengths
  - `calculate_area(self)`: Overrides the base class method to calculate the area of the triangle using Heron's formula
  - `calculate_perimeter(self)`: Overrides the base class method to calculate the perimeter of the triangle (`side1 + side2 + side3`)

## Usage

### Running the Program

1. Ensure you have Python installed on your system.
2. Create a directory for the project and add the following files:
   - `shape.py` (contains the class definitions)
   - `main.py` (contains the main program logic)

## Instructions
1. Place shape.py and main.py in the same directory.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the files.
4. Run the main program with the command:
```sh
python main.py