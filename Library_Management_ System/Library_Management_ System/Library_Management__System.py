class Library:

    def __init__ (self):
        self.file= open("books.txt","a+",encoding="utf-8")

    def __del__ (self):
        self.file.close()

    def list_books (self): 
        # Dosyan�n i�eri�ini okuma ve ekleme
        with open("books.txt","r",encoding="utf-8") as file:
            books = file.read().splitlines()

            # Listenin bo� olup olmad���n� kontrol etme
            if not books:
                print ("No books found. Please enter book.")
            else:
                # Ekrana yazd�rma
                for book in books:
                  print(book)
        
       
    def add_book(self):
   
        # Kullan�c�dan kitap ba�l���, kitap yazar�, ilk yay�n y�l� ve sayfa say�s� i�in giri� alma
        title= input ("Enter the name of book: ")
        author = input ("Enter the author of book: ")
        release_date= int(input("Enter the release date of book: "))
        number_of_pages = int(input("Enter the number of pages of the book: "))

        # Kitap bilgilerini i�eren bir string olu�turma
        book_info = f"Title: {title}, Author: {author}, Release Date: {release_date}, Number of Pages: {number_of_pages}\n"

        # Kitap bilgilerini dosyaya ekleme 
        with open("books.txt","a+",encoding="utf-8") as file :
          file.write(book_info)

        print("Book added successfully.")

    def remove_book(self):
        # Kullan�c�dan silinecek kitab�n ad�n� alma
        title_to_remove = input ("Enter the title of the book to remove : ")
        books = []
        try:
          # T�m sat�rlar� bir listeye yazd�rma
          with open("books.txt", "r", encoding = "utf-8") as file:
            books=file.readlines()
        
        
        # Kitab�n indeksini bulma
          index_to_remove = None
          for i, book in enumerate(books):
              if book.strip().lower().startswith(f"title: {title_to_remove}"):
                index_to_remove = i
                break

          if index_to_remove is not None:
            # Kitab� silme i�lmei
            removed_book = books.pop(index_to_remove)
            print(f"'{title_to_remove}' removed successfully.")
          else:
            print(f"'{title_to_remove}' not found in the library.")

          with open ("books.txt","w",encoding ="utf-8")as file:
            file.writelines(books)

        except Exception as e:
          print(f"An error occurred: {e}")   


import datetime

def greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "\033[1;34;40mGood Morning!"
    elif 12 <= current_hour < 18:
        return "\033[1;34;40mGood Afternoon!"
    elif 18 <= current_hour < 21:
        return "\033[1;34;40Good Evening!"
    else:
        return "\033[1;34;40mGood Night!"

greeting = greeting()
print(greeting)

#o Obje olu�turma
lib=Library()

# Men� i�lemleri
while True:
  print ("\n  \033[1;32;40m ***MENU***\n ")
  print(" 1) List Books ")
  print(" 2) Add Book ")
  print(" 3) Remove Book ")

  choice = input ("\033[1;33;40mPlease enter your choice: ")
  if choice == "1":
    lib.list_books()
  elif choice == "2":
     lib.add_book()
  elif choice == "3":
      lib.remove_book()
  elif choice == "q":
      break
  else:
      print("\033[1;31;40mInvaild choice. Please try again.")

  