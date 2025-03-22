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

![Login Page](screenshots/login.png)
![Dashboard](screenshots/dashboard.png)
![CV Form](screenshots/cv_form.png)
![Generated PDF](screenshots/pdf.png)

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

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/portfolio-generator.git
   cd portfolio-generator
