# Todo Woo 📝

A modern, user-friendly todo list application built with Django that helps you organize your tasks and boost your productivity.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **User Authentication**: Secure signup and login system
- **Create Todos**: Add new tasks with title, memo, and importance flag
- **Manage Todos**: View, edit, and delete your tasks
- **Mark as Complete**: Track completed tasks with completion timestamps
- **Important Tasks**: Flag critical tasks for priority management
- **Current & Completed Views**: Separate views for active and completed todos
- **User-Specific Data**: Each user has their own private todo list

## 🚀 Tech Stack

- **Backend**: Django 5.2+
- **Database**: SQLite (default, easily configurable for PostgreSQL/MySQL)
- **Frontend**: HTML, CSS (Bootstrap), Django Templates
- **Authentication**: Django's built-in authentication system
- **Testing**: pytest with pytest-django plugin

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/apadlo/todos.git
   cd todos
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 💻 Usage

### Getting Started

1. **Sign Up**: Create a new account on the signup page
2. **Login**: Access your account with your credentials
3. **Create Todos**: Click "Create" to add new tasks
4. **Manage Tasks**: 
   - View all current (incomplete) todos
   - Mark todos as complete
   - Edit existing todos
   - Delete unwanted tasks
5. **View Completed**: Check your completed tasks history

### Key URLs

- `/` - Home page
- `/signup/` - User registration
- `/login/` - User login
- `/current/` - View current todos
- `/completed/` - View completed todos
- `/create/` - Create a new todo
- `/admin/` - Admin panel (requires superuser)

## 📁 Project Structure

```
todos/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── todo/                  # Main application
│   ├── models.py         # Todo model definition
│   ├── views.py          # Application views/controllers
│   ├── forms.py          # Todo forms
│   ├── admin.py          # Admin configuration
│   ├── templates/        # HTML templates
│   │   └── todo/
│   ├── static/           # Static files (CSS, JS, images)
│   └── migrations/       # Database migrations
└── todowoo/              # Project configuration
    ├── settings.py       # Django settings
    ├── urls.py           # URL routing
    └── wsgi.py           # WSGI configuration
```

## 🗄️ Database Schema

### Todo Model

| Field          | Type         | Description                           |
|----------------|--------------|---------------------------------------|
| title          | CharField    | Todo title (max 100 characters)       |
| memo           | TextField    | Detailed description (optional)       |
| created        | DateTimeField| Auto-generated creation timestamp     |
| datecompleted  | DateTimeField| Completion timestamp (nullable)       |
| important      | BooleanField | Important flag (default: False)       |
| user           | ForeignKey   | Associated user (one-to-many)         |

## 🛠️ Development

### Running Tests

This project includes comprehensive test coverage using Django's built-in testing framework with pytest support.

#### Using Django's Test Runner

```bash
python manage.py test
```

For verbose output:
```bash
python manage.py test --verbosity=2
```

#### Using Pytest

The project is configured with pytest-django for an alternative testing workflow:

```bash
pytest
```

For verbose output with detailed test names:
```bash
pytest -v
```

For even more detailed output:
```bash
pytest -vv
```

Run specific test files or test classes:
```bash
pytest todo/tests.py::TodoModelTest
pytest todo/tests.py::TodoModelTest::test_todo_creation
```

#### Test Configuration

- **pytest.ini**: Configures pytest to work with Django
  - Sets `DJANGO_SETTINGS_MODULE = todowoo.settings`
  - Defines test file patterns: `tests.py`, `test_*.py`, `*_tests.py`

- **config_runner.toml**: Stores test user credentials for consistent testing
  - Test user credentials for authentication tests
  - New user credentials for signup tests

- **conftest.py**: Provides pytest fixtures for common test setup
  - `config`: Loads test configuration from config_runner.toml
  - `test_user`: Creates a test user for authentication
  - `authenticated_client`: Provides a logged-in test client

#### Test Coverage

The test suite includes **12 comprehensive tests** covering:

##### Model Tests (TodoModelTest)
- ✅ **Todo Creation**: Validates that Todo objects can be created with required fields (title, memo, user)
- ✅ **String Representation**: Tests the `__str__` method returns the todo title

##### Form Tests (TodoFormTest)
- ✅ **Valid Form**: Ensures the TodoForm accepts valid data (title, memo, important flag)
- ✅ **Missing Title Validation**: Verifies the form is invalid when title is missing

##### View Tests
- ✅ **Home View** (HomeViewTest): Tests the home page returns HTTP 200 status
- ✅ **Signup View** (SignupUserViewTest):
  - GET request loads the signup form
  - POST request successfully creates a new user account
- ✅ **Login View** (LoginUserViewTest): Tests the login page loads correctly
- ✅ **Create Todo View** (CreateTodoViewTest):
  - Requires authentication (redirects unauthenticated users)
  - Successfully creates a new todo with valid data
- ✅ **Complete Todo View** (CompleteTodoViewTest): Tests marking a todo as completed sets `datecompleted` timestamp
- ✅ **Delete Todo View** (DeleteTodoViewTest): Verifies todos can be deleted successfully

All tests use Django's TestCase class and are compatible with both Django's test runner and pytest.

### Create Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Access Admin Panel

After creating a superuser, access the admin panel at `http://127.0.0.1:8000/admin/`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built as part of "Django 3 - Full Stack Websites with Python Web Development course" from Nick Walter (Zappy Code)
- **Note on Original Project License**: The original [django3-todowoo-project](https://github.com/zappycode/django3-todowoo-project) by ZappyCode does not include a LICENSE file. This means the original code is protected by default copyright laws (all rights reserved), and cannot be used, modified, or distributed without explicit permission from the author. This repository (`apadlo/todos`) is an independent implementation inspired by the course material and is licensed under the MIT License (see below)

## 📧 Contact

For questions or support, please open an issue on GitHub.

---
