text = "Hello World. Welcome to the World of Python."
word = "World"

first = text.find(word)
last = text.rfind(word)

print("First World at:", first)
print("Last World at:", last)

between = text[first + len(word):last]
print("Between:", between)

after = text[last + len(word):]
print("After last World:", after)