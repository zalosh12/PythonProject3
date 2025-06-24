# question 2

lines = ["Hello world",
        "It’s the first exercise in I/O",
        "That mean it is number 1",
        "Not 2",
        "Not three",
        "It is exciting",
        "And i am all 4 it"]

with open("my_text.txt","w",encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
# test
with open("my_text.txt","r") as f:
    for line in f:
        print(line,end=" ")

# question 3

total_non_numbers = 0
total_letter_count = 0
even_word_lines = 0
word_freq = {}

with open("my_text.txt","r") as f:
    for line in f:
        words = line.split()
        if not line:
            continue

        for word in words:
            clean_word = word.strip(".,?!").lower()
            if not clean_word.isdigit():
                total_non_numbers += 1
                word_freq[clean_word] = word_freq.get(clean_word,0) + 1

        if len(words) % 2 == 0:
            even_word_lines += 1

        total_letter_count += sum(1 for c in line if c.isalpha())

most_common_word = max(word_freq.items(),key=lambda x: x[1])

print(f"the total number of words: {total_non_numbers}")
print(f"the total number of letters: {total_letter_count}")
print(f"the sum of even lines: {even_word_lines}")
print(f"the most common word: {most_common_word}")

#question 4

#read the content in my_text.txt"
with open("my_text.txt","r") as f:
    lines = f.readlines()

#add the content to a new file + the number of words in each line
with open("summary.txt","w") as f:
    for line in lines:
        sum_words = len([i for i in line.split() if not i.isdigit()])
        f.write(line.rstrip("\n") + " | num of words: " + str(sum_words) + "\n")
# test for the new file
with open("summary.txt","r") as f:
    x = f.read()
    print(x)




