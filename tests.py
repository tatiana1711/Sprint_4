from main import BooksCollector
import pytest


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2
    

    def test_add_new_book_add_book_with_name_more_than_max(self):
        collector = BooksCollector()
        book_name = 'Гарри Уизли и приключение, которое просто невозможно забыть просто так'
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre


    @pytest.mark.parametrize ('book', ['1', 'something_different', '&*&^%()', '40 символов 40 символов 40 символов 40 с', ' '])
    def test_add_new_book_with_valid_names(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert book in collector.get_books_genre()


    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        book_genre = 'Мультфильмы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert book_genre == collector.books_genre[book_name]

    def test_get_book_genre_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Рецепты на все случаи жизни')
        collector.set_book_genre('Рецепты на все случаи жизни', 'Кулинария')
        assert collector.get_book_genre('Рецепты на все случаи жизни') != 'Кулинария'


    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Красная шапочка')
        collector.set_book_genre('Красная шапочка', 'Ужасы')
        assert collector.get_book_genre('Красная шапочка') == 'Ужасы'


    def test_get_books_with_specific_genre_two_books_the_same_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать')
        collector.add_new_book('Му-му')
        collector.set_book_genre('Что делать', 'Фантастика')
        collector.set_book_genre('Му-му', 'Фантастика')
        assert (collector.get_books_with_specific_genre('Фантастика') == ['Что делать', 'Му-му'])
    
    def test_get_books_genre_add_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_books_genre() == {'Война и мир': ''}

    def test_get_books_for_children_book_not_in_genre_age_rating_list(self):
        collector = BooksCollector()
        collector.add_new_book('Сказ о закрытой ипотеке')
        collector.set_book_genre('Сказ о закрытой ипотеке', 'Фантастика')
        assert 'Сказ о закрытой ипотеке' in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        assert 'Унесенные ветром' in collector.favorites


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        collector.delete_book_from_favorites('Унесенные ветром')
        assert 'Унесенные ветром' not in collector.favorites


    @pytest.mark.parametrize('book, genre', [('Кто это сделал?', 'Детективы'),('Это сделал я', 'Комедия')])
    def test_get_list_of_favorites_books_get_two_books(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()





