# Fox-V1.0

## Overview
This project is a **Library Management System**, designed to simplify and streamline the process of managing library resources, users, and book circulation. It includes comprehensive functionality for **book management**, **user registration**, **user login with OTP (One-Time Password) verification**, **admin management**, and **book checkout/check-in** processes. The system ensures both user-friendly interfaces and strong security layers for reliable operations.
## Key Features
### User Functionality
- **Registration & Authentication**: Users can register, log in, and authenticate themselves using email-based OTP for verification.
- **Dashboard**: After logging in, users can view their active book checkouts and their associated due dates.
- **Book Browsing & Catalog**: Users can browse the catalog of available books and request checkouts.
- **Secure Checkout Process**: Users can check out books which are then marked as unavailable until they are returned.

### Admin Functionality
- **Secure Admin Login**: Admin access is controlled through a secure and configurable key.
- **Book Management**: Admins can add books to the catalog or check in books that have been returned.
- **Dashboard**: Admins have a global view of all books, including their availability and associated checkouts.

## Purpose and Vision
The purpose of this system is to digitize and automate the library management process, enhancing efficiency for both users and staff. It emphasizes ease of use and reliability while maintaining robust security and data integrity. The application is tailored for small to medium-sized libraries looking to modernize their system without complexity but with features to enhance the overall user experience.
## Security Functions
### 1. **User Authentication and Verification**
- **OTP Verification**: After login, users must verify their identity using a one-time password (OTP) which is sent to their registered email. The verification ensures that only legitimate users can access the dashboard and perform transactions.
- **Email Validation**: Users' email addresses must be unique and are verified during the signup process to ensure accurate identity registration.

### 2. **Password Hashing**
All user and admin passwords are hashed (using `werkzeug.security`) before being stored in the database. Hashing ensures security by preventing plaintext password storage, significantly reducing the risk of leaks.
### 3. **Session Control**
The system uses secure user sessions (`Flask`'s `session`) with role differentiation for users and admins. This ensures that sensitive functionalities (like admin features) are only accessible to authorized individuals, protecting against unauthorized access.
### 4. **Access Control**
- **Role-Based Access**: Admin features (like adding books or managing checkouts) are restricted to verified admins.
- **Verification Status**: Regular users can only perform specific actions, such as checking out a book, once they've successfully verified their OTP.

### 5. **Database Integrity**
The system enforces unique constraints (e.g., for email addresses) and relationships between models (like `User`, `Book`, and `Checkout`) to maintain the consistency of stored data.
### 6. **Secure Communication**
- **Email-Based Notifications**: OTPs are securely sent to users via email to facilitate identity verification, preventing fraudulent logins.
- **SMTP Handling**: Emails are sent using secure SMTP protocols to avoid interception and misuse of sensitive details.

## Installation and Setup
### Prerequisites
- Python 3.13 or higher
- Installed dependencies: Flask, Flask-SQLAlchemy, SQLAlchemy, Jinja2, Werkzeug, and Click.
- SMTP server credentials for email functionality.

## Future Enhancements
- **Advanced Search**: Add filters for searching books by genre or keywords.
- **Email Notifications**: Send reminders for approaching due dates.
- **Analytics**: Provide insights on popular books and user activity.

This system is currently in the **development phase**. Feedback, testing, and suggestions are welcome for improvement in future releases.
