# -*- coding: utf-8 -*-
"""


@author: taylor headen
COMP651 Assignment 5
"""
import os
import unittest
from datetime import datetime
from assignment5 import create_database, students_of_age, average_age

class TestMyDataBase(unittest.TestCase):

    def setUp(self):
        """Creates a new database 
        
        setUp() method can simply call assignment5.create_database()
        
        ARGS:
            self: instance of the assingment5 object
        
        RETURNS:
            none
        """
        create_database()

    def tearDown(self):
        """Deletes the database file 
        
        The tearDown() method can use the remove()
        function from the os module to delete mydatabase.db. And it should write an entry in the file 
        log.txt.
        
        ARGS:
            self: instance of the assingment5 object
        
        RETURNS:
            none
        """
        os.remove('mydatabase.db')

        with open('log.txt', 'a') as f:
            f.write(f'{self.id()}, {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

    def test_students_of_age(self):
        """Test function
        
        Tests the students_of_age function by checking the output for the age of 26.
        
        ARGS:
            self: instance of the assingment5 object
        
        RETURNS:
            none
        """
        expected = ['Jordan', 'Jonathan']
        result = students_of_age(26)
        self.assertListEqual(result, expected)

    def test_average_age(self):
        """ Test function
        
        Tests the average_age function by checking the output against the expected value.
        
        ARGS:
            self: instance of the assingment5 object
        
        RETURNS:
            none
        """
        expected = 25.83
        result = average_age()
        self.assertAlmostEqual(result, expected, places=2)

if __name__ == '__main__':
    unittest.main()