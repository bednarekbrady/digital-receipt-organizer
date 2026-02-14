# Digital Receipt Organizer — Project Outline

## 1. Project Overview
The Digital Receipt Organizer is a web application designed to help users upload, store, categorize, and analyze their receipts. Users can upload receipt images or PDFs, enter metadata such as vendor, amount, and category, and view all receipts in a searchable list. The system stores all receipt data in a SQLite database and provides a clean interface for browsing and viewing uploaded receipts. Future milestones will introduce OCR (Optical Character Recognition) to automatically extract receipt information.

---

## 2. Goals
- Build a functional receipt management system
- Allow users to upload receipt images/PDFs
- Store receipt metadata in a database
- Display receipts in a searchable, filterable table
- Provide visual spending analytics (category breakdown, monthly totals)
- Design the system so OCR can be added later without major redesign

---

## 3. Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (development)
- **Visualization:** Chart.js (future milestone)
- **OCR:** Looking into some currently (future milestone)

---

## 4. System Components
### ✔ Receipt Upload Module (Completed in Milestone 1)
- Upload form for vendor, amount, date, category, and file
- Saves uploaded files to `/static/uploads/`

### ✔ Database Layer (Completed in Milestone 1)
- SQLite database with `receipts` table
- Insert and fetch operations implemented

### ✔ Receipt List Interface (Completed in Milestone 1)
- Displays all receipts in a table
- Includes vendor, amount, date, category, and view button

### ✔ Receipt Viewer (Completed in Milestone 1)
- Displays full receipt details
- Shows uploaded image/PDF

### Dashboard & Analytics (Upcoming)
- Category breakdown
- Monthly spending trends
- Vendor summaries

### OCR Extraction Module (Future Milestone)
- Automatically extract vendor, amount, and date from receipt images
- Pre-fill upload form fields

---
