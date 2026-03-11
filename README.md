# Digital Receipt Organizer

## Overview
The Digital Receipt Organizer is a web-based application that allows users to upload, store, categorize, and view their receipts. The system supports image/PDF uploads, stores receipt metadata in a SQLite database, and displays all receipts in a searchable, filterable list. Future versions will include OCR (Optical Character Recognition) to automatically extract vendor names, dates, and amounts from uploaded receipts.

This project is being developed for CIDS 484 as a semester-long software project.

---

## Current Progress (Milestone 1)
### ✔ Project Setup
- Repository created and structured
- Initial documentation added
- Flask project scaffolded

### ✔ Working Prototype
- File upload form created
- Receipt files save to `/static/uploads/`
- SQLite database integrated
- Receipts table created via schema
- Uploaded receipts are inserted into the database
- Receipts list page added (`/receipts`)
- Individual receipt view page added (`/view/<id>`)
- Navigation bar added for easy movement between pages

### ✔ Next Steps
- Add sorting and filtering to the receipts list
- Build dashboard with spending analytics (Chart.js)
- Add edit/delete functionality
- Integrate OCR for automatic data extraction

---

## Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (development)
- **Visualization:** Chart.js (future milestone)
- **OCR:** Some kind of OCR (future milestone)

---
- Video link: [[https://2370711.kaf.kaltura.com/media/1_87ac040h](https://2370711.kaf.kaltura.com/media/Kaltura%20Capture%20recording%20-%20February%2013th%202026%2C%2010%3A33%3A15%20pm/1_87ac040h)](https://cdnapisec.kaltura.com/index.php/extwidget/preview/partner_id/2370711/uiconf_id/54949472/entry_id/1_87ac040h/embed/dynamic)
- Note: Link audio didn't work so if you need any further explaining or are doing peer review, DM and I'll be happy to answer any questions
