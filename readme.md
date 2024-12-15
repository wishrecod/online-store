# Online Clothing Store Project

Welcome to the **Online Clothing Store**, a portfolio project showcasing a modern e-commerce platform built with Django. This project demonstrates the implementation of key e-commerce features, including a dynamic product catalog, user authentication, shopping cart, and order processing.

## Features

### General
- Fully responsive design with a minimalist dark theme.
- Backend powered by Django with a RESTful API architecture.

### User Features
- **User Authentication**: Login, registration, and password reset functionality.
- **Product Catalog**: Browse products with search and filtering options by categories.
- **Product Details**: View detailed information about each product.
- **Shopping Cart**: Add, remove, and manage products in the cart with real-time updates.
- **Order History**: View past orders with detailed summaries.
- **Order Placement**: Seamless transition from cart to checkout.

### Admin Features
- **Admin Dashboard**: Manage products, categories, and orders.
- **Order Management**: Update order statuses and mark payments as completed.

### Additional Functionalities
- **WebSocket Integration**: Real-time cart updates using WebSockets.
- **Pagination**: Efficient product listing with paginated views.
- **Dynamic Search**: Live search and filter functionality.
- **File Uploads**: Supports adding product images through the admin panel.

## Technologies Used

### Backend
- Django (Python)
- Django REST Framework

### Database
- SQLite (can be replaced with PostgreSQL/MySQL for production)

### Other
- WebSockets for real-time features
- Git and GitHub for version control

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/online-clothing-store.git
   cd online-clothing-store
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Navigate to `http://127.0.0.1:8000/` in your browser.

## Usage

- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage products and orders.
- Register as a new user to explore the shopping cart and order placement functionality.

## Project Structure

```
├── cart
│   ├── models.py
│   ├── views.py
│   └── templates/cart
├── products
│   ├── models.py
│   ├── views.py
│   └── templates/products
├── static
│   ├── css
│   └── images
├── templates
│   ├── base.html
│   ├── home.html
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```


## License

This project is open source, for portfolio.

