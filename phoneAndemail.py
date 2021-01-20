import re
import pyperclip

# Create a regex for phone numbers
# Using American Phone Numbers - 123-345-6060 or (123) 345-6060 or 345-6060
phoneRegex = re.compile(r"""
   ( ((\d\d\d) | (\(\d\d\d\)) )?     #area code
    (\s | -)                     # Secanrio 2 or there is a -
    \d\d\d                      #triple digits
    -
    \d\d\d\d   )                 #ending digits
""", re.VERBOSE)

# Create a regex for email addresses
# something.+_@something.whatever
emailRegex = re.compile(r"""
    [a-zA-Z0-9.+_]+
    @
    [a-z0-9.+_]+
""", re.VERBOSE)

# Get the text off the clipboard
txt = pyperclip.paste()

# Extract the email/phone from the text
phone = phoneRegex.findall(txt)
email = emailRegex.findall(txt)


for phones in range(len(phone)):
    phone[phones] = phone[phones][0]

#  Copy the extracted emai/phone to clipboard
print(phone)
print(email)
