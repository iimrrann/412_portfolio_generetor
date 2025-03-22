# Portfolio Generator

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

The **Portfolio Generator** is a web application built with Django that allows users to create and manage their professional portfolios. Users can log in, fill out their personal information, skills, education, work experience, and projects, and generate a PDF version of their portfolio.

---

## Features

- **User Authentication**: Register, log in, and log out securely.
- **Portfolio Creation**:
  - Add personal information (name, contact info, bio, photo).
  - Add skills, education, work experience, and projects.
  - Save progress and update information later.
- **PDF Generation**: Generate a professional PDF version of the portfolio.
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices.

---

## Screenshots

-provided in folder : \portfolio_generator\demo\
---

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default)
- **PDF Generation**: xhtml2pdf
- **Static Files**: Django Static Files
- **Authentication**: Django's built-in authentication system

---

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation
. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/portfolio-generator.git
   cd portfolio-generator
###File structure

portfolio-generator/
├── cv_generator/              # Django app for portfolio management
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS, images)
│   ├── templates/             # HTML templates
│   ├── admin.py               # Admin configuration
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # App-specific URLs
├── portfolio_generator/       # Django project settings
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project URLs
│   ├── wsgi.py                # WSGI configuration
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation

### Usage
Register or Log In:

Register a new account or log in if you already have one.

Fill Out Your Portfolio:

Navigate to the Create CV page.

Fill out your personal information, skills, education, work experience, and projects.

Save your progress or generate a PDF.

Generate PDF:

Click the Save and Generate PDF button to download your portfolio as a PDF.

### Contribution : MD. IMRAN KHAN   2021-3-60-206
