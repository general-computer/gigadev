import unittest
import sqlite3
import os
from gigadev.database.setup import create_database, generate_developer, populate_database

class TestDatabaseSetup(unittest.TestCase):
    def setUp(self):
        """Create a test database"""
        self.test_db = 'test_gigadev.db'
        self.conn = sqlite3.connect(self.test_db)
    
    def tearDown(self):
        """Clean up test database"""
        self.conn.close()
        os.remove(self.test_db)
    
    def test_database_creation(self):
        """Test if database and table are created properly"""
        self.conn = create_database()
        cursor = self.conn.cursor()
        
        # Check if developers table exists
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='developers'
        """)
        self.assertIsNotNone(cursor.fetchone())
        
        # Check table schema
        cursor.execute("PRAGMA table_info(developers)")
        columns = cursor.fetchall()
        self.assertEqual(len(columns), 7)  # Check number of columns
        
        # Check column names
        column_names = [col[1] for col in columns]
        expected_columns = ['id', 'name', 'hometown', 'background', 
                          'strengths', 'skills', 'years_experience']
        self.assertEqual(column_names, expected_columns)
    
    def test_developer_generation(self):
        """Test if developer generation produces valid data"""
        dev = generate_developer()
        
        self.assertIsInstance(dev, dict)
        self.assertTrue(all(key in dev for key in ['name', 'hometown', 'background', 
                                                  'strengths', 'skills', 'years_experience']))
        self.assertIsInstance(dev['years_experience'], int)
        self.assertTrue(1 <= dev['years_experience'] <= 25)
    
    def test_database_population(self):
        """Test if database population works with a small number of records"""
        self.conn = create_database()
        populate_database(self.conn, num_records=10)
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM developers")
        count = cursor.fetchone()[0]
        self.assertEqual(count, 10)

if __name__ == '__main__':
    unittest.main()
