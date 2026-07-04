# Frontend Component Checklist

## Design & Props
- [ ] Component purpose clear (single responsibility)
- [ ] Props interface documented (with types)
- [ ] Default props sensible & safe
- [ ] No required prop with no default (except critical)
- [ ] Props composition works (can nest components)

## Styling
- [ ] Use design system tokens (colors, spacing, typography)
- [ ] No hardcoded pixel values (use variables)
- [ ] Responsive: works on mobile (320px), tablet, desktop
- [ ] Dark mode support (if app supports it)
- [ ] Print-friendly styles (if applicable)

## Accessibility (WCAG 2.1 AA)
- [ ] Semantic HTML (proper heading hierarchy, labels)
- [ ] Color contrast ≥ 4.5:1 (normal text), ≥ 3:1 (large text)
- [ ] Keyboard navigable (Tab, Enter, Escape, Arrow keys)
- [ ] ARIA labels for icon-only buttons
- [ ] ARIA live region for dynamic content
- [ ] Form labels associated with inputs
- [ ] Error messages linked to form controls

## Performance
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] CLS (Cumulative Layout Shift) < 0.1
- [ ] FID (First Input Delay) < 100ms
- [ ] Code splitting for large components
- [ ] Lazy load images (img loading="lazy")
- [ ] Memoize expensive renders (React.memo)

## Testing
- [ ] Unit test: props → output (happy path)
- [ ] Unit test: edge cases (empty, null, error state)
- [ ] Visual test: all breakpoints, light/dark mode
- [ ] A11y test: axe-core scan no violations
- [ ] E2E test: user interaction flow

## Documentation
- [ ] Storybook story (with all variants)
- [ ] Prop documentation in code (JSDoc or TypeScript)
- [ ] Usage example in README or docs
- [ ] Known limitations noted

## Code Quality
- [ ] No console.warn/error left
- [ ] No inline styles (except dynamic edge cases)
- [ ] No commented-out code
- [ ] Consistent indentation & naming
- [ ] Linter passes (ESLint, Prettier)
