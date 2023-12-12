
print("Going to reverse file")
with open("input.txt", "r") as f:
    file_lines = f.readlines()
    with open("output.txt", "w") as wf:
        count = len(file_lines) - 1
        while (count >= 0):
            wf.write(file_lines[count])
            count = count - 1
