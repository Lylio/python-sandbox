from jinja2 import Template


t = Template("Hello {{ name }}. Here are your {{ object }}.")
print(t.render(name="Sammy", object="keys"))

print("\n-------------------------")

t2 = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
print(t2.render())
