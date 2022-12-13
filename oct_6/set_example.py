my_set = {"one", "ten", "two", "ten", "three", "ten", "four", "nine", "ten"}




print("one".__hash__() % 10)
print("two".__hash__() % 10)
print("ten".__hash__() % 10)
