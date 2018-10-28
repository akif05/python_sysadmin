import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    # Since all methods are in same class, we can use setup method
    # to initial setup for all methods,
    # All methods are going to share thise setUp() method
    def setUp(self):
        self.phonebook = Phonebook()

    # The mothod is no longa needed, because setUp() method replaced it
    # def test_create_phonebook(self):
    #    phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        # phonebook = Phonebook()
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self):
        # phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # WIP means 'work in progress', This will skipp the next test
    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        #phonebook = Phonebook()
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("Poor example")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "123")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_another_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_add_names_and_numbers(self):
        self.phonebook.add("Sue", "12345")
        self.assertIn("Sue", phonebook.get_names())
        self.assertIn("12345", phonebook.get_numbers())

    # This metod can be used to clear the memmory even if the previpus
    # method fails.
    #def tearDown(self):
    #    pass