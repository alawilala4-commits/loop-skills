# Component Testing Best Practices

## Testing Pyramid

```
        /\
       /  \  E2E Tests (10%)
      /    \
     /______\
     /      \
    /   IT   \ Integration Tests (20%)
   /          \
  /____________\
  /            \
 /     Unit     \ Unit Tests (70%)
/________________\
```

## Unit Tests

```javascript
// Good unit test
describe('formatEmail', () => {
  it('should lowercase email', () => {
    const result = formatEmail('TEST@EXAMPLE.COM');
    expect(result).toBe('test@example.com');
  });

  it('should trim whitespace', () => {
    const result = formatEmail('  test@example.com  ');
    expect(result).toBe('test@example.com');
  });

  it('should throw on invalid email', () => {
    expect(() => formatEmail('invalid')).toThrow();
  });
});
```

## Component Tests (React)

```javascript
import { render, screen, fireEvent } from '@testing-library/react';

describe('UserForm', () => {
  it('should render form inputs', () => {
    render(<UserForm />);
    expect(screen.getByLabelText('Email')).toBeInTheDocument();
  });

  it('should submit form on button click', async () => {
    const mockSubmit = jest.fn();
    render(<UserForm onSubmit={mockSubmit} />);
    
    fireEvent.click(screen.getByText('Submit'));
    
    expect(mockSubmit).toHaveBeenCalled();
  });
});
```

## Integration Tests

```javascript
describe('User API', () => {
  it('should create user and retrieve it', async () => {
    // Create
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'john@example.com' });
    
    const userId = response.body.data.id;
    
    // Retrieve
    const getResponse = await request(app)
      .get(`/api/users/${userId}`);
    
    expect(getResponse.body.data.name).toBe('John');
  });
});
```

## Test Structure (AAA Pattern)

```javascript
it('should calculate total price with tax', () => {
  // ARRANGE
  const items = [{ price: 100 }, { price: 200 }];
  
  // ACT
  const total = calculateTotal(items, 0.1); // 10% tax
  
  // ASSERT
  expect(total).toBe(330); // (100+200)*1.1
});
```

## Mocking Best Practices

```javascript
// Mock database
jest.mock('./database', () => ({
  getUser: jest.fn().mockResolvedValue({ id: '1', name: 'John' }),
}));

// Mock external API
jest.mock('axios');
axios.get.mockResolvedValue({ data: { success: true } });
```

## Test Coverage

Target: **80%+ coverage**
```bash
npm run test:coverage
# View report: coverage/index.html
```
