"""
Populate database with fake receipts and placeholder images for demo purposes.
Run this script to generate realistic test data.
"""

import sqlite3
import os
from datetime import datetime, timedelta
import random
from PIL import Image, ImageDraw, ImageFont

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.db')
UPLOAD_FOLDER = 'static/uploads'

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Sample data
VENDORS = [
    "Whole Foods", "Trader Joe's", "Costco", "Walmart", "Target",
    "Shell Gas Station", "Chevron", "Exxon Mobil", "BP Gas",
    "Starbucks", "Taco Bell", "Chipotle", "Panera Bread", "Subway",
    "McDonald's", "Burger King", "Chick-fil-A", "Wendy's",
    "Best Buy", "Microcenter", "Amazon Fresh", "CVS Pharmacy",
    "Walgreens", "Home Depot", "Lowe's", "Ace Hardware",
    "Apple Store", "Nike", "Adidas", "Gap", "H&M",
    "Pizza Hut", "Domino's", "Olive Garden", "Applebee's",
    "Netflix", "Spotify", "Gym Membership", "UberEats"
]

CATEGORIES = ["Food", "Gas", "Shopping", "Electronics", "Home", "Subscription"]

def generate_placeholder_image(vendor_name, amount):
    """Generate a simple placeholder receipt image."""
    # Create image
    width, height = 400, 600
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 24)
        text_font = ImageFont.truetype("arial.ttf", 16)
        total_font = ImageFont.truetype("arial.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        total_font = ImageFont.load_default()
    
    # Draw border
    draw.rectangle([10, 10, width-10, height-10], outline='black', width=2)
    
    # Draw header
    draw.text((20, 30), "RECEIPT", fill='black', font=title_font)
    draw.line((20, 60, width-20, 60), fill='black', width=1)
    
    # Draw vendor name
    draw.text((20, 80), f"Store: {vendor_name}", fill='black', font=text_font)
    
    # Draw some fake items
    draw.text((20, 130), "Item 1 ........... $12.99", fill='black', font=text_font)
    draw.text((20, 160), "Item 2 ........... $8.50", fill='black', font=text_font)
    draw.text((20, 190), "Item 3 ........... $5.25", fill='black', font=text_font)
    
    # Draw separator
    draw.line((20, 220, width-20, 220), fill='black', width=1)
    
    # Draw total
    draw.text((20, 250), f"TOTAL: ${amount:.2f}", fill='black', font=total_font)
    
    # Draw footer
    draw.text((20, 300), "Thank you for shopping!", fill='gray', font=text_font)
    draw.text((20, 330), "Please keep your receipt", fill='gray', font=text_font)
    
    return img

def populate_database(num_receipts=50):
    """Generate and insert fake receipt data."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print(f"Generating {num_receipts} fake receipts...")
    
    # Generate dates from last 6 months
    start_date = datetime.now() - timedelta(days=180)
    
    for i in range(num_receipts):
        # Random data
        vendor = random.choice(VENDORS)
        category = random.choice(CATEGORIES)
        amount = round(random.uniform(5.00, 250.00), 2)
        days_ago = random.randint(0, 180)
        receipt_date = (start_date + timedelta(days=days_ago)).strftime('%Y-%m-%d')
        
        # Generate placeholder image
        img = generate_placeholder_image(vendor, amount)
        filename = f"receipt_{i+1:03d}.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        img.save(filepath)
        
        # Insert into database
        cursor.execute("""
            INSERT INTO receipts (vendor, amount, date, category, file_path)
            VALUES (?, ?, ?, ?, ?)
        """, (vendor, amount, receipt_date, category, filepath))
        
        if (i + 1) % 10 == 0:
            print(f"  Generated {i + 1} receipts...")
    
    conn.commit()
    conn.close()
    
    print(f"✓ Successfully populated database with {num_receipts} receipts!")
    print(f"✓ Placeholder images saved to: {UPLOAD_FOLDER}")

if __name__ == '__main__':
    populate_database(50)
