
class ShoppingCart:
    def __init__(self, id):
        self.id = id
        self.books = []
        self.total_price = 0

    def add_book(self, book, n, price = 0):
        book_list = self.books
        no_duplicate_books = True
        for current_book in book_list:
            if current_book[0] == book:
                self.total_price += n * current_book[2]
                current_book[1] += n
                no_duplicate_books = False
        if no_duplicate_books:
            self.books.append([book, n, price])
            self.total_price += n * price

    def delete_book(self, book):
        book_list = self.books
        for current_book in book_list:
            if current_book[0] == book:
                self.total_price -= current_book[1] * current_book[2]
                book_list.remove(current_book)

    def get_total(self):
        return self.total_price

    def __lt__(self, rhs):
        return self.total_price < rhs.total_price


cart_1 = ShoppingCart(1)
cart_1.add_book('b1', 2, 100)
cart_1.add_book('b1', 3)
cart_1.add_book('b2', 1, 103.5)
print(f"books in cart 1: {cart_1.books}")

cart_1.delete_book('b2')
print(f"books in cart 1: {cart_1.books}")

cart_2 = ShoppingCart(2)
cart_2.add_book('b1', 1, 200)
cart_2.add_book('b2', 3, 250)

print(f"cart 1 total price: {cart_1.get_total()}")

print(f"books in cart 2: {cart_2.books}")
print(f"cart 2 total price: {cart_2.get_total()}")

print(cart_1 < cart_2)