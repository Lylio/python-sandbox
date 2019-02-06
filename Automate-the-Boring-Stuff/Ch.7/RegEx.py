import re

phoneNumberRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
matchObject = phoneNumberRegEx.search('My number is 465-465-384.')
print('Phone number found: ' + matchObject.group())