import os
import csv
import re
import string 

file1 = open("paragraph_1.txt","rt") 
data = file1.read()
words = data.split()
print('Number of words in text file :', len(words))
number_of_characters = len(data)
#print('Number of characters in text file :', number_of_characters)

p = re.split("(?<=[.!?]) +", data)
number_of_sentence = len(p)
print('Number of sentence :', number_of_sentence)

data.count(' ')
a = number_of_characters - data.count(' ')

print('Number of characters in text file :', a)

Average_sentence_length = len(words)/len(p)
print(Average_sentence_length)

output_path = os.path.join('PyPara.txt')

with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Paragraph Analysis \n") 
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Approximate Word Count: {len(words)} \n")
    txt_file.write(f"Approximate Sentence Count: {number_of_sentence} \n")
    txt_file.write(f"Average Letter Count: {a} \n")
    txt_file.write(f"Average Sentence Length: {Average_sentence_length} \n")
    txt_file.write("---------------------------- \n") 

       