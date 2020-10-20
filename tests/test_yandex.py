import unittest
from Task_2 import add_yandex_folder


class TestYandexAPI(unittest.TestCase):
    def setUp(self):
        print('--> Тестирование начинается.\n')

    def test_add_yandex_folder(self):
        print('*Проверка на создание папки*')
        self.assertEqual(add_yandex_folder('Example Folder'), 201)

    def test_wrong_not_authorized(self):
        print('*Проверка на ошибку*')
        print('Вы не аторизованы.')
        self.assertEqual(add_yandex_folder('disk:/example'), 401)

    def test_wrong_folder_exists(self):
        print('*Проверка на ошибку*')
        print('Ресурс с таким путем уже существует.')
        self.assertEqual(add_yandex_folder('disk:/example'), 409)

    def tearDown(self):
        print('Тестирование заверешено.\n\n')


if __name__ == '__main__':
    unittest.main()
