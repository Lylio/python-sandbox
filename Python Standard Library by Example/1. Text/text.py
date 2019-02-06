import string

s = 'The quick brown fox jumped over the lazy fox'

print()
print(string.capwords(s))

# -----------------------------------------------------

leet = str.maketrans('abegiloprstz', '463611092572')
print(s.translate(leet))

# -----------------------------------------------------

values = {'var1': 'orange',
          'var2': 'green',
          'var3': 'red'}
t = string.Template("$var1, $var2, $var3")
print("Template: ", t.substitute(values))

# -----------------------------------------------------
