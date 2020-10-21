import unittest
from Task_3 import login


class TestYandexAPI(unittest.TestCase):
    def setUp(self):
        print('--> Тестирование начинается.\n')

    def test_authorization(self):
        self.assertTrue(login('your_login', 'your_password'))

    def tearDown(self):
        print('Тестирование заверешено.\n\n')


if __name__ == '__main__':
    unittest.main()
