class Person:
  def __dir__(self):
    return ['age', 'name', 'salary']

p1 = Person()

print(dir(p1))