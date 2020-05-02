import re

# p.151
phoneNumberRegEx1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegEx1.search('My home phone number is 555-254-8767')
print('The phone number is ' + mo.group())

# p.152
phoneNumberRegEx2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegEx2.search('My office phone number is 101-831-9977')
print('Area code is ' + mo.group(1))
print('Main number code is ' + mo.group(2))
print('All groups can be 0 or blank: ' + mo.group(0) + ' ' + mo.group())

# p.153
print(mo.groups())
areaCode, mainNumber = mo.groups()
print('Area code is ' + areaCode)
print('Main number is ' + mainNumber)

heroRegEx = re.compile(r'Batman|Tina Fey')
mo1 = heroRegEx.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegEx.search('Tina Fey and Batman')
print(mo2.group())

# p.154
batRegEx = re.compile(r'Bat(man|mobile|girl|arang)')
mo = batRegEx.search('I love how fast the Batmobile is')
print(mo.group()) # Batmobile
print(mo.group(1)) # mobile

batRegEx = re.compile(r'Bat(wo)?man')
mo1 = batRegEx.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegEx.search('The adventures of Batwoman')
print(mo2.group())

