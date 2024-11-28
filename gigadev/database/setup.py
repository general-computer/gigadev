import sqlite3
import random
import argparse
from faker import Faker

def create_database(db_path='gigadev.db'):
    """Create SQLite database and developer table"""
    conn = sqlite3.connect(db_path)
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
    """Generate random developer data"""
    fake = Faker()
    
    backgrounds = [
        'Software Engineer', 'Data Scientist', 'DevOps Engineer',
        'Full Stack Developer', 'Machine Learning Engineer',
        'Systems Architect', 'Cloud Solutions Engineer'
    ]
    
    strengths = [
        'Problem Solving', 'Team Leadership', 'System Design',
        'Code Optimization', 'Technical Architecture',
        'Agile Methodologies', 'Innovation'
    ]
    
    skills = [
        'Python', 'JavaScript', 'Java', 'Go', 'Rust',
        'AWS', 'Docker', 'Kubernetes', 'React', 'Node.js',
        'PostgreSQL', 'MongoDB', 'Redis'
    ]
    
    return {
        'name': fake.name(),
        'hometown': fake.city(),
        'background': random.choice(backgrounds),
        'strengths': ', '.join(random.sample(strengths, 2)),
        'skills': ', '.join(random.sample(skills, 3)),
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
    parser = argparse.ArgumentParser(description='Setup developer database')
    parser.add_argument('--quick', action='store_true', 
                       help='Quick mode: only generate 10,000 records')
    args = parser.parse_args()

    conn = create_database()
    num_records = 10000 if args.quick else 1000000
    populate_database(conn, num_records)
    conn.close()
