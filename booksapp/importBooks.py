import requests
from .models import Book

# In "books" are json data. Try to get only needed keys.
def importBook(books):

    all_results = []

    for book in books["items"]:
        
        id = book["id"]
        # Some books hasn't every keys. "try" provide this.
        try:
            # Some titles have troublesome letters inside. This encoding ignore this letters.
            title = book["volumeInfo"]["title"].encode(encoding="ascii", errors="ignore").decode("ascii")
        except:
            title = ""
        try:
            authors = ', '.join(book["volumeInfo"]["authors"])
        except:
            authors = ""
        try:
            publishedDate = book["volumeInfo"]["publishedDate"]
        except:
            publishedDate = ""

        try:
            for i in book["volumeInfo"]["industryIdentifiers"]:
                if i["type"] == "ISBN_10":
                    type10 = i["type"]
                    identifier10 = i["identifier"]
                
                elif i["type"] == "ISBN_13":
                    type13 = i["type"]
                    identifier13 = i["identifier"]
        except:
            type10 = ""
            identifier10 = ""
            type13 = ""
            identifier13 = ""   

        try:        
            pageCount = book["volumeInfo"]["pageCount"]
        except:
            pageCount = ""
        try:
            smallThumbnail = book["volumeInfo"]["imageLinks"]["smallThumbnail"]
        except:
            smallThumbnail = ""
        try:
            thumbnail = book["volumeInfo"]["imageLinks"]["thumbnail"]
        except:
            thumbnail = ""
        try:
            language = book["volumeInfo"]["language"]
        except:
            language = ""

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
                "language" : language,
                "id" : id
                }
        # Save every search to list.
        all_results.append(data_dict)


    return all_results
