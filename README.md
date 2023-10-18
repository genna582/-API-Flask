1. Разработка RECT API предоставляющая возможность ведение блога
2. Сущности:

    2.1. пользователь.

    2.2. пост.

    2.3. комментарий.
3. Пользователь имеет возможность:

    3.1. Создать, прочитать, изменить и удалить пост.

    3.2. Получить список всех постов.

    3.3. Добавить и удалить комментарии к посту# -API-Flask

добавить пост:

    # {"body": "my first post", "author": "@genna582", "comment": " "}
    
    # {"body": "my second post","author": "@genna582", "comment": " "}

добавить комментарии:

	localhost:5000/post/0

    # {"comment": "first post good"}

	localhost:5000/post/1
	
    # {"comment": "second post good"}

удалить пост:

	localhost:5000/post/0

	localhost:5000/post/1