import re

beginsWithHelloRegex = re.compile(r"^Hello")
endsWithWorldRegex = re.compile(r"world$")
# Starts with a Digit and ends with a Digit as well
allDigitsRegex = re.compile(r"^\d+$")

# Anything bar Newline
# A single character followed by AT - r"{1,2}.at" , 1 or 2 characters
atRegex = re.compile(r".at")
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")  # Anything
dotStar = re.compile(r".*")
vowelRegex = re.compile(r"[aeiou]", re.IGNORECASE)
#txt = "Hello there. This is a testing sentence. Hello world"
txt = "He said \"Hello\" and said world"
digit = "3482374104921x"
Name = "First Name: Larry Last Name: Ghenkin"

prime = "Serve the public trust.\nProtect the innocent.\nUphold the law."

txtObj = endsWithWorldRegex.search(txt)
digitRegex = allDigitsRegex.search(digit)
atRegx = atRegex.findall("The cat in the hat sat on the flat mat.")
name = nameRegex.findall(Name)
vowels = vowelRegex.findall("Hey, Why does the Book tALK ABOUT IT")

print(txtObj == None)
print(digitRegex == None)
# print(regexObj.group())
print(atRegx)
print(name)
print(vowels)
