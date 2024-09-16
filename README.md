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
