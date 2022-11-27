# qa_python
Реализованные тесты:
Метод __init__:
1. test_init_books_rating_takes_key_and_value - проверяем, что словарь с названием книги и рейтингом пополняется;
2. test_init_list_of_favorites_books_add_values - проверяем, что список избранных книг пополняется

Метод add_new_book:
1. test_add_new_book_add_two_books - проверяем, что можем добавить 2 книги;
2. test_add_new_book_similar_books_dont_add - проверяем, что одну и ту же книгу дважды мы добавить не можем
3. Здесь же мы проверяем метод get_books_rating

Метод set_book_rating:
1. test_set_book_rating_if_between_1_and_10_inclusive_rating_true - проверяем, что рейтинг книги устанавливается, если он
    в промежутке от 1 до 10 включительно;
2. test_set_book_rating_if_more_than_10_rating_one - проверяем, что в случае, когда рейтинг больше 10, выставляется
    изначальный рейтинг 1;
3. test_set_book_rating_if_less_than_1_rating_one - проверяем, что в случае, когда рейтинг меньше 1, выставляется 
    изначальный рейтинг 1
4. test_set_book_rating_if_book_not_added_cannot_set_rating - проверяем, что если книга не добавлена, не можем выставить рейтинг.
    Здесь же проверяем, что у недобавленной книги нет рейтинга
5. В этих же тестах проверяем метод get_book_rating (позитивные тесты и 1 негативный)

Метод get_books_with_specific_rating:
1. test_get_books_with_specific_rating_returned_list_is_equal_rating - проверяем, что выводится список книг согласно указанному рейтингу
2. test_get_books_with_specific_rating_if_no_rating_list_is_empty - проверяем, что список книг пуст, если указанного рейтинга нет

Метод add_book_in_favorites:
1. test_add_book_in_favorites_list_appends_with_book_name - проверяем, что книги добавляются в список избранных
2. test_add_book_in_favorite_if_book_not_in_books_rating_than_not_added - проверяем, что книги не добавляются в список избранных, если их нет в словаре books_rating
3. Здесь же мы проверяем метод get_list_of_favorites_books (позитивная и негативная проверка)

Метод delete_book_from_favorites:
1. test_delete_book_from_favorites_the_book_deletes_from_favorites_list - проверяем, что книгу можно удалить из избранного, если она там есть
2. test_delete_book_from_favorites_if_book_not_in_favorites_list_not_changed - проверяем, что список избранного не меняется, если мы удаляем из списка избранных книгу, которой в этом списке не было


