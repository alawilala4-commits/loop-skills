# Template: Python Unit Tests (pytest)
# Usage: Copy & adapt for your test suite

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Mock module import
sys.path.insert(0, os.path.dirname(__file__))

# 1. FIXTURES (Reusable test data)
@pytest.fixture
def sample_user():
    """Create sample user for testing"""
    return {
        'id': '123',
        'name': 'John Doe',
        'email': 'john@example.com',
    }

@pytest.fixture
def mock_database():
    """Mock database connection"""
    mock_db = Mock()
    mock_db.get_user.return_value = {'id': '123', 'name': 'John'}
    mock_db.save_user.return_value = True
    return mock_db

# 2. UNIT TESTS: Function behavior
class TestUserService:
    def test_create_user_success(self, sample_user):
        """Test creating user with valid data"""
        # Arrange
        name = sample_user['name']
        email = sample_user['email']
        
        # Act
        result = create_user(name, email)
        
        # Assert
        assert result['name'] == name
        assert result['email'] == email
        assert 'id' in result

    def test_create_user_invalid_email(self):
        """Test creating user with invalid email"""
        # Arrange
        invalid_email = 'not-an-email'
        
        # Act & Assert
        with pytest.raises(ValueError, match='Invalid email'):
            create_user('John', invalid_email)

    def test_create_user_missing_name(self):
        """Test creating user without name"""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match='Name required'):
            create_user('', 'john@example.com')

# 3. INTEGRATION TESTS: Database interaction
class TestUserRepository:
    def test_save_and_retrieve_user(self, mock_database):
        """Test saving and retrieving user from DB"""
        # Arrange
        repo = UserRepository(mock_database)
        user = {'id': '123', 'name': 'John'}
        
        # Act
        repo.save(user)
        result = repo.get('123')
        
        # Assert
        assert result['name'] == 'John'
        mock_database.save_user.assert_called_once()

    @patch('requests.get')
    def test_fetch_external_user(self, mock_get):
        """Test fetching user from external API"""
        # Arrange
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: {'id': '123', 'name': 'John'}
        )
        
        # Act
        result = fetch_user_from_api('123')
        
        # Assert
        assert result['name'] == 'John'
        mock_get.assert_called_once()

# 4. PARAMETRIZED TESTS: Multiple scenarios
class TestValidation:
    @pytest.mark.parametrize('email,valid', [
        ('john@example.com', True),
        ('invalid-email', False),
        ('', False),
        ('john@', False),
    ])
    def test_email_validation(self, email, valid):
        """Test email validation with multiple inputs"""
        result = validate_email(email)
        assert result == valid

# 5. FIXTURES: Setup & Teardown
@pytest.fixture(autouse=True)
def setup_teardown():
    """Setup before each test, cleanup after"""
    # Setup
    print('\\nSetting up test...')
    yield
    # Teardown
    print('\\nCleaning up...')

# 6. MARKERS: Test categorization
@pytest.mark.slow
def test_slow_operation():
    """Test that takes long (run with: pytest -m slow)"""
    import time
    time.sleep(1)
    assert True

@pytest.mark.skip(reason='Not implemented yet')
def test_future_feature():
    """Skipped test for future feature"""
    pass

# 7. HELPER FUNCTIONS (Mock implementations)
def create_user(name, email):
    if not name:
        raise ValueError('Name required')
    if '@' not in email:
        raise ValueError('Invalid email')
    return {'id': 'new-id', 'name': name, 'email': email}

def validate_email(email):
    return bool(email and '@' in email)

class UserRepository:
    def __init__(self, db):
        self.db = db
    
    def save(self, user):
        return self.db.save_user(user)
    
    def get(self, user_id):
        return self.db.get_user(user_id)

def fetch_user_from_api(user_id):
    import requests
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

# CHECKLIST
# ✓ Unit tests (functions)
# ✓ Integration tests (with database/API)
# ✓ Fixtures for test data
# ✓ Mocks for external dependencies
# ✓ Parametrized tests (multiple scenarios)
# ✓ Error cases (with pytest.raises)
# ✓ Setup/teardown
# ✓ Test markers (@pytest.mark)
# ✓ Descriptive test names & docstrings
