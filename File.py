text = "Hello World. Welcome to the World of Python."

first = text.find("World")
last = text.rfind("World")

print("First World at:", first)
print("Last World at:", last)

between = text[first + 5 : last]
print("Between:", between)

after = text[last + 5:]
print("After last World:", after)