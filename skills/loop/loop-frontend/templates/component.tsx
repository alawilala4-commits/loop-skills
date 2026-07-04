// Template: React Component (TypeScript + Hooks)
// Usage: Copy & adapt for your component

import React, { useState, useEffect, ReactNode } from 'react';

// 1. TYPE DEFINITIONS
interface User {
  id: string;
  name: string;
  email: string;
}

interface UserCardProps {
  user: User;
  onEdit?: (id: string) => void;
  isLoading?: boolean;
}

// 2. COMPONENT: Functional with Hooks
const UserCard: React.FC<UserCardProps> = ({ user, onEdit, isLoading = false }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  // 3. EFFECTS
  useEffect(() => {
    console.log('UserCard mounted/updated:', user.id);
    
    return () => {
      console.log('UserCard cleanup:', user.id);
    };
  }, [user.id]);

  // 4. HANDLERS
  const handleEdit = () => {
    if (onEdit) {
      onEdit(user.id);
    }
  };

  const handleToggle = () => {
    setIsExpanded(!isExpanded);
  };

  // 5. RENDER
  return (
    <div className="card user-card" role="article">
      {/* HEADER */}
      <div className="card-header">
        <h3>{user.name}</h3>
        <button 
          onClick={handleToggle}
          aria-expanded={isExpanded}
          aria-label={isExpanded ? 'Collapse' : 'Expand'}
          disabled={isLoading}
        >
          {isExpanded ? '▼' : '▶'}
        </button>
      </div>

      {/* BODY (Conditional) */}
      {isExpanded && (
        <div className="card-body">
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>ID:</strong> {user.id}</p>
        </div>
      )}

      {/* FOOTER */}
      <div className="card-footer">
        <button 
          onClick={handleEdit}
          disabled={isLoading}
          className="btn-primary"
        >
          {isLoading ? 'Loading...' : 'Edit'}
        </button>
      </div>

      {/* LOADING INDICATOR */}
      {isLoading && <div className="spinner" role="status" />}
    </div>
  );
};

// 6. STYLES (CSS Module or inline)
const styles = `
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.card-body {
  margin: 1rem 0;
}

.card-footer {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
}

.btn-primary {
  background: #007bff;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 3px solid #f3f3f3;
  border-top: 3px solid #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
`;

export default UserCard;

// CHECKLIST
// ✓ TypeScript types (interface, FC)
// ✓ React Hooks (useState, useEffect)
// ✓ Accessibility (role, aria-*)
// ✓ Conditional rendering
// ✓ Event handlers
// ✓ Loading state
// ✓ Cleanup function in useEffect
// ✓ Responsive styles
// ✓ Semantic HTML
