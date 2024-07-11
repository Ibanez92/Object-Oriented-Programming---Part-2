from shape import Circle, Rectangle, Triangle

def main():
    shapes = [
        Circle("Red", 5),
        Rectangle("Blue", 4, 6),
        Triangle("Green", 3, 4, 5)
    ]

    for shape in shapes:
        print(f"Shape: {shape.__class__.__name__}")
        print(f"Color: {shape.get_color()}")
        print(f"Area: {shape.calculate_area()}")
        print(f"Perimeter: {shape.calculate_perimeter()}")
        print()

if __name__ == "__main__":
    main()
