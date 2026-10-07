---
name: DuckProject
description: Clear entry points for a versatile collection of tools.
colors:
  action-blue: "#285cae"
  action-blue-hover: "#184784"
  cue-gold: "#d79b18"
  warm-paper: "#f7f5ef"
  panel-paper: "#fffefa"
  dark-ink: "#20272b"
  secondary-ink: "#4e585d"
  monitor-bg: "#0e1015"
  monitor-panel: "#1a1d27"
typography:
  wordmark:
    fontFamily: "Outfit, sans-serif"
    fontSize: "32px"
    fontWeight: 700
  display:
    fontFamily: "IBM Plex Sans Thai, sans-serif"
    fontSize: "clamp(38px, 5.8vw, 76px)"
    fontWeight: 700
    lineHeight: 1.2
  body:
    fontFamily: "IBM Plex Sans Thai, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  square: "0px"
  control: "3px"
spacing:
  small: "8px"
  medium: "16px"
  large: "24px"
components:
  button-primary:
    backgroundColor: "{colors.action-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.square}"
    padding: "12px 24px"
  button-primary-hover:
    backgroundColor: "{colors.action-blue-hover}"
    textColor: "#ffffff"
    rounded: "{rounded.square}"
---

# Design System: DuckProject

## Overview

**Creative North Star: "เครื่องมือหลายอย่าง ทางเข้าเดียวที่ชัดเจน"**

DuckProject is a multipurpose personal project. Its portal is calm and accessible to anyone; it does not frame every app as a classroom tool. Each app can have its own density: SCQuizz supports live event participation.

**Key Characteristics:** broad app rows, visible logos, direct Thai actions, strong text contrast, and minimal decoration.

## Colors

Warm paper and dark ink make the portal easy to scan. Blue marks actions; gold marks the current place or the edge of an app row.

## Typography

The six core portal pages use `core/static/core/theme.css` as the shared source for colors and fonts: IBM Plex Sans Thai for Thai text and Outfit for the DuckProject wordmark and app names. SCQuizz keeps its own visual design. Body text should stay at least 16px where it carries primary instructions.

## Layout

The portal has one column of broad app rows and a 1500px maximum width. At 700px and below, each row stacks its action below the logo and description. SCQuizz prioritizes a narrow participant form on phones and a wider organizer board on computers.

## Elevation & Depth

Surfaces are flat at rest. Borders and background contrast separate sections. Shadows are reserved for temporary overlays such as the account menu.

## Shapes

Portal rows are square and bordered. Primary action buttons are rectangular. Form controls use a small 3px radius. The mustard edge cue is a repeated portal signature.

## Components

### App row

Show an app logo, name, plain Thai description, and one “เปิดแอป” action. The full row is clickable. Keep uploaded custom logos when present.

### Buttons and inputs

Use blue for the main action and a clear gold focus outline. Inputs have a visible border, readable placeholder, and a 16px font on phones. Destructive controls retain distinct warning color.

### Navigation

All six core portal pages share one DuckProject header: wordmark, home link, available account actions, and a visible current-page cue. Account actions follow authentication and staff permissions. On narrow phones the same links move to a second row. SCQuizz uses visible task tabs; tabs must remain keyboard accessible.

## Do's and Don'ts

- **Do** use Thai for user-facing actions and guidance, retaining English for app names and technical terms when useful.
- **Do** let each app's real task set its information density.
- **Do** show a recognizable logo beside each app on the portal.
- **Don't** describe DuckProject as a teacher/student platform.
- **Don't** hide a primary task or copy control on mobile.
- **Don't** use ambient blobs, glass cards, or decorative gradients as the main visual language.
