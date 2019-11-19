import requests
from .models import Book

# This code import and save every book to database from below URL.
def database():
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=hobbit")
    data = response.json()

    # In "data" are json data. Try to get only needed keys.
    for book in data["items"]:
        # Some titles have troublesome letters inside. This encoding ignore this letters.
        title = book["volumeInfo"]["title"].encode(encoding="ascii", errors="ignore").decode("ascii")
        authors = ', '.join(book["volumeInfo"]["authors"])
        publishedDate = book["volumeInfo"]["publishedDate"]
        
        if "industryIdentifiers" in book["volumeInfo"]:
            for i in book["volumeInfo"]["industryIdentifiers"]:
                if i["type"] == "ISBN_10":
                    type10 = i["type"]
                    identifier10 = i["identifier"]
                
                elif i["type"] == "ISBN_13":
                    type13 = i["type"]
                    identifier13 = i["identifier"]
        else:
            type10 = ""
            identifier10 = ""
            type13 = ""
            identifier13 = ""    
        
        if "pageCount" in book["volumeInfo"]:
            pageCount = book["volumeInfo"]["pageCount"]
        else:
            pageCount = ""
        smallThumbnail = book["volumeInfo"]["imageLinks"]["smallThumbnail"]
        thumbnail = book["volumeInfo"]["imageLinks"]["thumbnail"]
        language = book["volumeInfo"]["language"]


        data_dict = {
                "title" : title,
                "authors" : authors,
                "publishedDate" : publishedDate,
                "type10" : type10,
                "identifier10" : identifier10,
                "type13" : type13,
                "identifier13" : identifier13,
                "pageCount" : pageCount,
                "smallThumbnail" : smallThumbnail,
                "thumbnail" : thumbnail,
                "language" : language
                }
        # Create and save each book to database.
        create_Database = Book(**data_dict)
        create_Database.save()
