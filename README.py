# Personal-Library-Manager
#"A Python system to manage personal books and wishlists using dynamic list operations and data flow logic."
#step 1: setup
library=[]
wishlist=[]
#step 2:Adding Individual books
book_name= input("Enter The name of a book you own:\n").lower()
library.append(book_name)

book_name= input("Enter The name of another book you own (or press 'Enter o skip') ....\n").lower()
if book_name:
    library.append(book_name)
print(f"your library {library}")
#step 3:managing the wishlist
book_name= input("Enter The name of a book you wish to have in the future:\n").lower()
wishlist.append(book_name)

book_name= input("Enter The name of another book you wish to have (or press 'Enter o skip') ....\n").lower()
wishlist.append(book_name)
print(f"your wishlist {wishlist}")

#step 4: mering wishlist in to library
Acquir_book= input("Enter The name of a book from your wishlist that you've acqured (or press 'Enter o skip') ....\n").lower()
if Acquir_book in wishlist:
    library.append(Acquir_book)
    wishlist.remove(Acquir_book)
print(f"updated library{library}")
print(f"updated wishlist{wishlist}")

#step 6:donating books
Donated_book= input("Enter The name of a book from your library you wish to donat (or press 'Enter o skip') ....\n").lower()
if Donated_book in library:
   library.remove(Donated_book)
print(f"final library after donations:{library}")
