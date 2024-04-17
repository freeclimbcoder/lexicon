import pymongo
#pymongo.MongoClient('mongodb://user:password@server:port/')
myclient = pymongo.MongoClient("mongodb://root:123456@localhost:27017/")

mydb = myclient["bookstore"]

mycol = mydb["books"]
for i in range(200):
    mydict = { "author name": f'Test', "title": f'Supertest', "price":100 }
    mycol.insert_one(mydict)

dblist = myclient.list_database_names()
if "bookstore" in dblist:
    print("The database exists.")
else:
    print('nope')

def print_menu() -> int:
    print('"--- Hello and welcome to the awesome Lexicon bookstore! ---" \n(1) Add a book \n(2) View all books \n(3) Search a book by titel \n(4) Update a book price\n(5) Delete a book \n(6)View books by author \n(7) View books in Stock \n(0)Exit')
    return input()

def add_book():
    author_name = input('write the author name\n')
    title = input('write the book title\n')
    price = int(input('write the book price\n'))
    mydict = { "author name": f'{author_name}', "title": f'{title}', "price":price }
    mycol.insert_one(mydict)


def view_all_books():
    for x in mycol.find():
        print(x)

def search_book_by_title():
    title = input('Search a book by titel\nEnter the desired title: \n')
    for x in mycol.find({"title":title}):
        print(x)
    

def upd_book_price():
    author_name = input('write the author name\n')
    title = input('write the book title\n')
    price = int(input('write the new book price\n'))
    myquery = {{"author name":author_name}, {"title": f'{title}' } }
    newvalues = { "$set": { "price": price  } }
    mycol.update_one(myquery, newvalues)
    
def del_book():
    pass

def view_books_by_author():
    author = input('Search a book by authorl\nEnter the desired author name: \n')
    for x in mycol.find({"author name":author}):
        print(x)

def view_books_in_stock():
    for x in mycol:
        print(x)

def exit_store():
    input()
    exit()

def swith_menu(choice: int):
    if choice == 0:
        exit_store()
    if choice == 1:
        add_book
    if choice == 2:
        view_all_books()
    if choice == 3:
        search_book_by_title()
    if choice == 4:
        upd_book_price()
    if choice == 5:
        del_book()
    if choice == 6:
        view_books_by_author()
    if choice == 7:
        view_books_in_stock()




swith_menu(print_menu())

