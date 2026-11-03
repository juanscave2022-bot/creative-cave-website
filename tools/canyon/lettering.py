"""Convert fixed words set in CANYON into SVG outline paths (static artwork, no font file shipped)."""
import sys, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

F = TTFont("/Volumes/Extreme SSD/Canyon_MODesign/CANYON.otf")
GS = F.getGlyphSet(); CMAP = F.getBestCmap(); HM = F['hmtx']
ASC, DESC = 760, 230   # generous box; tightened below by real bounds

def kern_pairs():
    pairs = {}
    if 'GPOS' not in F: return pairs
    for lookup in F['GPOS'].table.LookupList.Lookup:
        if lookup.LookupType != 2: continue
        for st in lookup.SubTable:
            if st.Format == 1:
                cov = st.Coverage.glyphs
                for i, ps in enumerate(st.PairSet):
                    for pvr in ps.PairValueRecord:
                        v = getattr(pvr.Value1, 'XAdvance', 0) or 0
                        if v: pairs[(cov[i], pvr.SecondGlyph)] = v
            elif st.Format == 2:
                cov = st.Coverage.glyphs
                c1 = st.ClassDef1.classDefs; c2 = st.ClassDef2.classDefs
                for g1 in cov:
                    k1 = c1.get(g1, 0)
                    rec = st.Class1Record[k1]
                    for g2, k2 in c2.items():
                        v = getattr(rec.Class2Record[k2].Value1, 'XAdvance', 0) or 0
                        if v: pairs[(g1, g2)] = v
    return pairs
KERN = kern_pairs()

def layout(text, tracking):
    x = 0; prev = None; placed = []
    for ch in text:
        g = CMAP.get(ord(ch))
        if g is None: raise SystemExit('missing glyph: ' + ch)
        if prev: x += KERN.get((prev, g), 0)
        placed.append((g, x)); x += HM[g][0] + tracking; prev = g
    return placed

def make(text, tracking=0):
    placed = layout(text, tracking)
    bp = BoundsPen(GS)
    for g, x in placed: GS[g].draw(TransformPen(bp, (1, 0, 0, 1, x, 0)))
    x0, y0, x1, y1 = bp.bounds
    y0 = 0   # bottom of the box is the baseline; descenders (Q, comma) hang below via overflow
    # crop to the ink so the SVG height equals the letter height
    pen = SVGPathPen(GS, ntos=lambda v: str(round(v)))
    for g, x in placed: GS[g].draw(TransformPen(pen, (1, 0, 0, -1, x - x0, y1)))
    return {'d': pen.getCommands(), 'w': round(x1 - x0), 'h': round(y1 - y0)}

if __name__ == '__main__':
    out = {k: make(v, int(t)) for k, v, t in (a.split('|') for a in sys.argv[1:])}
    print(json.dumps(out))
