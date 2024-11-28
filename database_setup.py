import sqlite3
import random
from faker import Faker

def create_database():
    """Create SQLite database and developer table"""
    conn = sqlite3.connect('gigadev.db')
    cursor = conn.cursor()
    
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
    
    conn.commit()
    return conn

def generate_developer():
    """Generate a single developer record"""
    fake = Faker()
    
    skills_list = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'Go', 'Rust', 'SQL']
    strengths_list = ['Problem Solving', 'Team Leadership', 'Architecture Design', 
                     'Code Optimization', 'Mentoring', 'Project Management']
    
    return {
        'name': fake.name(),
        'hometown': fake.city(),
        'background': fake.job() + " with " + fake.company(),
        'strengths': ', '.join(random.sample(strengths_list, k=random.randint(2, 4))),
        'skills': ', '.join(random.sample(skills_list, k=random.randint(3, 6))),
        'years_experience': random.randint(1, 25)
    }

def populate_database(conn, num_records=1000000):
    """Populate database with specified number of developer records"""
    cursor = conn.cursor()
    
    for i in range(num_records):
        dev = generate_developer()
        cursor.execute('''
        INSERT INTO developers (name, hometown, background, strengths, skills, years_experience)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (dev['name'], dev['hometown'], dev['background'], 
              dev['strengths'], dev['skills'], dev['years_experience']))
        
        if i % 10000 == 0:  # Commit every 10000 records
            conn.commit()
            print(f"Inserted {i} records...")
    
    conn.commit()
    print(f"Completed inserting {num_records} records.")

if __name__ == "__main__":
    conn = create_database()
    populate_database(conn)
    conn.close()