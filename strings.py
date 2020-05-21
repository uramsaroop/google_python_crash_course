def first_and_last(message):
  if message[0] == message[-1]:
    return True
  elif message[0] != message[-1]:
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last("elephant"))
print(first_and_last("strings"))