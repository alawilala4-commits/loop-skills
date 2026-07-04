---
name: loop-frontend
description: "Development frontend: component, styling, responsif, accessibility, performance."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, frontend, UI, component, performance]
---

# Loop Frontend

## When to Use
Gunakan saat mengerjakan fitur frontend, component baru, styling, atau perubahan UI.

## Inputs
- Requirement UI/UX.
- Design system atau component library.
- Target browser/device.
- Accessibility standar (WCAG 2.1).
- Performance budget.
- Existing component structure.

## Procedure
1. Breakdown requirement → component granular.
2. Cek apakah component sudah ada di library.
3. Design component props & state.
4. Implementasi component dengan accessibility in mind.
5. Add styling (responsive, dark mode jika perlu).
6. Test responsif di breakpoint utama.
7. Test accessibility (keyboard nav, screen reader).
8. Optimasi performance (lazy load, code split).
9. Verifikasi dengan design spec.

## Output
- Component siap pakai.
- Story atau demo.
- Unit tests.
- Accessibility checklist lolos.
- Performance metrics (LCP, CLS, FID).

## Pitfalls
- Jangan hardcode sizing, gunakan design tokens.
- Jangan neglect mobile viewport.
- Jangan create component terlalu generic atau terlalu specific.
- Jangan lupa keyboard navigation.
- Jangan inline style besar — gunakan CSS class.

## Verification
- Component render di semua breakpoint.
- Keyboard accessible (Tab, Enter, Escape).
- Semantic HTML (proper headings, labels).
- Color contrast ≥ 4.5:1 untuk text.
- No console errors.
- Performance: LCP < 2.5s, CLS < 0.1.

## Component Checklist
✓ Props typed (TypeScript/PropTypes)
✓ Default props sensible
✓ Responsive design
✓ Dark mode support
✓ Keyboard navigation
✓ ARIA labels where needed
✓ Unit tests
✓ Storybook story
✓ Performance optimized

## Testing Approach
1. Unit test: logic, state, props
2. Visual test: responsif, dark/light mode
3. A11y test: axe-core, keyboard nav
4. E2E test: user flow

## Performance Optimization
- Code split component besar
- Lazy load non-critical assets
- Memoize expensive renders
- Defer non-critical scripts
- Image optimization (WebP, srcset)