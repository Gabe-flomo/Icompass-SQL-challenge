import unittest
import os
from app import verifySanitization


class TestSanitation(unittest.TestCase):

    def test_valid_characters(self):
        ''' this function test random input that shouldn't cause any SQL errors '''
        self.assertEqual(verifySanitization('This is a test'), 'Sanitized')
        self.assertEqual(verifySanitization(450), 'Sanitized')
        self.assertEqual(verifySanitization(4.50), 'Sanitized')
        self.assertEqual(verifySanitization(True), 'Sanitized')
        self.assertEqual(verifySanitization(['this  is a list', 'of strings']), 'Sanitized')
        self.assertEqual(verifySanitization({'This is a test': 'using a dictionary'}), 'Sanitized')
        
    def test_invalid_characters(self):
        ''' this function test input that should cause SQL errors'''
        # this just makes sure that each statement in the file is registered as unsanitized
        with open('SQL-Injection-codes.txt', 'r') as file:
            lines = file.readlines()
            lines = [line.strip("\n") for line in lines]
        
        for line in lines:
            # print(line)
            self.assertEqual(verifySanitization(line), 'Unsanitized')
        


if __name__ == '__main__':
    unittest.main()
