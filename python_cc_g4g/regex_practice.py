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
# ^(string): chooses the beginning of a string
# e.g. =>
print(re.search(r"^Geeks", "Hello Geeks")) # => None
print(re.search(r"^Geeks", "GeeksforGeeks")) # => <re.Match object; span=(0, 5), match='Geeks'>
# (string)$: chooses the ending of a string
print(re.search(r"bert$", "hello scoobert")) # => <re.Match object; span=(10, 14), match='bert'>
# any character: 
# .: this represents any character
# e.g. =>
print(re.findall(r"s..ob..t", "hello scoobert spoobart")) # => ['scoobert', 'spoobart']


# more regex
# optinal characters:
# (str)?: allows str or [char cls] to be unpresent or present once.
# e.g. =>
print(re.search(r"colou?r", "color")) # => <re.Match object; span=(0, 5), match='color'>
print(re.search(r"colou?r", "colour")) # => <re.Match object; span=(0, 6), match='colour'>
# repetition:
# (str){num}: allows for str or [char cls] to repeat num times; {num} can be range --{lower,upper}; {1,} --upper = inf
print("[month]-[day]-[year]:", re.findall(r"[\d]{2}.[\d]{2}.[\d]{4}", "05-21-2025 or 05/21/2025")) 
# => [month]-[day]-[year]: ['05-21-2025', '05/21/2025']
print("Range Num:", re.findall(r"[\d]{3,4}", "123 or 1234"))
# => Range Num: ['123', '1234']
# shorthand:
# +: this is short for {1,}--one or more
# *: this is short for {0,}--zero or more
print("+:", re.search(r"[\d]+", "123")) # => +: <re.Match object; span=(0, 3), match='123'>
print("*:", re.search(r"[\d]*", "hello")) # => *: <re.Match object; span=(0, 0), match=''>

# grouping:
# (): this allows fetching regex as a group
# e.g. =>
print("[month]-[day]-[year]:", re.findall(r"([\d]{2}.[\d]{2}.[\d]{4})", "05-21-2025 or 05/21/2025")) 
# => [month]-[day]-[year]: ['05-21-2025', '05/21/2025']

# .group(index): returns data as entire match or if provided index the group at the index
print("[month]-[day]-[year]:", re.search(r"([\d]{2}.[\d]{2}.[\d]{4})", "05-21-2025").group()) 
# => [month]-[day]-[year]: 05-21-2025
print("[month]-[day]-[year]:", re.search(r"([\d]{2}).([\d]{2}).([\d]{4})", "05-21-2025").group(2))
# => [month]-[day]-[year]: 21

# .groups(): return a tuple of matched groups
print("[month]-[day]-[year]:", re.search(r"([\d]{2}).([\d]{2}).([\d]{4})", "05-21-2025").groups()) 
# => [month]-[day]-[year]: ('05', '21', '2025')

# naming groups:
# (?P<name>): python extension for naming
print("group(mm):", re.search(r"(?P<dd>[\d]{2}).(?P<mm>[\d]{2}).(?P<yyyy>[\d]{4})", "05-21-2025").group("mm"))
# => group(mm): 21
print("groupdict():", re.search(r"(?P<dd>[\d]{2}).(?P<mm>[\d]{2}).(?P<yyyy>[\d]{4})", "05-21-2025").groupdict())
# => groupdict(): {'dd': '05', 'mm': '21', 'yyyy': '2025'}


# lookahead:
# => attempts to match the subsequent input with the given pattern
# str(?!regex): negative lookahead; regex DOESN'T come after current str
print("neg lookahead:", re.search(r"ber(?!e)", "scoobert"))
# => neg lookahead: <re.Match object; span=(4, 7), match='ber'>
print("neg lookahead:", re.search(r"ber(?!t)", "scoobert"))
# => neg lookahead: None

# str(?=regex): positive lookahead; regex DOES come after current str
print("pos lookahead:", re.search(r"ber(?=e)", "scoobert"))
# => pos lookahead: None
print("pos lookahead:", re.search(r"ber(?=t)", "scoobert"))
# => pos lookahead: <re.Match object; span=(4, 7), match='ber'>


# subsitution:
# sub(regex, replacement, search str): replaces the result via the replacement str
# e.g. =>
print("replace whitespace:", re.sub(r"\s", r".", "scoo bert"))
# => replace whitespace: scoo.bert

# compiled regex
regex = re.compile(r"([\d]{2}).([\d]{2}).([\d]{4})")

print("Compiled RegEx:", regex.search("05-21-2025").group())
# => Compiled RegEx: 05-21-2025
print("Sub Compiled:", regex.sub(r"\1.\2.\3", "05-21-2025"))
# => Sub Compiled: 05.21.2025