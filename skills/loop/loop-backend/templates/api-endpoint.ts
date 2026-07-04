// Template: REST API Endpoint (Express + TypeScript)
// Usage: Copy & adapt for your API route

import { Router, Request, Response, NextFunction } from 'express';
import { z } from 'zod';

const router = Router();

// 1. SCHEMA VALIDATION (Input validation)
const CreateUserSchema = z.object({
  email: z.string().email('Invalid email'),
  name: z.string().min(2, 'Name too short'),
  age: z.number().int().min(0).max(150, 'Invalid age'),
});

type CreateUserPayload = z.infer<typeof CreateUserSchema>;

// 2. ERROR HANDLING
class ApiError extends Error {
  constructor(
    public statusCode: number,
    message: string,
    public code: string = 'INTERNAL_ERROR'
  ) {
    super(message);
  }
}

// 3. MIDDLEWARE: Request validation
const validateBody = (schema: z.ZodSchema) => {
  return (req: Request, res: Response, next: NextFunction) => {
    try {
      const validated = schema.parse(req.body);
      (req as any).validated = validated;
      next();
    } catch (err) {
      if (err instanceof z.ZodError) {
        return res.status(400).json({
          status: 'error',
          code: 'VALIDATION_ERROR',
          errors: err.errors,
        });
      }
      next(err);
    }
  };
};

// 4. ROUTE: POST /users (Create)
router.post(
  '/users',
  validateBody(CreateUserSchema),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const payload = (req as any).validated as CreateUserPayload;
      
      // TODO: Save to database
      const user = {
        id: Math.random().toString(36).substring(7),
        ...payload,
        createdAt: new Date(),
      };
      
      res.status(201).json({
        status: 'success',
        data: user,
      });
    } catch (err) {
      next(err);
    }
  }
);

// 5. ROUTE: GET /users/:id (Retrieve)
router.get('/users/:id', async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { id } = req.params;
    
    // TODO: Fetch from database
    if (!id) {
      throw new ApiError(400, 'User ID required', 'MISSING_ID');
    }
    
    const user = { id, name: 'John Doe', email: 'john@example.com' };
    
    res.status(200).json({
      status: 'success',
      data: user,
    });
  } catch (err) {
    next(err);
  }
});

// 6. ERROR HANDLER (Global)
router.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Error:', err);
  
  if (err instanceof ApiError) {
    return res.status(err.statusCode).json({
      status: 'error',
      code: err.code,
      message: err.message,
    });
  }
  
  res.status(500).json({
    status: 'error',
    code: 'INTERNAL_SERVER_ERROR',
    message: 'Something went wrong',
  });
});

export default router;

// CHECKLIST
// ✓ Input validation (Zod schema)
// ✓ Error handling (custom ApiError class)
// ✓ Async/await with try-catch
// ✓ TypeScript types
// ✓ Proper status codes (201, 400, 500)
// ✓ JSON response format
// ✓ Global error handler
// ✓ Middleware for request validation
