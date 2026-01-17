string = input("Please enter your own word: ")
char = input("Please enter a charecter: ")
i=0
count=0
while(i < len(string)):
    if (string [i]==char):
        count = count + 1
    i = i + 1
print(f"The total number of times {char} has occoured = {count}")    