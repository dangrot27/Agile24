import sys

# Check if at least one name is provided
if len(sys.argv) < 2:
    print("Usage: python script.py [name1] [name2] ... [nameN]")
else:
    # Loop through each name in the command-line arguments (excluding the script name)
    for name in sys.argv[1:]:
        print(f"Hello, {name}!")