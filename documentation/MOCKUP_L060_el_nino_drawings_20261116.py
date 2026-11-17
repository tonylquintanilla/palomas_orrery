"""
MOCKUP_L060_el_nino_drawings_20261116.py -- REFERENCE ONLY, not part of
the build and not run by anything. The drawing code behind the El Nino
page mockup of Nov 16, 2026 (claude.ai artifact "El Nino page mockup"),
kept so the build session can see the three maps' shapes, colours and
labels, and the charts' layout. The long RONI chart here is a SKETCH
(made-up shape); the build draws it from NOAA's file. Written with
Anthropic's Claude Opus 5.5.
"""
import math, json, os, datetime
os.makedirs(root,exist_ok=True)
RED='#d9542b'; BLUE='#2f6fbf'; INK='#222'; DIM='#555'

# ---- sketch series (shape only) ----
ev=[(1957.9,1.6),(1965.8,1.6),(1972.9,1.7),(1982.95,2.40),(1987.6,1.5),(1991.9,1.6),(1997.9,2.28),(2002.9,1.2),(2009.9,1.4),(2015.9,2.25),(2023.9,1.6),
    (1955.8,-1.6),(1973.9,-1.91),(1975.9,-1.6),(1988.9,-1.94),(1999.9,-1.6),(2007.9,-1.6),(2010.9,-1.63),(2021.5,-1.2),(1964.4,-0.9),(1970.9,-1.3),(1984.9,-1.1),(1995.9,-1.0),(2017.9,-1.0)]
def val(t):
    v=0.0
    for c,a in ev: v+=a*math.exp(-((t-c)/0.42)**2)
    v+=0.10*math.sin(t*2.1)+0.05*math.sin(t*5.3)
    return v
# real last 12 seasons (CPC RONI.ascii.txt, fetched 2026-11-16)
real=[('SON 25',-0.93),('OND 25',-0.98),('NDJ 25',-1.04),('DJF 26',-0.91),('JFM 26',-0.76),('FMA 26',-0.44),('MAM 26',-0.04),('AMJ 26',0.49),('MJJ 26',0.97),('JJA 26',1.36),('JAS 26',1.69),('ASO 26',1.97)]
# CPC RONI.ascii.txt, read 2026-11-16 (ASO 2026 read in the browser at 18:10 Chicago)
pts=[]
t=1950.0
while t<2025.7:
    pts.append((t,val(t))); t+=1/12
for i,(s,v) in enumerate(real): pts.append((2025.75+i/12,v))

def seesaw(W,H,label_peaks=True,compact=False):
    padL,padR,padT,padB=28,8,18,26
    x0,x1=1950,2027; ymax=3.0
    sx=lambda t: padL+(t-x0)/(x1-x0)*(W-padL-padR)
    sy=lambda v: padT+(ymax-v)/(2*ymax)*(H-padT-padB)
    up=' '.join(f'{sx(t):.1f},{sy(max(v,0)):.1f}' for t,v in pts)
    dn=' '.join(f'{sx(t):.1f},{sy(min(v,0)):.1f}' for t,v in pts)
    z0=sy(0); xa=sx(pts[0][0]); xb=sx(pts[-1][0])
    g=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Sketch of the seesaw chart: El Nino seasons as red peaks above the line, La Nina as blue dips below, 1950 to 2026; shape only, not NOAA data">']
    for v in (2,1,-1,-2):
        g.append(f'<line x1="{padL}" x2="{W-padR}" y1="{sy(v):.1f}" y2="{sy(v):.1f}" stroke="#e3e3e3" stroke-width="1"/>')
        g.append(f'<text x="{padL-4}" y="{sy(v)+3:.1f}" font-size="9" text-anchor="end" fill="{DIM}">{v:+d}</text>')
    for v in (0.5,-0.5):
        g.append(f'<line x1="{padL}" x2="{W-padR}" y1="{sy(v):.1f}" y2="{sy(v):.1f}" stroke="#999" stroke-width="0.8" stroke-dasharray="3 3"/>')
    g.append(f'<polygon points="{xa:.1f},{z0:.1f} {up} {xb:.1f},{z0:.1f}" fill="{RED}"/>')
    g.append(f'<polygon points="{xa:.1f},{z0:.1f} {dn} {xb:.1f},{z0:.1f}" fill="{BLUE}"/>')
    g.append(f'<line x1="{padL}" x2="{W-padR}" y1="{z0:.1f}" y2="{z0:.1f}" stroke="#333" stroke-width="1"/>')
    for yr in (1950,1970,1990,2010):
        g.append(f'<text x="{sx(yr):.1f}" y="{H-8}" font-size="10" text-anchor="middle" fill="{DIM}">{yr}</text>')
    if label_peaks:
        for (c,a,lab) in [(1982.95,2.40,'1982-83  +2.40'),(1997.9,2.28,'1997-98  +2.28'),(2015.9,2.25,'2015-16  +2.25')]:
            g.append(f'<text x="{sx(c):.1f}" y="{sy(a)-5:.1f}" font-size="9" text-anchor="middle" fill="{INK}">{lab.split()[0]}</text>')
    g.append(f'<circle cx="{xb:.1f}" cy="{sy(1.97):.1f}" r="3.5" fill="#111"/>')
    g.append(f'<text x="{xb-6:.1f}" y="{sy(1.97)+12:.1f}" font-size="9" text-anchor="end" fill="{INK}">now +1.97</text>')
    g.append(f'<text x="{padL+2}" y="11" font-size="9" fill="{RED}">El Nino above</text>')
    g.append(f'<text x="{W-padR}" y="11" font-size="9" text-anchor="end" fill="{DIM}">RONI, degrees C</text>')
    g.append(f'<text x="{padL+2}" y="22" font-size="8" fill="{DIM}">dashed: the +0.5 and -0.5 thresholds</text>')
    g.append(f'<text x="{padL+2}" y="{H-padB-4}" font-size="9" fill="{BLUE}">La Nina below</text>')
    g.append('</svg>'); return ''.join(g)

def zoom(W,H):
    padL,padR,padT,padB=30,10,16,34
    n=len(real); ymin,ymax=-1.5,2.8
    sx=lambda i: padL+i/(n-1)*(W-padL-padR)
    sy=lambda v: padT+(ymax-v)/(ymax-ymin)*(H-padT-padB)
    g=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="NOAA RONI, the last twelve seasons: from -1.04 in Nov-Jan 2025 to +1.97 in Aug-Oct 2026; the record +2.40 drawn as a dashed line above">']
    for v in (-1,0,1,2):
        g.append(f'<line x1="{padL}" x2="{W-padR}" y1="{sy(v):.1f}" y2="{sy(v):.1f}" stroke="{"#333" if v==0 else "#e3e3e3"}" stroke-width="1"/>')
        g.append(f'<text x="{padL-4}" y="{sy(v)+3:.1f}" font-size="9" text-anchor="end" fill="{DIM}">{v:+d}</text>')
    g.append(f'<line x1="{padL}" x2="{W-padR}" y1="{sy(2.40):.1f}" y2="{sy(2.40):.1f}" stroke="{INK}" stroke-width="1" stroke-dasharray="4 3"/>')
    g.append(f'<text x="{padL+2}" y="{sy(2.40)-4:.1f}" font-size="9" fill="{INK}">record +2.40, Dec-Feb 1982-83</text>')
    g.append(f'<text x="{padL+2}" y="{sy(-1)+12:.1f}" font-size="8.5" fill="{DIM}">RONI, degrees C</text>')
    bw=(W-padL-padR)/n*0.7
    for i,(s,v) in enumerate(real):
        x=sx(i); y=sy(max(v,0)); h=abs(sy(v)-sy(0))
        g.append(f'<rect x="{x-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{RED if v>0 else BLUE}"/>')
        if i%2==1 or i==n-1:
            g.append(f'<text x="{x:.1f}" y="{H-20}" font-size="8.5" text-anchor="middle" fill="{DIM}">{s.split()[0]}</text>')
    g.append(f'<text x="{sx(1.0):.1f}" y="{H-6}" font-size="9" text-anchor="middle" fill="{DIM}">2025</text>')
    g.append(f'<text x="{sx(7.0):.1f}" y="{H-6}" font-size="9" text-anchor="middle" fill="{DIM}">2026</text>')
    g.append(f'<text x="{sx(n-1)-2:.1f}" y="{sy(1.97)-5:.1f}" font-size="9" text-anchor="end" fill="{INK}">+1.97</text>')
    g.append('</svg>'); return ''.join(g)

def chances(W,H):
    # NOAA CPC, roni/probabilities/, issued November 2026 (read 2026-11-16)
    seas=['OND','NDJ','DJF','JFM','FMA','MAM','AMJ']
    a=[100,100,100,100,98,80,38]
    padL,padR,padT,padB=10,10,16,30
    n=len(seas); cw=(W-padL-padR)/n
    sy=lambda p: padT+(100-p)/100*(H-padT-padB)
    g=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="NOAA&#39;s chance of El Nino by season, issued November 2026: 100 percent for October-December through January-March, 98 for February-April, 80 for March-May, 38 for April-June">']
    g.append(f'<line x1="{padL}" x2="{W-padR}" y1="{sy(0):.1f}" y2="{sy(0):.1f}" stroke="#333"/>')
    for i,s in enumerate(seas):
        x=padL+i*cw
        g.append(f'<rect x="{x+cw*0.18:.1f}" y="{sy(a[i]):.1f}" width="{cw*0.64:.1f}" height="{sy(0)-sy(a[i]):.1f}" fill="{RED}"/>')
        g.append(f'<text x="{x+cw/2:.1f}" y="{sy(a[i])-3:.1f}" font-size="9" text-anchor="middle" fill="{INK}">{a[i]}%</text>')
        g.append(f'<text x="{x+cw/2:.1f}" y="{H-16}" font-size="9.5" text-anchor="middle" fill="{DIM}">{s}</text>')
    g.append(f'<text x="{padL}" y="{H-3}" font-size="8.5" fill="{DIM}">Seasons from Oct-Dec 2026 to Apr-Jun 2027</text>')
    g.append('</svg>'); return ''.join(g)

def pacific(W,H):
    # Simplified map of the tropical Pacific, 120E to 70W, 30S to 30N. Not to scale in detail.
    # Nino 3.4 box: 5N-5S, 170W-120W (NOAA CPC ONI and RONI pages).
    def panel(y0,h,title,phase):
        X=lambda lonE: 6+(lonE-120)/190*(W-12)
        Y=lambda lat: y0+20+(30-lat)/60*(h-26)
        g=[f'<text x="6" y="{y0+12}" font-size="11" font-weight="600" fill="{INK}">{title}</text>']
        g.append(f'<rect x="6" y="{Y(30):.1f}" width="{W-12}" height="{Y(-30)-Y(30):.1f}" fill="#d6e6f4"/>')
        # water temperature
        if phase=='neutral':
            g.append(f'<ellipse cx="{X(150):.1f}" cy="{Y(0):.1f}" rx="{X(178)-X(150):.1f}" ry="{Y(-9)-Y(0):.1f}" fill="{RED}" opacity="0.8"/>')
            g.append(f'<ellipse cx="{X(262):.1f}" cy="{Y(-1):.1f}" rx="{X(285)-X(262):.1f}" ry="{Y(-5)-Y(0):.1f}" fill="{BLUE}" opacity="0.8"/>')
        elif phase=='lanina':
            g.append(f'<ellipse cx="{X(146):.1f}" cy="{Y(0):.1f}" rx="{X(166)-X(146):.1f}" ry="{Y(-10)-Y(0):.1f}" fill="{RED}" opacity="0.85"/>')
            g.append(f'<ellipse cx="{X(240):.1f}" cy="{Y(-1):.1f}" rx="{X(286)-X(240):.1f}" ry="{Y(-6)-Y(0):.1f}" fill="{BLUE}" opacity="0.85"/>')
        else:
            g.append(f'<ellipse cx="{X(225):.1f}" cy="{Y(0):.1f}" rx="{X(282)-X(225):.1f}" ry="{Y(-7)-Y(0):.1f}" fill="{RED}" opacity="0.75"/>')
            g.append(f'<ellipse cx="{X(148):.1f}" cy="{Y(0):.1f}" rx="{X(162)-X(148):.1f}" ry="{Y(-6)-Y(0):.1f}" fill="{RED}" opacity="0.35"/>')
        # land, simplified
        land='#c9b98f'
        def poly(pts): return '<polygon points="'+' '.join(f'{X(lo):.1f},{Y(la):.1f}' for lo,la in pts)+f'" fill="{land}"/>'
        g.append(poly([(120,30),(134,30),(130,25),(122,21),(120,21)]))
        g.append(poly([(120,8),(127,10),(126,0),(141,-2),(150,-6),(141,-9),(130,-4),(120,-6)]))
        g.append(poly([(120,-15),(131,-12),(142,-11),(146,-19),(153,-28),(151,-30),(120,-30)]))
        g.append(poly([(253,30),(255,22),(265,16),(275,9),(280,7),(280,1),(279,-4),(282,-14),(289,-19),(290,-30),(311,-30),(311,30)]))
        # equator and Nino 3.4 box
        g.append(f'<line x1="6" x2="{W-6}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" stroke="#555" stroke-width="0.8" stroke-dasharray="2 3"/>')
        g.append(f'<rect x="{X(190):.1f}" y="{Y(5):.1f}" width="{X(240)-X(190):.1f}" height="{Y(-5)-Y(5):.1f}" fill="none" stroke="#111" stroke-width="1.4"/>')
        g.append(f'<text x="{(X(190)+X(240))/2:.1f}" y="{Y(5)-3:.1f}" font-size="9" text-anchor="middle" fill="#111">Nino 3.4</text>')
        g.append(f'<text x="{X(122):.1f}" y="{Y(26):.1f}" font-size="8.5" fill="{INK}">Asia</text>')
        g.append(f'<text x="{X(126):.1f}" y="{Y(-22):.1f}" font-size="8.5" fill="{INK}">Australia</text>')
        g.append(f'<text x="{X(292):.1f}" y="{Y(-8):.1f}" font-size="8.5" fill="{INK}">S. America</text>')
        g.append(f'<text x="{X(232):.1f}" y="{Y(-25):.1f}" font-size="8" fill="{DIM}">equator (dotted)</text>')
        # trade winds
        ay=Y(13)
        def arrow(x1,x2,w,label):
            return [f'<line x1="{X(x1):.1f}" y1="{ay:.1f}" x2="{X(x2)+4:.1f}" y2="{ay:.1f}" stroke="#111" stroke-width="{w}"/><polygon points="{X(x2):.1f},{ay:.1f} {X(x2)+3+2*w:.1f},{ay-2-1.5*w:.1f} {X(x2)+3+2*w:.1f},{ay+2+1.5*w:.1f}" fill="#111"/>',
                    f'<text x="{(X(x1)+X(x2))/2:.1f}" y="{ay-6:.1f}" font-size="8.5" text-anchor="middle" fill="#111">{label}</text>']
        if phase=='neutral': g+=arrow(250,185,2,'trade winds')
        elif phase=='lanina': g+=arrow(270,170,3.2,'stronger trade winds')
        else: g+=arrow(228,206,1.2,'weak trade winds')
        return g
    g=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Simplified map of the tropical Pacific, Asia and Australia on the left and the Americas on the right, with the Nino 3.4 box on the equator. El Nino: weak trade winds, the warm water spread east to the Americas. Neutral: trade winds, warm water in the west, cooler water in the east. La Nina: stronger trade winds, more warm water pushed toward Asia, more cool water in the east.">']
    ph=(H-14)/3
    g+=panel(0,ph-4,'El Nino','elnino')
    g+=panel(ph+2,ph-4,'Neutral','neutral')
    g+=panel(2*ph+4,ph-4,'La Nina','lanina')
    g.append(f'<text x="{W-6}" y="{H-2}" font-size="8" text-anchor="end" fill="{DIM}">Red: warm water. Blue: cool water. Simplified map.</text>')
    g.append('</svg>'); return ''.join(g)

def heat(W,H):
    g=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Sketch with no time axis: in La Nina years the ocean takes heat in; in El Nino years it gives heat back to the air and more leaves to space.">']
    half=W/2
    for k,(ttl,col,arrow_up) in enumerate([('La Nina: the ocean takes heat in',BLUE,False),('El Nino: the ocean gives heat back',RED,True)]):
        x0=k*half+6; w=half-12
        g.append(f'<rect x="{x0}" y="70" width="{w}" height="{H-80}" fill="{col}" opacity="0.85" rx="4"/>')
        g.append(f'<text x="{x0+w/2}" y="{H-14}" font-size="9" text-anchor="middle" fill="#fff">ocean</text>')
        cx=x0+w/2
        if arrow_up:
            g.append(f'<line x1="{cx}" y1="68" x2="{cx}" y2="28" stroke="#111" stroke-width="2.5"/><polygon points="{cx},20 {cx-6},30 {cx+6},30" fill="#111"/>')
        else:
            g.append(f'<line x1="{cx}" y1="20" x2="{cx}" y2="60" stroke="#111" stroke-width="2.5"/><polygon points="{cx},68 {cx-6},58 {cx+6},58" fill="#111"/>')
        for j,line in enumerate(ttl.split(': ')):
            g.append(f'<text x="{cx}" y="{10+j*0+0}" font-size="0"></text>')
        g.append(f'<text x="{cx}" y="12" font-size="10" font-weight="600" text-anchor="middle" fill="{INK}">{ttl.split(":")[0]}</text>')
        g.append(f'<text x="{cx+10}" y="48" font-size="8.5" fill="{INK}">heat {"out" if arrow_up else "in"}</text>')
    g.append('</svg>'); return ''.join(g)

OUT={'seesaw':seesaw(358,220),'seesaw_c':seesaw(358,240),'zoom':zoom(358,190),'chances':chances(358,170),'pacific':pacific(358,500),'heat':heat(358,150)}
for k in OUT:
    OUT[k]=OUT[k].replace('Nino','Ni\u00f1o').replace('Nina','Ni\u00f1a')
json.dump(OUT,open('mockup_svgs.json','w'))
print('ok')