import sys

# Check if a name is provided
if len(sys.argv) != 2:
    print("Usage: python script.py [name]")
else:
    name = sys.argv[1]
    print(f"Hello, {name}!")