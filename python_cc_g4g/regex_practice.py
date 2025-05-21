# REGEX REVIEW
# regular expressions:
# => tool for matching text based on pre-defined pattern; detects the prescence or absence of a certain string of text via pattern matching
# => provided by the python library RE module
import re

# search():
# syntax -> search(regular expression, string) => returns first match or none
match = re.search(r"geeks", "test geeks for geeks") # => r stands for RAW NOT REGEX
print(match) # => <re.Match object; span=(5, 10), match='geeks'>; spans from index 5 (including) to index 10 (excluding)
# group(): => returns the matching string
# start(): => returns the starting index of the match
# end(): => returns the ending index of the match

print(match.group()) # => geeks
print("Start index:", match.start()) # => Start index: 5
print("End index:", match.end()) # => End index: 10

# Regex Meta Characters:
# \: used for escaping the first character following it
# []: represent a character class
# ^: matches the beginning
# $: matches the end
# .: matches any character except NEW LINE
# |: OR; matches any of the characters separated by it
# ?: matches 0 or 1 occurrence
# *: matches any number of occurrences --INCLUDING ZERO OCCURRENCES
# +: one or more occurrences
# {}: indicates the number of occurrences of a preceding RegEx to match
# (): enclose a group of RegEx

# why regular expressions
# data mining: RegEx is the best tool for data mining => e.g. identifying email, phone number, url from pile of text
# data validation: Checks that the input follows a proper format or else doesn't accept it => e.g. email, phone number...

# basic regular expressions
# character classes => []: allows matching of a single set of characters with a possible set of characters
# e.g. =>
print(re.findall(r'[Gg]eeks', "Geeks for geeks")) # => ['Geeks', 'geeks'] => matches both G and g followed by eeks

# ranges:
# allows for matching a range of characters
# e.g. =>
print("Range Match:", re.search(r'[a-zA-Z]', "x23")) # => Range Match: <re.Match object; span=(0, 1), match='x'>
# => matches ranges a to z and A to Z in string

# negation:
# inverts a character class and matches all but the inverted class
# e.g. =>
print("Neg Match:", re.findall(r'[^a-z]', "x23")) # => Neg Match: ['2', '3']
# search ONLY returns FIRST match!!!
print("Neg Match:", re.search(r'[^a-z]', "x23")) # => Neg Match: <re.Match object; span=(1, 2), match='2'>
print("Neg Match:", re.search(r'[^a-z]', "x")) # => Neg Match: None

# List of SPECIAL SEQUENCES:
# \A: matches if the string begins with the character provided => e.g. --\Ahello matches hello world and hello kitty
# \b: \b(string) matches if begins with the provided string; (string)\b matches if ends with the provided string
# \B: OPPOSITE of \b => does not match if begins \B(string) or ends (string)\B w provided string
# \d: matches any digits 0-9; equivalent to [0-9] character class
# \D: marches any non digits; equivalent to [^0-9] --negation of [0-9]
# \s: matches any white space character
# \S: matches any NON white space character => negation of \s
# \w: matches any alpha numeric characters (word characters) = equivalent to [0-9a-zA-Z_] --> due to snake_case => _ is included
# \W: matches any non alpha numeric characters => negation of \w; [^0-9a-zA-Z_]

# \Z: matches if the string ends with the given RegEx => (string)\Z => if there is \n for newline at end of line it will NOT MATCH
# => differs from \b in that it checks that the regex provided is at the very end 
# => where as \b checks for the str character before a non alphanumeric character

# shortcuts:
# \b: matches a position and not a character 
print("b shortcut:", re.search(r"\bGeeks\b", "GeeksforGeeks")) 
# => b shortcut: None -> GeeksforGeeks doesn't have a word boundary after Geeks, there are more strs that follow
# => checks for word boundries before & after RegEx
# beginning and end of string:
# any character: 

# more regex
# compiled regex