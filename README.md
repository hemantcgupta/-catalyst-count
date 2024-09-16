# catalyst-count

## Description
Your task is to create a Web application using Django. The application will allow users to login and filter the 
database table using a form. 
Once the user submits the form, display the count of records based on the applied filters.

## Setup Instructions

### Prerequisites
- Python (3.11.0 or higher)
- Pip (24.0 or higher)
- PostgreSQL

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/hemantcgupta/catalyst-count.git
   ```
   
2. **Create a `.env` file** in the root directory of your Django project.

3. **Add the following content** to the `.env` file:

    ```env
    # Django Settings
    DEBUG=True

    # PostgreSQL Database Configuration
    DB_NAME=your_db
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_HOST=your_host
    DB_PORT=your_post
    ```   
4. **Create the database** named as same as `your_db`:

    ```sql
    CREATE DATABASE your_db;
    ```

## Setting Up the Virtual Environment

1. **Create a virtual environment** in the root directory of your project:

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:

    - On **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - On **macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

3. **Install dependencies using pip:**
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. **Make migrations:**
   ```bash
   python manage.py makemigrations
   ```
2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

### Running the Server
Start the Django development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.


## API Endpoints

Here are the available API endpoints for application:
- **`/signup/`**
  - **Method:** POST
  - **Description:** Custom signup endpoint to create a new user. It uses `SignupForm` from `allauth` to handle user registration.

- **`/login/`**
  - **Method:** POST
  - **Description:** Custom login endpoint for user authentication. It authenticates users based on username and password and logs them in if credentials are valid.

- **`/logout/`**
  - **Method:** POST
  - **Description:** Custom logout endpoint to terminate the user session. Only POST requests are allowed.

- **`/upload_data/`**
  - **Method:** POST
  - **Description:** Endpoint to upload data files. It saves the uploaded file and processes it in the background using a separate thread. The file is saved to the `uploads` directory.

- **`/get_users/`**
  - **Method:** GET
  - **Description:** Endpoint to retrieve a list of users. It returns a rendered view of user data.

- **`/add_user/`**
  - **Method:** POST
  - **Description:** Endpoint to add a new user to the database. It uses `SignupForm` from `allauth` to handle user registration.

- **`/delete_user/`**
  - **Method:** POST
  - **Description:** Endpoint to delete a user from the database based on the provided user ID. It handles the deletion and returns the updated list of users.

- **`/query_builder/`**
  - **Method:** GET, POST
  - **Description:** Endpoint for constructing and executing custom queries. It allows users to filter data based on various criteria (e.g., industry, year founded, city, state, country) and returns the filtered results.

## Additional Notes

- Ensure that the PostgreSQL server is running and accessible with the provided credentials.
- For production environments, you should set `DEBUG` to `False` and configure other security settings accordingly.
