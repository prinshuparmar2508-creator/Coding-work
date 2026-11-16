#creating a file and writing in it
file = open("data.txt", "w")
file.write("Hi,I am Txt file\n writing line 2nd\n writing line 3rd\n writing line 4th\n writing line 5th")
file.close()

#reading a file
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()

#counting words in a text file
file = open("data.txt", "r")
text = file.read()
words = text.split()
print("Word count:", len(words))
file.close()

#finding the longest word in a text file
file = open("data.txt", "r")
text = file.read()
words = text.split()
longest = max(words, key=len)
print("Longest word:", longest)
file.close()