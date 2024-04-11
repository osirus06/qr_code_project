# Django QR Code API

This project provides a Django REST Framework (DRF) API for managing users and generating QR codes based on user information.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/osirus06/qr_code_project.git
   cd qr_code_project
   
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


3. Run database migrations:

   ```bash
   python manage.py migrate

4. Start the development server:

   ```bash
   python manage.py runserver

5. Access the API endpoints:
   Users: http://localhost:8000/api/users/


## API Endpoints

### Users

- `GET /api/users/`: List all users
- `POST /api/users/`: Create a new user
- `GET /api/users/{id}/`: Retrieve a specific user
- `PUT /api/users/{id}/`: Update a specific user
- `DELETE /api/users/{id}/`: Delete a specific user

## Contributing

Contributions are welcome! If you have suggestions or find issues with the project, please open an issue or submit a pull request.



