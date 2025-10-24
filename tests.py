from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = "Война и мир"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Комедии")
        collector.set_book_genre("Книга2", "Комедии")
        books = collector.get_books_with_specific_genre("Комедии")
        assert "Книга1" in books
        assert "Книга2" in books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.add_new_book("Взрослая книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        collector.set_book_genre("Взрослая книга", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books
        assert "Взрослая книга" not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Книга для избранных"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = "Удаляемая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    


