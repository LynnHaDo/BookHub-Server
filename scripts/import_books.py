from book.models import Book, BookCategory
import csv 

RATINGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

def run(*args):
    """
    Parse a list of books in csv format and import those to the database

    @params
        path to the csv file
    """
    if args[0].index('.csv') >= 0:
        with open(args[0], encoding='utf-8') as data:
            reader = csv.reader(data)
            next(reader, None)

            for row in reader:
                category = BookCategory.objects.get(name = row[1])

                if category is None: 
                    category = BookCategory.objects.create(
                        name = row[1]
                    )
                    category.save()
                
                book = Book.objects.get(title = row[0])

                if book is not None:
                    continue 

                book = Book.objects.create(
                    title = row[0],
                    category = category,
                    rating = RATINGS[row[2]],
                    price = row[3],
                    stock = row[4],
                    quantity = row[5]
                )

                book.save() 
        
        print(f"Imported {Book.objects.count()} books from data")
    else:
        print("Invalid input. Please pass in a csv file")