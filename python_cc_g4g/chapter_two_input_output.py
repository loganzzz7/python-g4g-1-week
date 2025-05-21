# input notes

# PRINT
# cover print function & various ops
print("study", end = '\n')

a = [1, 2, "lock in"]

print(a)
# print syntax print(vals, sep = '', end = "/n", file = file, flush = flush)

# vals = any value -> converts to string before print

# sep = separator -> how to separate the objects if there is more than one. Default = ''; e.g. sep = ","; sep = "--"
# print("one", "two", "three", sep = "--") -> one--two--three

# end = '\n' new line is default -> otherwise can use to specify end of print

# file = object with write method; default => sys.stdout 
# => e.g. 
# open('file_one.txt', 'w') as file: => w = write -> this overwrites; a = append
# print("this is line one", file = file) => write to a file named file_one with the line this is file one in it

# flush = boolean specifying if output is flushed; default => false
# if false, the print is buffered; 
# else print is instant => useful when another program monitoring printed msgs for debug while print program still running

# INPUT
# used to take input from user
# syntax: input(prompt) => prompt = string written to cmdline w/out newline => return: string obj
name = input("What is your name? \n")
print("Your name is: " + name)

# take in int:
age = int(input("What is your age? \n"))
# can also do float()
# can also do list()
# can also do tuple()
age_next_year = age + 1
print("Your age next year is: ", age_next_year, sep = '') #auto sep = ' ' space

# list example
# List some numbers: 12345
# ['1', '2', '3', '4', '5']
number_list = list(input("List some numbers: "))
print(number_list)

# can also do dictionary
# dictionary example
words_str = input("Input words separated by spaces: ")
word_dict = {word: len(word) for word in words_str.split()}
print(word_dict)

# output notes