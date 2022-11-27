from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_init_books_rating_takes_key_and_value(self):
        collector = BooksCollector()
        collector.books_rating = {
            'Алхимик': 8,
            'Тестирование Дот Ком': 9
        }
        assert len(collector.books_rating) == 2

    def test_init_list_of_favorites_books_add_values(self):
        collector = BooksCollector()
        collector.favorites = ['Алхимик', 'Тестирование Дот Ком']
        assert len(collector.favorites) == 2

    def test_add_new_book_similar_books_dont_add(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Алхимик')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_if_between_1_and_10_inclusive_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_rating(name='Алхимик', rating=8)
        assert collector.get_book_rating('Алхимик') == 8

    def test_set_book_rating_if_more_than_10_rating_one(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.set_book_rating(name='Тестирование Дот Ком', rating=11)
        assert collector.get_book_rating('Тестирование Дот Ком') == 1

    def test_set_book_rating_if_less_than_1_rating_one(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.set_book_rating(name='Тестирование Дот Ком', rating=0)
        assert collector.get_book_rating('Тестирование Дот Ком') == 1

    def test_set_book_rating_if_book_not_added_cannot_set_rating(self):
        collector = BooksCollector()
        collector.set_book_rating(name='Думай медленно, решай быстро', rating=5)
        assert collector.get_book_rating('Думай медленно, решай быстро') is None

    def test_get_books_with_specific_rating_returned_list_is_equal_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('Думай медленно, решай быстро')
        collector.set_book_rating(name='Алхимик', rating=8)
        collector.set_book_rating(name='Тестирование Дот Ком', rating=9)
        collector.set_book_rating(name='Думай медленно, решай быстро', rating=9)
        assert collector.get_books_with_specific_rating(9) == ['Тестирование Дот Ком', 'Думай медленно, решай быстро']

    def test_get_books_with_specific_rating_if_no_rating_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_rating(name='Алхимик', rating=8)
        assert len(collector.get_books_with_specific_rating(9)) == 0

    def test_add_book_in_favorites_list_appends_with_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('Думай медленно, решай быстро')
        collector.add_book_in_favorites('Тестирование Дот Ком')
        collector.add_book_in_favorites('Думай медленно, решай быстро')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorite_if_book_not_in_books_rating_than_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Тихий Дон')
        collector.add_book_in_favorites('Война и мир')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_the_book_deletes_from_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('Думай медленно, решай быстро')
        collector.add_book_in_favorites('Алхимик')
        collector.add_book_in_favorites('Тестирование Дот Ком')
        collector.add_book_in_favorites('Думай медленно, решай быстро')
        collector.delete_book_from_favorites('Алхимик')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_if_book_not_in_favorites_list_not_changed(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('Думай медленно, решай быстро')
        collector.add_book_in_favorites('Тестирование Дот Ком')
        collector.add_book_in_favorites('Думай медленно, решай быстро')
        collector.delete_book_from_favorites('Алхимик')
        assert len(collector.get_list_of_favorites_books()) == 2
