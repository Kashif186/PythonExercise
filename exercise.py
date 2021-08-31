
books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}

def findAuthor(title):
    for author in books.keys():
        authorBooks = books[author]

        for i in range(len(authorBooks)):
            if title.lower() == authorBooks[i].lower():
                return f"{author} wrote {title.title()}"

    return "Book not found"

    
userTitle = input("Input a book title to find the author: ")
print(findAuthor(userTitle))