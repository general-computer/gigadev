import unittest
import os
import sqlite3
from gigadev.prompts.generator import get_first_developer, generate_prompt, save_prompt
from datetime import datetime

class TestPromptGenerator(unittest.TestCase):
    """
    Test suite for the prompt generator functionality.
    As a clinical molecular geneticist turned developer, I understand the importance
    of thorough testing and validation.
    """
    
    def setUp(self):
        """
        Initialize test environment with a sample database.
        Using my background in precise laboratory protocols, I ensure consistent test conditions.
        """
        # Create test database
        self.test_db = 'test_gigadev.db'
        self.conn = sqlite3.connect(self.test_db)
        cursor = self.conn.cursor()
        
        # Create developers table with test data
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS developers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL,
            background TEXT NOT NULL,
            strengths TEXT NOT NULL,
            skills TEXT NOT NULL,
            years_experience INTEGER NOT NULL
        )
        ''')
        
        # Insert test developer data
        cursor.execute('''
        INSERT INTO developers (name, hometown, background, strengths, skills, years_experience)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Test Developer', 'Tech City', 'Software Architect', 
              'Problem Solving, Leadership', 'Python, Java, SQL', 10))
        
        self.conn.commit()
    
    def tearDown(self):
        """Clean up test artifacts"""
        self.conn.close()
        os.remove(self.test_db)
        # Clean up any test prompts if the directory exists
        if os.path.exists('prompts'):
            for file in os.listdir('prompts'):
                if file.startswith('test_prompt_'):
                    os.remove(os.path.join('prompts', file))
    
    def test_get_first_developer(self):
        """
        Test developer data retrieval.
        With my experience in data handling, I ensure proper data structure and completeness.
        """
        dev_data = get_first_developer()
        
        self.assertIsInstance(dev_data, dict)
        required_fields = ['name', 'hometown', 'background', 'strengths', 'skills', 'years_experience']
        for field in required_fields:
            self.assertIn(field, dev_data)
            self.assertIsNotNone(dev_data[field])
    
    def test_generate_prompt(self):
        """
        Test prompt generation logic.
        Drawing from my mentoring experience, I verify the prompt's motivational aspects.
        """
        test_data = {
            'name': 'Test Developer',
            'hometown': 'Tech City',
            'background': 'Software Architect',
            'strengths': 'Problem Solving, Leadership',
            'skills': 'Python, Java, SQL',
            'years_experience': 10
        }
        
        prompt = generate_prompt(test_data)
        
        # Verify all components are present
        self.assertIn(test_data['name'], prompt)
        self.assertIn(str(test_data['years_experience']), prompt)
        self.assertIn(test_data['hometown'], prompt)
        self.assertIn(test_data['background'], prompt)
        self.assertIn(test_data['strengths'], prompt)
        self.assertIn(test_data['skills'], prompt)
        
        # Verify executive focus
        self.assertIn("executive", prompt.lower())
        self.assertIn("revolutionize", prompt.lower())
    
    def test_save_prompt(self):
        """
        Test prompt saving functionality.
        Using my architecture design skills to verify proper file handling.
        """
        test_prompt = "Test prompt content"
        filename = save_prompt(test_prompt)
        
        # Verify file creation and content
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, test_prompt)
        
        # Verify filename format
        self.assertTrue(filename.startswith('prompts/prompt_'))
        self.assertTrue(filename.endswith('.txt'))

if __name__ == '__main__':
    unittest.main()
