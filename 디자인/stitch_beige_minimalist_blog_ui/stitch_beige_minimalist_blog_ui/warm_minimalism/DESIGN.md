---
name: Warm Minimalism
colors:
  surface: '#fbf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#fbf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ef'
  surface-container: '#efeeea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e4e2de'
  on-surface: '#1b1c1a'
  on-surface-variant: '#504441'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f0ed'
  outline: '#827470'
  outline-variant: '#d4c3be'
  surface-tint: '#77574d'
  primary: '#442a22'
  on-primary: '#ffffff'
  primary-container: '#5d4037'
  on-primary-container: '#d4ada1'
  inverse-primary: '#e7bdb1'
  secondary: '#655d5a'
  on-secondary: '#ffffff'
  secondary-container: '#ece0dc'
  on-secondary-container: '#6b6360'
  tertiary: '#432b22'
  on-tertiary: '#ffffff'
  tertiary-container: '#5b4137'
  on-tertiary-container: '#d2aea1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#e7bdb1'
  on-primary-fixed: '#2c160e'
  on-primary-fixed-variant: '#5d4037'
  secondary-fixed: '#ece0dc'
  secondary-fixed-dim: '#cfc4c0'
  on-secondary-fixed: '#201a18'
  on-secondary-fixed-variant: '#4c4542'
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#e4beb2'
  on-tertiary-fixed: '#2b160f'
  on-tertiary-fixed-variant: '#5b4137'
  background: '#fbf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2de'
typography:
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1120px
  gutter: 24px
  margin-mobile: 20px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
  section-gap: 80px
---

## Brand & Style

The design system is centered on a "Quiet Professionalism" aesthetic—blending the warmth of a personal journal with the precision of a high-end editorial platform. It targets a reader who values focus and a writer who seeks a calm, distraction-free environment.

The style is a refined take on **Minimalism**, moving away from "clinical white" toward "organic cream." It utilizes ample whitespace to let content breathe, but anchors that space with soft, tactile touches and sophisticated typography. The emotional goal is to evoke a sense of home, reliability, and intellectual clarity.

## Colors

The palette is built on a foundation of "Oatmeal" and "Clotted Cream" tones to reduce eye strain and create an inviting atmosphere. 

- **Primary:** A deep, roasted coffee brown used for high-importance text and primary interactive states.
- **Secondary:** A soft, muted clay used for subtle dividers and secondary button backgrounds.
- **Backgrounds:** The main canvas is a warm beige, while cards and containers use a pure white to create a soft "lifted" effect without heavy shadows.
- **Accents:** Earthy terracotta and cedar tones provide warmth for links and active states without breaking the monochromatic harmony.

## Typography

This design system employs a dual sans-serif pairing to maintain a modern yet friendly voice. **Plus Jakarta Sans** is used for headlines to provide a soft, geometric clarity that feels contemporary and welcoming. **Be Vietnam Pro** is selected for body text due to its exceptional legibility and slightly warmer, more approachable character at smaller scales.

Hierarchy is established through significant scale shifts and purposeful use of weight. Body copy should always maintain a generous line height (1.6x) to ensure long-form reading remains comfortable.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop, centered to create a focused reading experience, and a fluid model for mobile devices. 

- **Desktop:** 12-column grid with a 1120px max-width.
- **Mobile:** Single column with 20px side margins.
- **Rhythm:** An 8px base unit governs all spatial relationships. Vertical rhythm is emphasized, with large gaps (Section-gap) between major content blocks to prevent visual clutter and maintain the minimalist "zen" aesthetic.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and very soft, ambient shadows. 

Instead of traditional drop shadows, this design system uses a "Layered Paper" approach. Surfaces (like cards) sit on the canvas with a very subtle 1px border in a slightly darker beige or an extremely diffused shadow (15% opacity of the primary brown). This creates a sense of tactile stacking—as if cards were pieces of premium stationery laid on a wooden desk. Backdrop blurs are used sparingly, specifically for navigation bars to maintain context while scrolling.

## Shapes

The design system utilizes **Soft** roundedness. A radius of 0.25rem (4px) for small components and up to 0.75rem (12px) for larger cards provides a gentle, organic feel without appearing overly "bubbly" or juvenile. This balance maintains the professional edge of the blog while reinforcing the "cozy" brand pillar.

## Components

### Buttons
Primary buttons use a solid fill of the Primary color with white text. Secondary buttons use a transparent background with a 1px border. All buttons should have generous horizontal padding (2.5x the height) to feel substantial and high-end.

### Cards
Minimalist cards are the core of the blog board. They feature a white background, the "Soft" corner radius, and no heavy borders. Instead, use a subtle 1px stroke in the Secondary color. Content inside cards should be padded at 32px to emphasize the "clean" aesthetic.

### Input Fields
Inputs should be stripped of heavy shadows. Use a simple bottom border or a very light-colored background fill. The focus state should be indicated by a shift in border color to the Primary brown, never a high-contrast glow.

### Chips & Tags
Use chips for categories. These should have a pill-shape (fully rounded) and use the Secondary color with a low-opacity fill to remain unobtrusive.

### Article Lists
Lists should prioritize white space. Use thin, 1px dividers in a very light beige to separate items, ensuring that the typography does the heavy lifting for the hierarchy.