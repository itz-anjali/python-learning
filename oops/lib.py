# creat library
class lib:
    def __init__(self , series , book):
            self.series = series
            self.book = book
    def add_book (self):
          f= open("lib.txt" , "a")
          f.write(f"{str(self.series)}) {self.book}  \n")
          f= open("lib.txt" , "r")
          data = f.read()
          return data

print("welcome to universe library :~")
while True :
    try:
        print( " do you wanna continue : \n 1) yes  \n 2) no")
        user = int(input(" enter 1 or 2 :  "))
        if user == 1 :
            no = int(input("enter series no : "))
            book_name = input("enter book name: ")
            library = lib( no , book_name)
            print(f" list of books \n { library.add_book()}")
        else:
            break
    except:
         print("something wrong try again :")
