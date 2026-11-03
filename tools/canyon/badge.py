"""Ranch badge: CANYON letters set on a circle (as outlines) around the bear mark."""
import math, sys
sys.argv=['x']; from lettering import GS, CMAP, HM, KERN
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
CAP = 645

def glyphs(text, tracking):
    out=[]; prev=None
    for ch in text:
        g=CMAP[ord(ch)]; k=KERN.get((prev,g),0) if prev else 0
        pen=SVGPathPen(GS, ntos=lambda v: str(round(v)))
        GS[g].draw(TransformPen(pen,(1,0,0,-1,0,CAP)))
        out.append((pen.getCommands(), HM[g][0], k)); prev=g
    return out, tracking

def arc(text, cx, cy, r, capH, tracking, bottom=False, fill='var(--navy)'):
    gl, tr = glyphs(text, tracking); s = capH / CAP
    advs = [a + k for _, a, k in gl]; total = (sum(advs) + tr * (len(gl) - 1)) * s
    span = total / r; parts = []; cum = 0
    for (d, a, k), adv in zip(gl, advs):
        cum += k * s
        mid = (cum + a * s / 2) / r
        th = (-math.pi / 2 - span / 2 + mid) if not bottom else (math.pi / 2 + span / 2 - mid)
        x = cx + r * math.cos(th); y = cy + r * math.sin(th)
        rot = math.degrees(th) + (90 if not bottom else -90)
        parts.append(f'<path transform="translate({x:.2f} {y:.2f}) rotate({rot:.2f}) translate({-a*s/2:.2f} {-capH/2:.2f}) scale({s:.5f})" d="{d}"/>')
        cum += a * s + tr * s
    return f'<g fill="{fill}">' + ''.join(parts) + '</g>'

def straight(text, x, ybase, capH, tracking, anchor='middle', fill='var(--seal)'):
    gl, tr = glyphs(text, tracking); s = capH / CAP
    total = sum(a + k for _, a, k in gl) * s + tr * s * (len(gl) - 1)
    x0 = x - total / 2 if anchor == 'middle' else x
    parts=[]; cx = x0
    for d, a, k in gl:
        cx += k * s
        parts.append(f'<path transform="translate({cx:.2f} {ybase-capH:.2f}) scale({s:.5f})" d="{d}"/>')
        cx += a * s + tr * s
    return f'<g fill="{fill}">' + ''.join(parts) + '</g>'

CX, CY = 110, 80
svg = f'''<svg viewBox="0 0 220 160" role="img" aria-label="Creative Cave, Authentic Branding, established 2022">
  <circle cx="{CX}" cy="{CY}" r="66" fill="none" stroke="var(--navy)" stroke-width="3"/>
  <circle cx="{CX}" cy="{CY}" r="45" fill="none" stroke="var(--navy)" stroke-width="2"/>
  {arc("AUTHENTIC", CX, CY, 55.5, 11, 90)}
  {arc("BRANDING", CX, CY, 55.5, 11, 110, bottom=True)}
  <defs><mask id="bearHole" maskUnits="userSpaceOnUse" x="0" y="0" width="220" height="160">
    <rect width="220" height="160" fill="#fff"/><circle cx="{CX}" cy="{CY-2}" r="24" fill="#000"/>
  </mask></defs>
  <g mask="url(#bearHole)">
  <!-- scroll wings, like a ranch brand plate -->
  <g fill="none" stroke="var(--navy)" stroke-width="3" stroke-linecap="round">
    <path d="M32 70 C 22 58, 6 60, 4 72 C 3 82, 15 86, 20 79 C 24 73, 17 69, 13 73"/>
    <path d="M188 70 C 198 58, 214 60, 216 72 C 217 82, 205 86, 200 79 C 196 73, 203 69, 207 73"/>
    <path d="M26 92 L 194 92"/>
  </g>
  <!-- banner plate across the middle -->
  <path d="M28 66 L 192 66 L 183 76 L 192 86 L 28 86 L 37 76 Z" fill="var(--navy)"/>
  {straight("EST", 62, 80.5, 8, 90, fill="var(--crimson)")}
  {straight("2022", 158, 80.5, 8, 90, fill="var(--crimson)")}
  </g>
  <!-- bear medallion: open ring, page shows through behind the bear -->
  <circle cx="{CX}" cy="{CY-2}" r="24" fill="none" stroke="var(--navy)" stroke-width="2.5"/>
  <image href="cc-bear.png" x="{CX-15}" y="{CY-21.7}" width="30" height="37.3"/>
  <!-- rays under the plate, like the reference -->
  <g stroke="var(--navy)" stroke-width="2.2" stroke-linecap="round">
    <path d="M78 96 L72 104"/><path d="M90 98 L87 107"/><path d="M130 98 L133 107"/><path d="M142 96 L148 104"/>
  </g>
</svg>'''
open('badge.svg','w').write(svg); print(len(svg))
