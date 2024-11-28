import sqlite3
import os
from datetime import datetime

def get_first_developer():
    """Retrieve the first developer from the database"""
    conn = sqlite3.connect('gigadev.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT name, hometown, background, strengths, skills, years_experience 
    FROM developers LIMIT 1
    ''')
    
    dev = cursor.fetchone()
    conn.close()
    
    return {
        'name': dev[0],
        'hometown': dev[1],
        'background': dev[2],
        'strengths': dev[3],
        'skills': dev[4],
        'years_experience': dev[5]
    }

def generate_prompt(dev_data):
    """Generate an inspirational prompt based on developer data"""
    prompt = f"""Imagine yourself as {dev_data['name']}, a seasoned developer with {dev_data['years_experience']} years of experience.
    
Coming from {dev_data['hometown']}, you've built an impressive career as {dev_data['background']}.
Your exceptional strengths in {dev_data['strengths']} have set you apart in the industry.
With expertise in {dev_data['skills']}, you're uniquely positioned to tackle any challenge.

As an executive looking to revolutionize the tech industry:
1. How would you leverage your diverse skill set to transform the next generation of software?
2. What innovative solutions would you propose to address current industry pain points?
3. How would your background influence your approach to building and leading high-performing teams?

Share your vision for the future of technology, drawing from your rich experience and unique perspective."""

    return prompt

def save_prompt(prompt):
    """Save the generated prompt to a timestamped file in the prompts directory"""
    if not os.path.exists('prompts'):
        os.makedirs('prompts')
        
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'prompts/prompt_{timestamp}.txt'
    
    with open(filename, 'w') as f:
        f.write(prompt)
    
    return filename

def main():
    dev_data = get_first_developer()
    prompt = generate_prompt(dev_data)
    filename = save_prompt(prompt)
    print(f"Prompt generated and saved to: {filename}")
    print("\nGenerated Prompt:\n")
    print(prompt)

if __name__ == "__main__":
    main()
