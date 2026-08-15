data = open("junk.txt")
lines = data.readlines()
for line in lines:
    print(line[0:-1])

with open("junk.txt") as file:
    file.write
    lines = file.readlines()
    print("Total number of lines:", len(lines))

    text = "".join(lines).lower()

    text += "text file nanalyssis\n"

    with open("junk.txt", "w") as file:
        file.write(text)

    print("File processed and saved successfully.")


data.close()