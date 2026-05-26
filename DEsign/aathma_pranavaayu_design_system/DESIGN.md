---
name: Aathma Pranavaayu Design System
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#40493c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#707a6b'
  outline-variant: '#c0cab9'
  surface-tint: '#226d1c'
  primary: '#004903'
  on-primary: '#ffffff'
  primary-container: '#166313'
  on-primary-container: '#8fde7f'
  inverse-primary: '#8bd97b'
  secondary: '#586152'
  on-secondary: '#ffffff'
  secondary-container: '#dce6d2'
  on-secondary-container: '#5e6758'
  tertiary: '#273b72'
  on-tertiary: '#ffffff'
  tertiary-container: '#3f538b'
  on-tertiary-container: '#b9c9ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a6f694'
  primary-fixed-dim: '#8bd97b'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#005304'
  secondary-fixed: '#dce6d2'
  secondary-fixed-dim: '#c0cab7'
  on-secondary-fixed: '#151e12'
  on-secondary-fixed-variant: '#40493b'
  tertiary-fixed: '#dbe1ff'
  tertiary-fixed-dim: '#b3c5ff'
  on-tertiary-fixed: '#00184a'
  on-tertiary-fixed-variant: '#30447b'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
  status-good: '#2D8A29'
  status-satisfactory: '#FFB800'
  status-poor: '#E67E22'
  sage-wash: '#F7FCF2'
  deep-navy: '#1A3066'
  sky-accent: '#2EA3F2'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

The design system is centered on the concept of **Atmospheric Clarity**. It translates the intangible nature of pure air into a tangible digital experience. The brand personality is professional, scientific, and revitalizing, targeting health-conscious consumers and premium corporate environments.

The design style is a blend of **Modern Minimalism** and **Tonal Layering**. It prioritizes generous whitespace—referred to as "Oxygen Space"—to evoke a sense of breathability and openness. The visual language avoids clutter, using high-quality typography and a restricted color palette to maintain a sophisticated, "airy" aesthetic that reflects the product's core promise of purification.

## Colors

The palette is anchored by **Deep Forest Green**, symbolizing life and rooted professionalism. This is balanced by **Soft Sage** and **Sage Wash** backgrounds, which replace harsh grays to keep the UI feeling organic and "pure."

### Status Indicators
To communicate air quality effectively, the system utilizes a specialized "Purity Scale":
- **Good:** A vibrant, healthy green (#2D8A29).
- **Satisfactory:** A warm amber (#FFB800) indicating caution.
- **Poor:** A deep, high-visibility burnt orange (#E67E22) to signal the need for purification without causing undue panic.

**Deep Navy** is reserved for high-contrast typography and iconography to ensure maximum legibility against light backgrounds.

## Typography

**Plus Jakarta Sans** is the sole typeface for the design system. Its modern, geometric construction and slightly wider stance provide an approachable yet highly professional character. 

- **Headlines:** Use Bold (700) weights with slight negative letter-spacing to create a "dense" focal point against the surrounding whitespace.
- **Body Text:** Use Regular (400) weight for maximum breathability. 
- **Labels:** Use Semi-Bold (600) with increased letter-spacing in all-caps for technical data points (e.g., PM2.5 levels) to enhance scannability.

## Layout & Spacing

The layout follows a **Fluid Grid** model with an emphasis on extreme vertical breathing room. 

- **The 8px Rule:** All spacing between elements must be a multiple of 8px to maintain mathematical harmony.
- **Oxygen Space:** Large-scale sections should be separated by a minimum of `section-gap` (120px) on desktop to prevent visual "suffocation."
- **Grid:** Use a 12-column grid for desktop with wide 24px gutters. On mobile, transition to a 4-column grid with 16px side margins. 
- **Alignment:** Content should predominantly be left-aligned to mimic the flow of a professional report, though "Hero" sections may use center-alignment for visual impact.

## Elevation & Depth

To maintain the "airy" feel, the design system avoids heavy, dark shadows. Instead, it uses **Atmospheric Elevation**:

- **Tonal Tiers:** Depth is primarily created by placing `White` cards on `Sage-Wash` backgrounds.
- **Subtle Shadows:** When elevation is required (e.g., for hovering over a purifier card), use a very large blur radius (30px+) with low-opacity (5-8%) forest green-tinted shadows. This makes elements appear to "float" on a cushion of air rather than sit on a solid surface.
- **Soft Borders:** Use ultra-thin (1px) borders in a slightly darker shade of sage (#D0E6C5) for form inputs and static containers to define space without adding visual weight.

## Shapes

The shape language is **Rounded and Organic**. 

Corners are softened to 0.5rem (8px) for standard components like input fields and small cards, while larger containers and buttons use 1rem (16px) or 1.5rem (24px) for a more approachable, tactile feel. This avoids the "clinical" sharpness often found in technology products, making the air purifier feel like a seamless part of a home or office environment.

## Components

- **Buttons:** Primary buttons use the Deep Forest Green with white text. Secondary buttons use a Sage background with Deep Forest Green text. Buttons should have generous horizontal padding (min 32px) to feel substantial.
- **Air Quality Chips:** Small, pill-shaped indicators using the status colors. They should include a soft-tinted background and a high-contrast text/icon pairing for immediate status recognition.
- **Cards:** White surfaces with a 1px Sage border. Header areas within cards should use the Sage-Wash background to separate information.
- **Input Fields:** Minimalist design with a Soft Sage border that transitions to Deep Forest Green on focus. Labels should sit above the field in the `label-lg` style.
- **Status Gauges:** Use circular, high-stroke-width progress bars to visualize air quality levels, employing the status color palette for the active stroke.
- **Lists:** Clean lines with ample vertical padding (16px+) between items, using the 1px Sage divider for separation.