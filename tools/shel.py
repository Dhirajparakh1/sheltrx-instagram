"""Shel: the SheltrX page character. LOCKED LOOK - do not redesign.

A purple (#6856E6) rounded-dome body, two big white oval eyes with navy pupils,
navy brows, soft darker-purple cheeks, round purple hands. Flat style, no outlines
on the body. He is 24, works a 9-to-5, and reacts to news and trends through how
they hit his own everyday life.

shel(expr, cx, cy, s, props) returns an SVG <g> string. (cx, cy) is the centre of
the dome's arc (roughly eye level); s is scale (1.0 = 360px wide body).
Expressions: neutral, happy, shocked, tired, annoyed, sad, thinking, phone
Props: "lanyard" (office ID card), "phone", "chai", "laptop"
"""

PURPLE = "#6856E6"
DARK = "#4b3bc4"
NAVY = "#18293D"

# per expression: pupil (dx, dy, r), brows (left path, right path), mouth path, extras
EXPR = {
    "neutral": dict(p=(0, 6, 22), bl="M-135 -52 q55 -14 105 0", br="M30 -52 q50 -14 105 0",
                    m='<path d="M-34 78 q34 26 68 0" stroke="{n}" stroke-width="9" fill="none" stroke-linecap="round"/>'),
    "happy": dict(arc=True, bl="M-135 -70 q55 -18 105 -4", br="M30 -66 q50 -18 105 -4",
                  m='<path d="M-48 70 q48 62 96 0 z" fill="{n}"/><path d="M-26 96 q26 16 52 0 q-26 -14 -52 0z" fill="#ff8b8b"/>'),
    "shocked": dict(p=(0, 4, 12), bl="M-135 -88 q55 -24 105 -6", br="M30 -94 q50 -24 105 -6",
                    m='<ellipse cx="0" cy="92" rx="24" ry="30" fill="{n}"/>'),
    "tired": dict(p=(0, 22, 20), lid=0.5, bl="M-135 -46 q55 4 105 6", br="M30 -40 q50 -4 105 -6",
                  m='<path d="M-28 88 h56" stroke="{n}" stroke-width="9" stroke-linecap="round"/>',
                  x='<path d="M-118 62 q38 16 76 0" stroke="{d}" stroke-width="7" fill="none" stroke-linecap="round"/>'
                    '<path d="M42 62 q38 16 76 0" stroke="{d}" stroke-width="7" fill="none" stroke-linecap="round"/>'),
    "annoyed": dict(p=(16, 8, 20), lid=0.32, bl="M-135 -64 q55 6 105 26", br="M30 -38 q50 -20 105 -26",
                    m='<path d="M-30 92 q30 -14 60 0" stroke="{n}" stroke-width="9" fill="none" stroke-linecap="round"/>'),
    "sad": dict(p=(0, 20, 22), bl="M-135 -40 q50 -30 105 -34", br="M30 -74 q55 4 105 34",
                m='<path d="M-32 100 q32 -30 64 0" stroke="{n}" stroke-width="9" fill="none" stroke-linecap="round"/>',
                x='<path d="M-120 60 q-14 26 0 40 q14 -14 0 -40z" fill="#9fd6ff"/>'),
    "thinking": dict(p=(18, -20, 20), bl="M-135 -60 q55 -14 105 0", br="M30 -84 q50 -20 105 -8",
                     m='<path d="M-6 90 q24 -10 44 4" stroke="{n}" stroke-width="9" fill="none" stroke-linecap="round"/>'),
    "phone": dict(p=(-6, 22, 22), bl="M-135 -45 q55 -22 105 6", br="M30 -39 q50 -28 105 -6", m=""),
}


def shel(expr="neutral", cx=540, cy=690, s=1.0, props=()):
    e = EXPR[expr]
    f = lambda t: t.format(n=NAVY, d=DARK)
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<path d="M-180 210 V0 a180 190 0 0 1 360 0 V210 z" fill="{PURPLE}"/>')
    for ex in (-80, 80):
        if e.get("arc"):
            g.append(f'<path d="M{ex-40} 22 q40 -56 80 0" stroke="{NAVY}" stroke-width="12" fill="none" stroke-linecap="round"/>')
            continue
        g.append(f'<ellipse cx="{ex}" cy="10" rx="48" ry="54" fill="#fff"/>')
        dx, dy, r = e["p"]
        g.append(f'<circle cx="{ex+dx}" cy="{10+dy}" r="{r}" fill="{NAVY}"/>')
        if e.get("lid"):
            h = 108 * e["lid"]
            g.append(f'<rect x="{ex-52}" y="-46" width="104" height="{h}" fill="{PURPLE}"/>')
            g.append(f'<path d="M{ex-48} {-46+h} h96" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<path d="{e["bl"]}" stroke="{NAVY}" stroke-width="10" fill="none" stroke-linecap="round"/>')
    g.append(f'<path d="{e["br"]}" stroke="{NAVY}" stroke-width="10" fill="none" stroke-linecap="round"/>')
    if "x" not in e or expr == "sad":
        g.append(f'<ellipse cx="-96" cy="84" rx="30" ry="9" fill="{DARK}" opacity=".6"/><ellipse cx="96" cy="84" rx="30" ry="9" fill="{DARK}" opacity=".6"/>')
    g.append(f(e.get("x", "")))
    g.append(f(e["m"]))
    if "lanyard" in props:
        g.append(f'<path d="M-70 150 L0 205 L70 150" stroke="{NAVY}" stroke-width="8" fill="none"/>'
                 f'<rect x="-30" y="196" width="60" height="14" rx="4" fill="#fff"/>')
    if "phone" in props or expr == "phone":
        g.append('<rect x="-60" y="110" width="120" height="78" rx="12" fill="#0b1420"/><rect x="-52" y="118" width="104" height="62" rx="6" fill="#d5ecff"/>'
                 f'<circle cx="-70" cy="160" r="26" fill="{PURPLE}" stroke="{DARK}" stroke-width="6"/><circle cx="70" cy="160" r="26" fill="{PURPLE}" stroke="{DARK}" stroke-width="6"/>')
    if "chai" in props:
        g.append('<path d="M96 120 h64 l-8 70 h-48z" fill="#fff"/><path d="M100 128 h56 l-2 16 h-52z" fill="#b9793f"/>'
                 '<path d="M118 104 q-10 -16 0 -30 M140 104 q-10 -16 0 -30" stroke="#fff" stroke-width="5" fill="none" opacity=".7" stroke-linecap="round"/>'
                 f'<circle cx="92" cy="160" r="26" fill="{PURPLE}" stroke="{DARK}" stroke-width="6"/>')
    if "laptop" in props:
        g.append('<rect x="-130" y="120" width="260" height="96" rx="12" fill="#cfd6e0"/><circle cx="0" cy="168" r="14" fill="#fff"/>'
                 f'<circle cx="-140" cy="196" r="26" fill="{PURPLE}" stroke="{DARK}" stroke-width="6"/><circle cx="140" cy="196" r="26" fill="{PURPLE}" stroke="{DARK}" stroke-width="6"/>')
    g.append("</g>")
    return "".join(g)


if __name__ == "__main__":
    import subprocess, sys, os
    out = sys.argv[1] if len(sys.argv) > 1 else "shel_sheet.png"
    cells = [("neutral", (), "Normal"), ("happy", (), "Khush"), ("shocked", (), "Shock"), ("tired", ("lanyard",), "Thaka hua"),
             ("annoyed", ("laptop",), "Chidha hua"), ("sad", (), "Udaas"), ("thinking", ("chai",), "Soch raha hai"), ("phone", (), "Phone mein")]
    W, H = 2160, 1500
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#F4F2FF"/>']
    svg.append(f'<text x="80" y="120" font-family="Poppins" font-weight="700" font-size="72" fill="{NAVY}">Shel: character sheet</text>')
    for i, (ex, pr, lab) in enumerate(cells):
        x = 80 + (i % 4) * 510; y = 190 + (i // 4) * 640
        svg.append(f'<rect x="{x}" y="{y}" width="470" height="590" rx="28" fill="#fff"/>')
        svg.append(shel(ex, x + 235, y + 260, 0.95, pr))
        svg.append(f'<rect x="{x}" y="{y+470}" width="470" height="120" fill="#fff"/><rect x="{x}" y="{y+462}" width="470" height="10" fill="#e9e6fb"/>')
        svg.append(f'<text x="{x+235}" y="{y+545}" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="40" fill="{NAVY}">{lab}</text>')
    svg.append("</svg>")
    html = os.path.abspath("_sheet.html")
    open(html, "w").write("<!doctype html><meta charset='utf-8'><body style='margin:0'>" + "".join(svg))
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", f"--screenshot={out}", "file://" + html], check=True, capture_output=True)
    os.remove(html)
