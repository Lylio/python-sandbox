# Practice using delimiters

s = 'some-sentence-which-is-split-with-hyphens'

delimit1 = s.split('-')

print(delimit1) # ['some', 'sentence', 'which', 'is', 'split', 'with', 'hyphens']

s2 = 'Is it possible to delimit by a word?'
delimt2 = s2.split('to')
print(delimt2) # ['Is it possible ', ' delimit by a word?']