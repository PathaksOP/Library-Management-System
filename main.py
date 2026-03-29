class Library:
    def __init__(self , no_books , books : list):
        self.no = no_books
        if int(no_books) == len(books):
            self.books = books
        else:
            print('No. of books should be eqal to books in list!')

    def add_book(self , books:str):
        # to add single book
        self.books.append(books)
        self.no = len(self.books)

    def add_book_s(self , books:list):
        # to add many books
        for i in books:
            self.books.append(i)
        self.no = len(self.books)

    def library(self):
        print(f'There are {self.no} books in the library: {self.books}')


x = Library(2 ,['tun-tun' , 'tuk-tuk'])
x.add_book_s(['good' , 'Evil'])
print(x.books)
x.add_book('Tikka')
print(x.books)