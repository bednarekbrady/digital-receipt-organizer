"""
OCR Processing Module for Digital Receipt Organizer
Extracts vendor, amount, and date information from receipt images using EasyOCR.
"""

import easyocr
import re
from datetime import datetime
from pathlib import Path

# Initialize OCR reader (loads model on first use)
_reader = None

def get_reader():
    """Lazy-load the OCR reader to avoid unnecessary model loading."""
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(['en'], gpu=False)
    return _reader

def extract_text_from_image(image_path):
    """
    Extract all text from an image using EasyOCR.
    
    Args:
        image_path (str): Path to the receipt image
        
    Returns:
        list: List of tuples (text, confidence) from OCR
    """
    try:
        reader = get_reader()
        results = reader.readtext(image_path)
        # Return text and confidence scores
        return [(text, confidence) for (_, text, confidence) in results]
    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return []

def extract_amount(text_list):
    """
    Extract the most likely amount/total from receipt text.
    Looks for currency amounts ($ or numbers with 2 decimals).
    
    Args:
        text_list (list): List of text strings from OCR
        
    Returns:
        dict: {value: float/None, confidence: float}
    """
    all_text = " ".join([text for text, _ in text_list])
    
    # Patterns for currency amounts
    patterns = [
        r'\btotal[:\s]+\$?([\d,]+\.?\d{0,2})\b',  # "Total: $123.45"
        r'\bsubtotal[:\s]+\$?([\d,]+\.?\d{0,2})\b',  # "Subtotal: 123.45"
        r'\$?([\d,]+\.\d{2})\b',  # Generic currency format
    ]
    
    amounts = []
    for pattern in patterns:
        matches = re.findall(pattern, all_text, re.IGNORECASE)
        for match in matches:
            # Parse and clean the amount
            amount_str = match.replace(',', '')
            try:
                amount = float(amount_str)
                if amount > 0:  # Only positive amounts
                    amounts.append(amount)
            except ValueError:
                continue
    
    if amounts:
        # Return the largest amount (likely the total)
        return {"value": max(amounts), "confidence": 0.7}
    
    return {"value": None, "confidence": 0.0}

def extract_date(text_list):
    """
    Extract the most likely purchase date from receipt text.
    Looks for common date formats.
    
    Args:
        text_list (list): List of text strings from OCR
        
    Returns:
        dict: {value: 'YYYY-MM-DD' or None, confidence: float}
    """
    all_text = " ".join([text for text, _ in text_list])
    
    # Common date patterns
    date_patterns = [
        # MM/DD/YYYY or MM/DD/YY
        (r'(\d{1,2})[/\-](\d{1,2})[/\-](\d{2,4})', 'mdy'),
        # YYYY-MM-DD
        (r'(\d{4})[/\-](\d{1,2})[/\-](\d{1,2})', 'ymd'),
        # Month DD, YYYY (e.g., "Dec 25, 2023")
        (r'([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})', 'mdy_text'),
    ]
    
    for pattern, date_format in date_patterns:
        matches = re.findall(pattern, all_text)
        for match in matches:
            try:
                if date_format == 'mdy':
                    month, day, year = match
                    year = int(year)
                    # Handle 2-digit years
                    if year < 100:
                        year = 2000 + year if year < 30 else 1900 + year
                    date_obj = datetime(year, int(month), int(day))
                elif date_format == 'ymd':
                    year, month, day = match
                    date_obj = datetime(int(year), int(month), int(day))
                elif date_format == 'mdy_text':
                    month_str, day, year = match
                    date_obj = datetime.strptime(f"{month_str} {day} {year}", "%B %d %Y")
                    # Try abbreviated month if full name fails
                    try:
                        pass
                    except ValueError:
                        date_obj = datetime.strptime(f"{month_str} {day} {year}", "%b %d %Y")
                
                # Return if date is reasonable (not too far in past/future)
                if 2020 <= date_obj.year <= 2030:
                    return {"value": date_obj.strftime("%Y-%m-%d"), "confidence": 0.8}
            except (ValueError, IndexError):
                continue
    
    return {"value": None, "confidence": 0.0}

def extract_vendor(text_list):
    """
    Extract the most likely vendor/store name from receipt text.
    Typically found at the top of the receipt and is often repeated.
    
    Args:
        text_list (list): List of (text, confidence) tuples from OCR
        
    Returns:
        dict: {value: str or None, confidence: float}
    """
    # Get top lines (vendor usually near top)
    top_text = [text for text, conf in text_list[:10]]
    
    # Filter out common receipt words to isolate vendor name
    common_words = {
        'receipt', 'thank', 'you', 'visit', 'welcome', 'please',
        'total', 'amount', 'change', 'cash', 'card', 'date', 'time',
        'for', 'your', 'business', 'and', 'our', 'www', 'http',
        'the', 'a', 'of', 'in', 'to', 'at', '#', '-', '--'
    }
    
    candidates = []
    for text in top_text:
        if len(text) > 2 and not all(word.lower() in common_words for word in text.split()):
            # Score based on position (earlier = higher) and length
            candidates.append(text.strip())
    
    if candidates:
        # Return the first substantial text that's not filtered
        vendor = candidates[0]
        if len(vendor) > 3:
            return {"value": vendor, "confidence": 0.6}
    
    return {"value": None, "confidence": 0.0}

def process_receipt(image_path):
    """
    Main function to process a receipt image and extract key information.
    
    Args:
        image_path (str): Path to the receipt image
        
    Returns:
        dict: Extracted receipt data with confidence scores
              {
                  'vendor': {'value': str, 'confidence': float},
                  'amount': {'value': float, 'confidence': float},
                  'date': {'value': str (YYYY-MM-DD), 'confidence': float},
                  'raw_text': list of tuples (text, confidence)
              }
    """
    # Verify file exists
    if not Path(image_path).exists():
        return {
            'vendor': {'value': None, 'confidence': 0.0},
            'amount': {'value': None, 'confidence': 0.0},
            'date': {'value': None, 'confidence': 0.0},
            'raw_text': [],
            'error': 'Image file not found'
        }
    
    # Extract all text from image
    text_list = extract_text_from_image(image_path)
    
    # Extract specific fields
    vendor = extract_vendor(text_list)
    amount = extract_amount(text_list)
    date = extract_date(text_list)
    
    return {
        'vendor': vendor,
        'amount': amount,
        'date': date,
        'raw_text': text_list,
        'error': None if text_list else 'No text detected in image'
    }
