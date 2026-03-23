# Digital Receipt Organizer

## Overview
The Digital Receipt Organizer is a web-based application that allows users to upload, store, categorize, and view their receipts. The system supports image/PDF uploads, stores receipt metadata in a SQLite database, and displays all receipts in a searchable, filterable list. Milestone 2 expands the project with full CRUD functionality and a new analytics dashboard powered by Chart.js.

This project is being developed for CIDS 484 as a semester-long software project.

---

## Current Progress (Milestone 2)

### ✔ Core Functionality Expanded
- Full CRUD implemented (Create, Read, Update, Delete)
- Edit page added for modifying receipt details  
- Delete confirmation added for safe removal  
- Navigation updated to include Dashboard page  

### ✔ Improved Receipts List
- Sorting by date, amount, vendor, and category  
- Filtering by category  
- Search bar for vendor name  
- Cleaner table layout with action buttons  

### ✔ Dashboard & Analytics
A new `/dashboard` page was added featuring three interactive Chart.js visualizations:

- **Spending by Category (Pie Chart)**  
- **Spending by Month (Bar Chart)**  
- **Top Vendors (Horizontal Bar Chart)**  

All charts pull live aggregated data from the SQLite database.

### ✔ Code & Structure Enhancements
- Templates organized using `base.html` inheritance  
- Database queries structured for analytics  
- Static uploads folder maintained for receipt files  
- Project structure cleaned and documented  

---

## Next Steps
- Add file validation and error handling  
- Integrate OCR for automatic data extraction  
- Add user authentication (optional future milestone)  
- Add export options (CSV/PDF)  
- Expand dashboard with more analytics  

---

## Tech Stack
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **Visualization:** Chart.js  
- **OCR:** Planned for future milestone  

---

## Video Link
- Milestone 2 Link: https://cdnapisec.kaltura.com/index.php/extwidget/preview/partner_id/2370711/uiconf_id/54949472/entry_id/1_tnqz8pwg/embed/dynamic 
