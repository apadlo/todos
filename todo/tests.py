from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm
from .test_data import TEST_USERNAME, TEST_PASSWORD, NEW_USER_USERNAME, NEW_USER_PASSWORD


class TodoModelTest(TestCase):
    """Test the Todo model"""

    def setUp(self):
        self.user = User.objects.create_user(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_todo_creation(self):
        """Test that a Todo can be created with required fields"""
        todo = Todo.objects.create(
            title='Test Todo',
            memo='Test memo',
            user=self.user
        )
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.memo, 'Test memo')
        self.assertEqual(todo.user, self.user)
        self.assertIsNone(todo.datecompleted)
        self.assertFalse(todo.important)

    def test_todo_str_representation(self):
        """Test the string representation of a Todo"""
        todo = Todo.objects.create(
            title='My Todo Title',
            user=self.user
        )
        self.assertEqual(str(todo), 'My Todo Title')


class TodoFormTest(TestCase):
    """Test the TodoForm"""

    def test_valid_form(self):
        """Test that the form is valid with correct data"""
        form_data = {
            'title': 'Test Todo',
            'memo': 'Test memo',
            'important': True
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_title(self):
        """Test that the form is invalid without a title"""
        form_data = {
            'memo': 'Test memo',
            'important': False
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())


class HomeViewTest(TestCase):
    """Test the home view"""

    def test_home_view_status_code(self):
        """Test that home view returns 200 status code"""
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class SignupUserViewTest(TestCase):
    """Test the signup user view"""

    def test_signup_get_request(self):
        """Test that signup page loads correctly"""
        client = Client()
        response = client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_signup_post_create_user(self):
        """Test that a new user can be created through signup"""
        client = Client()
        client.post('/signup/', {
            'username': NEW_USER_USERNAME,
            'password1': NEW_USER_PASSWORD,
            'password2': NEW_USER_PASSWORD
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, NEW_USER_USERNAME)


class LoginUserViewTest(TestCase):
    """Test the login user view"""

    def setUp(self):
        self.user = User.objects.create_user(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_login_get_request(self):
        """Test that login page loads correctly"""
        client = Client()
        response = client.get('/login/')
        self.assertEqual(response.status_code, 200)


class CreateTodoViewTest(TestCase):
    """Test the create todo view"""

    def setUp(self):
        self.user = User.objects.create_user(username=TEST_USERNAME, password=TEST_PASSWORD)
        self.client = Client()
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_create_todo_requires_login(self):
        """Test that creating todo requires authentication"""
        client = Client()
        response = client.get('/create/')
        self.assertEqual(response.status_code, 302)  # Redirect to log in

    def test_create_todo_post(self):
        """Test creating a new todo"""
        self.client.post('/create/', {
            'title': 'New Test Todo',
            'memo': 'Test memo',
            'important': True
        })
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.first().title, 'New Test Todo')


class CompleteTodoViewTest(TestCase):
    """Test the complete todo functionality"""

    def setUp(self):
        self.user = User.objects.create_user(username=TEST_USERNAME, password=TEST_PASSWORD)
        self.client = Client()
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
        self.todo = Todo.objects.create(
            title='Test Todo',
            user=self.user
        )

    def test_complete_todo(self):
        """Test that a todo can be marked as completed"""
        response = self.client.post(f'/todo/{self.todo.pk}/complete')
        self.assertEqual(response.status_code, 302)  # Redirect after completion
        self.todo.refresh_from_db()
        self.assertIsNotNone(self.todo.datecompleted)


class DeleteTodoViewTest(TestCase):
    """Test the delete todo functionality"""

    def setUp(self):
        self.user = User.objects.create_user(username=TEST_USERNAME, password=TEST_PASSWORD)
        self.client = Client()
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
        self.todo = Todo.objects.create(
            title='Test Todo',
            user=self.user
        )

    def test_delete_todo(self):
        """Test that a todo can be deleted"""
        self.assertEqual(Todo.objects.count(), 1)
        response = self.client.post(f'/todo/{self.todo.pk}/delete')
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertEqual(Todo.objects.count(), 0)
