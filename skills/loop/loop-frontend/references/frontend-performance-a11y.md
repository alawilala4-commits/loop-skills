# Frontend Performance & Accessibility

## Core Web Vitals Checklist

### LCP (Largest Contentful Paint) < 2.5s
- [ ] Optimize images (compress, use modern formats)
- [ ] Minimize CSS blocking
- [ ] Preload critical resources
- [ ] Remove render-blocking JavaScript

### FID (First Input Delay) < 100ms
- [ ] Break up long JavaScript tasks
- [ ] Use Web Workers for heavy computation
- [ ] Defer non-critical scripts
- [ ] Optimize event handlers

### CLS (Cumulative Layout Shift) < 0.1
- [ ] Specify image dimensions
- [ ] Avoid inserting content above existing
- [ ] Use transform/opacity for animations
- [ ] Avoid dynamic content (ads, popups)

## Accessibility Checklist

### WCAG 2.1 Level AA

- [ ] **Keyboard Navigation**
  - All interactive elements accessible via Tab
  - Logical tab order
  - Focus visible

- [ ] **Semantic HTML**
  - Proper heading hierarchy (h1→h6)
  - `<button>` for buttons, `<a>` for links
  - Form labels with `<label>`

- [ ] **Screen Reader**
  - `alt` text for images
  - ARIA labels where needed
  - Skip navigation link

- [ ] **Color Contrast**
  - Text: 4.5:1 ratio (normal)
  - Large text: 3:1 ratio
  - UI components: 3:1 ratio

- [ ] **Forms**
  - Labels associated with inputs
  - Error messages clear
  - Required fields marked

## Implementation

```tsx
// Accessible component example
<div>
  <label htmlFor="email">Email:</label>
  <input 
    id="email"
    type="email"
    aria-describedby="email-error"
    required
  />
  <span id="email-error" role="alert">
    {error && 'Please enter valid email'}
  </span>
</div>
```

## Testing Tools

- Lighthouse (Chrome DevTools)
- axe DevTools (accessibility)
- WebPageTest (performance)
- WAVE (accessibility)
