#Bethany Berlage and Vinni Paradiso
# my_string="Hello, my name is John."
# my_list=my_string.split()
# print(my_list)
import string
def sentence_to_list(input_sentence):
    input_sentence=input_sentence.translate(str.maketrans(" "," ", string.punctuation))
    output_list=input_sentence.split()
    return output_list

my_sentence="This is a sample sentence with some punctuation, like a comma."
my_list=sentence_to_list(my_sentence)
print(my_list)
