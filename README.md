# Digital Receipt Organizer

## 📋 Overview

The **Digital Receipt Organizer** is a web-based application that streamlines receipt management. Users can upload receipt images, automatically extract data using AI-powered OCR, store receipts in an organized database, and analyze spending patterns through an interactive dashboard.

**Status:** Alpha Release (Milestone 3)  
**Course:** CIDS 484 - Semester-long Software Project  
**Last Updated:** April 2026

---

##  Alpha Release Features

### 1. **Receipt Upload & OCR Extraction**  NEW
- Upload receipt images (JPG, PNG, GIF, BMP, TIFF)
- **Automatic data extraction** using EasyOCR AI
  - Vendor/store name detection
  - Total amount recognition
  - Transaction date extraction
- Confidence scores displayed for each extracted field
- Users can edit extracted values before saving
- Fallback to manual entry if OCR extraction fails

### 2. **Full CRUD Operations**
- ✅ **Create:** Upload and save receipts with metadata
- ✅ **Read:** View all receipts in searchable list or individual receipt details
- ✅ **Update:** Edit receipt information (vendor, amount, date, category)
- ✅ **Delete:** Remove receipts with confirmation dialog

### 3. **Smart Receipt Management**
- **Search:** Find receipts by vendor name
- **Filter:** Filter receipts by category
- **Sort:** Sort receipts by date (newest/oldest), amount (highest/lowest), vendor name, or category
- **Categories:** Organize receipts (Food, Gas, Shopping, etc.)

### 4. **Analytics Dashboard**
Ray interactive charts powered by Chart.js:
- **Spending by Category** - Pie chart showing expense breakdown
- **Spending by Month** - Bar chart tracking trends over time
- **Top Vendors** - Horizontal bar chart of most frequent stores
- All visualizations update dynamically as receipts are added/modified

### 5. **User-Friendly Interface**
- Clean, responsive Bootstrap design
- Intuitive navigation menu
- Receipt image preview
- Mobile-ready layout

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Setup

1. **Clone or download the repository**
   ```bash
   cd digital-receipt-organizer
   ```

2. **Install required packages**
   ```bash
   pip install Flask EasyOCR Pillow
   ```
   
   Or install them individually:
   - Flask (web framework)
   - EasyOCR (optical character recognition)
   - Pillow (image processing)

3. **Initialize the database**
   ```bash
   python src/init_db.py
   ```
   This creates the SQLite database and prepares the receipts table.

4. **Run the application**
   ```bash
   python src/app.py
   ```
   
   The app will be available at: `http://localhost:5000`

### File Structure
```
digital-receipt-organizer/
├── src/
│   ├── app.py                 # Flask application & route handlers
│   ├── ocr_processor.py       # OCR extraction logic (EasyOCR)
│   ├── init_db.py             # Database initialization
│   ├── schema.sql             # Database schema
│   ├── static/
│   │   └── uploads/           # Stored receipt images
│   └── templates/
│       ├── base.html          # Base template (navigation, styling)
│       ├── upload.html        # Receipt upload & OCR extraction
│       ├── receipts.html      # Receipt list view
│       ├── view_receipt.html  # Individual receipt details
│       ├── edit.html          # Receipt editing
│       └── dashboard.html     # Analytics & charts
├── OCR_IMPLEMENTATION.md      # OCR integration details
├── .gitignore
├── database.db                # SQLite database (generated on first run)
└── README.md                  # This file
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3 + Flask |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Database** | SQLite |
| **AI/OCR** | EasyOCR (leverages deep learning) |
| **Charts** | Chart.js |
| **Template Engine** | Jinja2 |

---

## Key Technical Highlights

### OCR Integration (Milestone 3 Focus)
- Uses EasyOCR for robust character recognition
- Handles multiple receipt formats and quality levels
- Provides confidence scoring (0-100%) for extracted data
- Lazy-loads OCR model for performance
- Cleans temporary files after processing

### Database Schema
- **receipts table:** Stores vendor, amount, date, category, file path, and timestamps
- Indexed for efficient searching and filtering
- Prepared for multi-user support (future milestone)

### API Endpoints
- `POST /api/extract-receipt` - OCR extraction endpoint
- Additional CRUD endpoints for receipt management

---

## Demonstration Video for Current Milestone

For a video walkthrough of features and OCR extraction in action, see Milestone 3 video:(https://cdnapisec.kaltura.com/index.php/extwidget/preview/partner_id/2370711/uiconf_id/54949472/entry_id/1_yo8gspio/embed/dynamic)

### Features Demonstrated:
1. Uploading a receipt image
2. Auto-extraction of vendor, amount, and date
3. Editing extracted data before saving
4. Viewing and searching receipts
5. Analytics dashboard in action
6. Sorting and filtering receipts

---

## Possible Future Enhancements (Doubtful I'll be able to get to all)

### Phase 2 (Planned)
- User authentication & multi-user support
- Export receipts to CSV/PDF
- Receipt image compression & optimization
- Advanced date parsing for non-English receipts
- Recurring receipt patterns & budgeting

### Phase 3 (Planned)
- Mobile app (React Native)
- Cloud storage integration (AWS S3)
- Receipt receipt template matching
- Expense predictions & ML-based categorization
- Integration with accounting software

---

## Known Limitations & Notes

- OCR accuracy depends on receipt image quality (clearer images = better extraction)
- Handwritten receipts may have lower extraction accuracy
- Currently single-user (authentication planned for future milestone)
- Receipts stored locally in SQLite (cloud backup planned)

---

## Development Notes

### Database
- Use `src/init_db.py` to reset the database if needed
- All receipt files are stored in `src/static/uploads/`

### Running Tests
```bash
python -m pytest  # When test suite is added
```

### Building for Production
The application uses Flask's development server. For production deployment:
- Use Gunicorn: `gunicorn -w 4 src.app:app`
- Set up reverse proxy (Nginx)
- Configure environment variables for security

---

## Contributors

- **Developer:** [Brady Bednarek]
- **Course:** CIDS 484

---

## License

This project is open source and available for educational purposes.

---

## Questions

For issues, questions, or feature requests, please refer to the project documentation or message me.

---

**Last Updated:** April 2026 | **Project Status:** Active Development
