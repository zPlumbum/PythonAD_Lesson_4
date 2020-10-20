import unittest
from main import get_person, add_document, del_document


class TestDocuments(unittest.TestCase):
    def setUp(self):
        print('--> Тестирование начинается.\n')

    def test_get_person(self):
        self.assertEqual(get_person('10006'), 'Аристарх Павлов')

    def test_add_document(self):
        self.assertTrue(add_document('passport', '12345', 'Vasiliy', '1'))

    def test_delete_document(self):
        self.assertTrue(del_document('2207 876234'))

    def tearDown(self):
        print('Тестирование заверешено.\n\n')


if __name__ == '__main__':
    unittest.main()
