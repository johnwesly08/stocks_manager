# Stock Management System

## Overview
The **Stock Management System** is a web application built with Flask that allows users to efficiently manage inventory, track stock levels, and generate reports. It supports product addition, deletion, updating, and viewing, along with user authentication and role-based access control

## Features
- **User Authentication & Authorization** (Admin, Manager, Staff)
- **Add, Update, and Delete Products**
- **Track Stock Levels**
- **Generate Reports (Stock Status, Low Stock Alerts, Sales Reports)**
- **Search & Filter Products**
- **RESTful API for Integration**
- **Responsive UI with Bootstrap**

## Technologies Used
- **Backend:** Flask, Flask-RESTful, Flask-SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript

## Installation
### Prerequisites
- Python 3.x installed
- Virtual environment (optional but recommended)

### Steps to Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/stock-management.git
   cd stock-management
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set environment variables:
   ```sh
   export FLASK_APP=app.py
   export FLASK_ENV=development  # For development mode
   ```
5. Initialize the database:
   ```sh
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
6. Run the application:
   ```sh
   flask run
   ```
7. Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|--------------|
| GET | /api/products | Get all products |
| GET | /api/products/<id> | Get product by ID |
| POST | /api/products | Add a new product |
| PUT | /api/products/<id> | Update a product |
| DELETE | /api/products/<id> | Delete a product |

## Folder Structure
```
stock-management/
│-- app.py              # Main application file
│-- config.py           # Configuration settings
│-- models.py           # Database models
│-- routes.py           # API routes
│-- templates/          # HTML templates
│-- static/             # CSS, JavaScript, Images
│-- migrations/         # Database migrations
│-- requirements.txt    # Dependencies
│-- README.md           # Project documentation
```

## Future Enhancements
- Role-based dashboard
- Barcode scanning for stock management
- Advanced analytics and reports
- Multi-user access with permissions

## License
This project is licensed under the MIT License.

## Contributors
- **John Wesly P D** - [GitHub Profile](https://github.com/johnwesly08)

## Acknowledgments
- Flask Official Documentation

