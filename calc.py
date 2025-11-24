# calc.py - simple calculator
VERSION = "v1.0"

def add(a, b):
    return a + b

def main():
    # Greeting line that we'll intentionally change on branches
    print("Hello from feature-A branch - version " + VERSION)
    print("2 + 3 =", add(2, 3))

if __name__ == "__main__":
    main()
    