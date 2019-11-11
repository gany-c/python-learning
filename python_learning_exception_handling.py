try:
    f = open("some_non_existent_file.txt")
except FileNotFoundError as e:
    print("File not found")
    print(e)
except Exception as e:
    print("General Error")
    # Put general errors lower in the hierarchy
else:
    print(f.read())
    print("This section runs if no exceptions are hit")
finally:
    print("This part will always run")
