with open("person.csv","r") as person_file:
    content_lines = person_file.readlines()

for line in content_lines[1:]:
    line = line.split(",")
    print(line[0] + " is " + line[2] + " and " + line[1] + " years old.")
