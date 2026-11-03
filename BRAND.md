# Creative Cave Brand Guide

Living brand guide for Creative Cave. Start here when designing anything new (site sections, social, decks, merch) so it stays consistent with the November 25, 2026 launch site at creativecave.io.

Last updated: November 3, 2026

---

## 1. The idea

**In an era of AI, we feel organic, authentic and relational.**

We use industry-leading large language models, but the brand should never feel like a machine made it. Everything leans handmade: screen-print texture, hand-lettered script, ranch badges, a pixel bear you can actually play with. Tech does the heavy lifting. The relationships stay human.

The look is three things mixed together:

| Ingredient | What it brings | Where you see it |
|---|---|---|
| **Ranch / Western merch** | Warmth, craft, "made by hand" | Canyon lettering, ranch badge, longhorn herd, rope divider, stars, halftone grain |
| **Arcade** | Play, delight, a reason to stay | Pixel bear runner game, pixel mesas and cacti |
| **Apple design** | Restraint, clarity, polish | Clean layout, pill buttons, glass nav, spring-feel motion, generous space |

---

## 2. Color palette

Three colors. Nothing else.

| Name | Hex | RGB | Role |
|---|---|---|---|
| **Seal Blue** | `#DBF2FC` | 219, 242, 252 | Light base. Backgrounds, and text on navy |
| **Navy Blue** | `#072D59` | 7, 45, 89 | Dark base. Text on seal, dark sections, logo |
| **Crimson Pink** | `#FD6E88` | 253, 110, 136 | The accent. Use sparingly so it pops |

> "The first two colors set the mood. The accent gives it life."

### Supporting tints (derived, not new colors)

| Token | Value | Use |
|---|---|---|
| Crimson hover | `#ff8ea3` | Button hover |
| Crimson pressed | `#f4506f` | Button active |
| Crimson glow | `rgba(253,110,136,.2)` | Soft fills, focus halos |
| Navy 74% | `rgba(7,45,89,.74)` | Secondary text on seal |
| Navy 50% | `rgba(7,45,89,.5)` | Hints, captions on seal |
| Seal 74% | `rgba(219,242,252,.74)` | Secondary text on navy |
| Seal 6% / 11% | `rgba(219,242,252,.06)` / `.11` | Cards and pills on navy |

### How the colors work together

- **Light scope (top of the page, hero):** Seal background, Navy text, Crimson accents. Soft crimson and white glows in the corners.
- **Dark scope (everything below the hero):** Navy background, Seal text, Crimson accents.
- **The transition:** a gradient band from seal to navy, with the crimson longhorn herd walking across it.
- **Game sky:** gradient from Navy down to a Crimson horizon (`#072D59` → `#2b5585` → `#a77a9c` → `#FD6E88`).

### Contrast rules

- Crimson on Seal is **low contrast**. Use it for big or decorative things only (script words, badges, stars, button fills). Never for small body text.
- Crimson on Navy reads well. Script words and accents can be crimson in the dark sections.
- Buttons: crimson fill with **white Canyon lettering** (nav "Join the Waitlist"), or crimson fill with **navy text** (form "I Want In").

### CSS tokens

```css
:root{
  --seal:#DBF2FC;
  --navy:#072D59;
  --crimson:#FD6E88;
  --crimson-hi:#ff8ea3;
  --crimson-lo:rgba(253,110,136,.2);
}
```

---

## 3. Typography

| Role | Typeface | Notes |
|---|---|---|
| **Ranch display** | **CANYON** by Madeline O'Donoghue Studio | Chunky groovy Western caps. Section titles, labels, badges, stamps, the nav CTA |
| **Script accent** | **Yellowtail** (Google Fonts, free) | Signature brush script. One or two words at a time, tilted, overlapping the type around it |
| **Headline + body** | **SF Pro / system UI** | Clean Apple sans. Headline, paragraphs, FAQ answers, form |
| **Live labels** | **Anton** (Google Fonts, free) | Condensed caps for anything that changes on screen (game score, "SPACE TO JUMP") |

### CANYON license (important)

We own a **Standard Font Licence (one user)**.

- Allowed: static website graphics, social, print, merch, apparel, client work, and converting lettering to outlines.
- **Not allowed:** embedding or serving the font file on a website or app (`@font-face`), or sharing the file with anyone.
- So on the web, every Canyon word is **converted to vector outlines (SVG paths)**. The .otf never ships.
- Font file lives at: `/Volumes/Extreme SSD/Canyon_MODesign/CANYON.otf`
- To use Canyon as real live web type, email madeline.a.odonoghue@gmail.com for a web embedding license.

### Making new Canyon lettering for the site

Scripts live in `tools/canyon/` (they read the font from the SSD, they never copy it).

```bash
# one-time setup
python3 -m venv /tmp/fontenv && /tmp/fontenv/bin/pip install fonttools pillow

# any word -> SVG path JSON (key|TEXT|tracking)
/tmp/fontenv/bin/python tools/canyon/lettering.py "join|JOIN THE WAITLIST|50"

# rebuild the ranch badge (writes badge.svg)
cd tools/canyon && /tmp/fontenv/bin/python badge.py
```

In the page, outlines go in an `<svg class="cy">` with `fill:currentColor`, sized in `em`, plus a hidden `<span class="sr">` copy of the words for screen readers and SEO.

### Script move (the signature)

- One word in Yellowtail, crimson, rotated about **-7deg**, nudged up so it overlaps the line above.
- It should look intentionally a little sloppy, like we wrote it on there ourselves.
- No underline under "playbook." (removed on purpose).
- Current script words: "playbook.", "the", "Frequently", "almost there", "see you in the cave".

### Type details

- Big headlines: tight tracking (`-0.025em`), tight leading (`1.08`).
- Canyon and Anton labels: wide tracking (`.14em` to `.2em`), always caps.
- Body: system font, `1.5` line height, never tracked.

---

## 4. Logo

| Asset | File | Use |
|---|---|---|
| Full lockup (bear + creativecave) | `cc-logo.png` (668 x 158) | Hero, footer |
| Bear mark | `cc-bear.png` (127 x 158) | Nav, badge center, small spaces |
| Favicon / app icon | `favicon.png` (128 x 128, bear on seal circle) | Browser tab, home screen |
| Source | `~/Documents/Serotonin Lake Nona Grand Opening Countdown/CC OFFICIAL LOGO.png` | Illustrator export, Nov 3 2026 |

- On the web the logo is used as a CSS mask, so it takes the scope color: **Navy on seal, Seal on navy.**
- Never put the logo on a colored disc or box. Let it sit on the background.
- **To do:** export a trimmed SVG (or a 2000px+ PNG with the artboard trimmed to the logo) so it stays crisp on large screens.

---

## 5. Ranch badge

The "Authentic Branding" badge, modeled on classic longhorn ranch plates.

- Outer and inner navy rings.
- **"AUTHENTIC"** curved along the top, **"BRANDING"** along the bottom, in Canyon.
- Navy notched banner plate across the middle reading **"EST"** and **"2022"** in **crimson**.
- Bear mark centered in an open navy ring, with **no background fill** (page shows through).
- Navy curled scroll wings, a navy rule under the banner, and four short navy rays.
- No other crimson on the badge except EST 2022.
- Placement: stamped at about 9deg to the upper right of the headline on desktop. Under the headline on phones.
- Source: `tools/canyon/badge.py` (viewBox 220 x 160).

---

## 6. Motifs and texture

| Motif | Spec |
|---|---|
| **Print grain** | Fixed overlay over everything: 5px halftone dot grid + fractal noise, `mix-blend-mode:overlay`, 55% opacity |
| **Longhorn herd** | Pixel longhorns (26 x 12 grid), crimson, drawn through a 3px halftone dot mask, walking left to right, 38s loop, two-frame leg animation. Fades in and out at the edges |
| **Rope divider** | Two interlaced wavy strokes, seal at 45% opacity, in the footer |
| **Stars** | ★ in crimson as separators ("★ NOVEMBER 25 ★", "MADE BY HAND ★★★ TAMPA, FL") |
| **Mesas** | Two parallax layers of flat-topped pixel buttes, navy at 50% and 26% |
| **Cacti** | Pixel saguaros, navy silhouettes |

---

## 7. Voice and copy

**Tone:** direct, warm, relationship-forward. Short sentences. No filler. No robotic or AI-sounding phrasing. **No em dashes.**

Key lines in use:

- Headline: "We're rewriting the whole *playbook.*"
- Subline: "We're launching authentic connection, powered by industry-leading large language models, to connect people and businesses with real customers and real community."
- Section titles: "TRUSTED BY *the* REAL ONES", "*Frequently* ASKED QUESTIONS"
- Badge: "AUTHENTIC BRANDING, EST 2022"
- Footer: "*see you in the cave*" / "MADE BY HAND ★★★ TAMPA, FL"
- CTAs: "JOIN THE WAITLIST", "I Want In"
- Locations: Orlando · Tampa · St. Petersburg · Austin
- Awards: "THE 2026 GRIZZLIES ★ our year-end awards for the local businesses doing it right"

### The Grizzlies

Creative Cave's year-end awards for local businesses. On the site it stays subtle: one dim line under the client carousel (bear mark + "THE 2026 GRIZZLIES" in Canyon + a short note) and an FAQ entry. Next year, regenerate the Canyon lettering with the new year (`lettering.py "griz|THE 2027 GRIZZLIES|50"`).

Words we like: authentic, real, human, made by hand, community, connection, the cave.
Words to avoid: synergy, leverage, cutting-edge, revolutionary, "AI-powered" as a headline.

---

## 8. Components

| Component | Spec |
|---|---|
| **Nav** | Fixed, translucent seal glass (`rgba(219,242,252,.74)` + 20px blur). Bear mark, then pills: Home (navy filled, active), Play, FAQ, Contact. Right side: Join the Waitlist |
| **Pills** | 36px tall, fully rounded, 1px border, press scales to 0.97 |
| **Join the Waitlist** | Solid crimson pill, white Canyon lettering, soft crimson shadow. Scrolls to the email form and focuses it |
| **Email form** | Rounded bar, translucent fill, crimson "I Want In" button with navy text |
| **Countdown** | Navy tabular numbers, Canyon labels (DAYS HRS MIN SEC), "almost there" in script above |
| **Client carousel** | Full-width row of white client logos, 42s continuous scroll, pauses on hover, edges fade out. Logos sized for equal visual weight (wide marks shorter, stacked marks taller). Reduced motion shows a static wrapped grid |
| **FAQ** | Rounded translucent cards, crimson plus icon that rotates into an X, smooth height open |

---

## 9. Motion (Apple principles)

- Respond on press, not on release. Every button reacts instantly.
- One entrance: fade up with a slight blur clearing, staggered, about 0.9s.
- Ease: `cubic-bezier(.16,1,.3,1)`. No bouncy overshoot except tiny success moments.
- Respect `prefers-reduced-motion`: herd stops, entrances become simple fades, no smooth scroll.
- No busy moving backgrounds. The only constant motion is the herd and the game.

---

## 10. The game: Bear Runner

- Pixel bear (seal) runs across a dusk ranch. Space, up arrow or tap to jump. A short tap gives a short hop.
- Obstacles: navy saguaro cacti (single and double). After score 250, crimson bats: low ones you jump, high ones you stay under.
- Speeds up over time. Score flashes every 100. High score saved in the browser.
- HUD in Anton. Messages: "READY?", "GAME OVER", "ONE MORE RUN".

---

## 11. Do and don't

**Do**
- Keep it to Seal, Navy and Crimson.
- Mix one Canyon line with one script word for headings.
- Let things look a little hand-made and imperfect on purpose.
- Leave space. Simple beats busy.

**Don't**
- Add new colors, gradients outside the palette, or neon.
- Use Canyon as a live web font (license).
- Use crimson for small text on seal.
- Use em dashes in copy.
- Copy other brands' marks or phrases (the ranch inspo is for style only).

---

## 12. Clients in the carousel

All logos live in `logos/` as white, trimmed files. On the page they also get `filter:brightness(0) invert(1)` so any new logo with a transparent background turns white automatically.

| Client | File | Source |
|---|---|---|
| Toyota Gazoo Racing | `toyota-gazoo-racing.png` | Local file (low res, 288px) |
| Alphalete | `alphalete.png` | Local file (low res, 288px) |
| Serotonin Centers | `serotonin.png` | Lake Nona countdown assets |
| The Salty | `the-salty.svg` | saltydonut.com header |
| Beekman 1802 | `beekman-1802.svg` | beekman1802.com header |
| You Zone Longevity (formerly Blue Zone You) | `you-zone.png` | YZL_AgentBase |
| Tremble | `tremble.png` | Local file |
| Speed Syndicate | `speed-syndicate.png` | Speed Syndicate site, S knocked out of the circle |
| Dermastart (ClearChoice) | `dermastart.png` | dermastart.com header |
| Orlando Family Medical | `orlando-family-medical.png` | Local file |
| Broll Mountain Vineyards | `broll-mountain-vineyards.svg` | Local file |
| Dr. Schalit | `dr-schalit.png` | drschalit.com white logo |

To add a client: drop a transparent PNG or SVG in `logos/`, then add an `<li>` to both halves of `.marquee__track` (the second half is `aria-hidden` and makes the loop seamless).

## 13. Files

```
creative-cave-website/
  index.html          the launch site (single page)
  logos/              white client logos for the carousel
  cc-logo.png         full logo lockup
  cc-bear.png         bear mark
  favicon.png         tab / app icon
  BRAND.md            this guide
  tools/canyon/       Canyon to SVG outline scripts (font stays on the SSD)
```

Live: https://creativecave.io (deployed with the Vercel CLI from this folder: `vercel --prod`)

## 14. Open items

- [ ] Trimmed SVG or 2000px+ export of the logo
- [ ] Hook the email form up to a real list (Klaviyo, Mailchimp, etc.). Right now it only shows "You're in."
- [ ] Confirm every client in the carousel is OK to show publicly
- [ ] Higher-res Alphalete and Toyota Gazoo Racing logos (current files are 288px)
- [ ] Optional: web embedding license for Canyon
