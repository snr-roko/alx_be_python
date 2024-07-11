class Book :
  def __init__(self, title, author) :
    self.title = title
    self.author = author
    self._is_checked_out = False

  def check_out_book(self) :
    if self._is_checked_out == False :
      self._is_checked_out = True
    else :
      print ("Book has already been checked out!!!")

  def return_book(self) :
    if self._is_checked_out == True :
      self._is_checked_out = False
    else :
      print("Book has not been checked out yet")


  def check_out_status(self) :
    if self._is_checked_out :
      return "unavailable"
    else :
      return "available"

class Library :
  def __init__(self) :
    self._books = []
  
  def add_book(self, book) :
    self._books.append(book)
    
  
  def check_out_book(self, title) :
    for book in self._books :
      if book.title == title :
        return book.check_out_book()
    print(f"The Book {title} can not be found in the library")

  def return_book(self, title) :
    self.title = title
    for book in self._books :
      if book.title == self.title :
        return book.return_book()
    print("Book Not Found")

  def list_available_books(self) :
    for book in self._books :
      if book.check_out_status() == "available" :
        print(f"{book.title} by {book.author}")
           

    
    