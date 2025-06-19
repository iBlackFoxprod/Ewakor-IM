# EWAKOR Inventory Management System

A local inventory and stock management system for EWAKOR, designed to run on a local network.

## Features

- User authentication with role-based access (Admin, Staff)
- Product management (add, edit, delete)
- Stock level tracking
- Incoming stock management
- Outgoing product tracking
- Low stock alerts
- Dashboard with visual status
- Multi-device access via local network

## Setup Instructions

1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   python init_db.py
   ```
4. Run the application:
   ```bash
   python run.py
   ```
5. Access the application:
   - On the host machine: http://localhost:5000
   - On other devices in the same network: http://<host-ip>:5000

## Default Admin Account

- Username: admin@ewakor.com
- Password: admin123

**Important**: Change the default password after first login!

## System Requirements

- Python 3.8+
- Modern web browser
- Local network connection 