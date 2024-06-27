# Django HTMX Tailwind Live Search

This repository contains a Django application that demonstrates live search functionality using HTMX for handling AJAX requests and Tailwind CSS for responsive styling. These technologies are ideal for simplifying modern web development by streamlining rapid prototyping and enhancing user experience through dynamic content updates.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)  
    - [Prerequisites](#prerequisites)  
    - [Steps](#steps)
- [Usage](#usage)
- [License](#license)

## Introduction

This project showcases how to implement a live search feature in a Django application using HTMX and Tailwind CSS. The application allows users to search and view results dynamically without reloading the page.

## Features

- Real-time search results
- Responsive design with Tailwind CSS
- Django backend with HTMX for AJAX requests
- Optimized and compressed CSS/JS using Django Compressor

## Technologies Used

- **Django**: The web framework used for the backend.
- **HTMX**: A library for handling AJAX requests and updating the DOM.
- **Tailwind CSS**: A utility-first CSS framework for styling.
- **Django Compressor**: A tool for compressing and combining CSS and JavaScript files.

## Installation

### Prerequisites

- Python 3.10+
- Django 4.2+

### Steps

1. **Clone the repository**:

    Using HTTPS:
    ```bash
    git clone https://github.com/yourusername/django-htmx-tailwind-live-search.git
    cd django-htmx-tailwind-live-search
    ```

    Using SSH:
    ```bash
    git clone git@github.com:yourusername/django-htmx-tailwind-live-search.git
    cd django-htmx-tailwind-live-search
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations**:

    ```sh
    python manage.py migrate
    ```

5. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Use the search bar to perform live searches.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
