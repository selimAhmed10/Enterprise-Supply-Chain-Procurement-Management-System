# SCM Pro - Enterprise Supply Chain & Procurement Management System

## Overview
SCM Pro is a comprehensive web-based ERP system designed to digitize and automate the complete supply chain and procurement lifecycle.

## Project Structure
\\\
~/scm/scm_project/
├── backend/                    # Django API
│   ├── apps/                   # All Django Apps
│   ├── core/                   # Shared Utilities
│   ├── scm_pro/                # Django Config
│   └── media/                  # User Uploads
├── frontend/                   # React UI
├── docs/                       # Documentation
├── scripts/                    # Utility Scripts
└── docker-compose.yml          # Docker Setup
\\\

## Quick Start
\\\ash
cd backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\\\

## License
MIT
