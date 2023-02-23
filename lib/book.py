#!/usr/bin/env python3

class Book:
    author = "Agatha Christie"
    genre = "Mystery"
    def __init__(self, title, page_count=0):
        self.title = title        
        self.page_count = page_count


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_page(self):
        return self._page_count
    
    def set_page(self, page_count):
        if (type(page_count) == int):
            print(f"Ayyeeee there's {page_count} pages in this ishhh")
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page, set_page)


book = Book("And Then There Were None.")
print(book.title)
book.page_count = 272
print(book.author)
book.genre 
book.turn_page()



        # if (type(page_count) == (int)):