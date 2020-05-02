#! python3
# pw.py - an insecure password locker program.

PASSWORDS = {'email': 'fwegr435743g',
             'blog': 'rjtjt3t4ttt',
             'luggage': '567384'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is account

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)


