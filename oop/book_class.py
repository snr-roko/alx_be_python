class Book:
  def __init__(self, name, author, year):
    self.name = name
    self.author = author
    self.year = year

  def __del__(self):
    print(f"Deleting {self.name}")
  
  def __str__(self):
    return f"{self.name} by {self.author}, published in {self.year}"

  def __repr__(self):
    return f"Book('{self.name}', '{self.author}', {self.year})"