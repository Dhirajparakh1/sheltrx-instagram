"""Render one Shelu post (1080x1350 JPEG) or story (1080x1920 JPEG).

Usage: python3 make_post.py spec.json out.jpg [--story]
spec: {"theme": "night"|"day", "scene": "bed"|"desk"|"plain", "expr": "...", "props": [...],
       "chip": "small news label (optional)", "big": "big top text (optional)", "line": "Shelu's one line"}
"""
import json, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shel import shel, PURPLE, NAVY

THEMES = {"night": dict(bg="#0f1b2b", fg="#ffffff", sub="#8f84f0", big="#ff6b6b", chipbg="#1d2c42", chipfg="#cfd8e6", furn="#24364d", soft="#e9e6fb"),
          "day": dict(bg="#F4F2FF", fg=NAVY, sub=PURPLE, big=PURPLE, chipbg="#ffffff", chipfg=NAVY, furn="#d9d4fa", soft="#ffffff")}


def render(spec, out, story=False):
    t = THEMES[spec.get("theme", "night")]
    W, H = 1080, (1920 if story else 1350)
    oy = 285 if story else 0  # shift everything down for 9:16
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{t["bg"]}"/><g transform="translate(0,{oy})">']
    if spec.get("theme", "night") == "night":
        s.append('<rect x="770" y="330" width="210" height="260" rx="16" fill="#16263a" stroke="#24364d" stroke-width="10"/>'
                 '<line x1="875" y1="330" x2="875" y2="590" stroke="#24364d" stroke-width="8"/><line x1="770" y1="460" x2="980" y2="460" stroke="#24364d" stroke-width="8"/>'
                 '<circle cx="928" cy="395" r="32" fill="#f4efd2"/><circle cx="942" cy="387" r="28" fill="#16263a"/>'
                 '<circle cx="810" cy="370" r="4" fill="#fff"/><circle cx="820" cy="530" r="3" fill="#fff"/><circle cx="940" cy="540" r="4" fill="#fff"/>')
    if spec.get("chip"):
        w = 60 + len(spec["chip"]) * 19
        s.append(f'<rect x="100" y="110" width="{w}" height="64" rx="32" fill="{t["chipbg"]}"/>'
                 f'<text x="130" y="153" font-family="Inter" font-weight="600" font-size="30" fill="{t["chipfg"]}">{spec["chip"]}</text>')
    if spec.get("big"):
        s.append(f'<text x="100" y="300" font-family="Poppins" font-weight="700" font-size="96" fill="{t["big"]}">{spec["big"]}</text>')
    scene = spec.get("scene", "plain")
    s.append('<g transform="translate(0,-70)">')
    if scene == "bed":
        s.append(f'<rect x="120" y="600" width="110" height="420" rx="30" fill="{t["furn"]}"/><rect x="150" y="740" width="170" height="130" rx="50" fill="{t["soft"]}"/>')
    s.append(shel(spec.get("expr", "neutral"), 540, 730, 1.0, tuple(spec.get("props", []))))
    if scene == "bed":
        s.append(f'<path d="M120 940 h840 a30 30 0 0 1 30 30 v90 h-900 v-90 a30 30 0 0 1 30 -30z" fill="{t["soft"]}"/><rect x="90" y="1050" width="900" height="50" rx="14" fill="{t["furn"]}"/>')
    elif scene == "desk":
        s.append(f'<rect x="60" y="940" width="960" height="46" rx="14" fill="{t["furn"]}"/><rect x="130" y="986" width="40" height="50" fill="{t["furn"]}"/><rect x="910" y="986" width="40" height="50" fill="{t["furn"]}"/>')
    else:
        s.append(f'<ellipse cx="540" cy="948" rx="250" ry="22" fill="{t["furn"]}"/>')
    s.append("</g></g></svg>")
    lines = spec["line"].split("\n")
    m = max(len(x) for x in lines)
    size = 58 if m <= 28 else (46 if m <= 38 else 40)
    cap = "".join(f"<div>{x}</div>" for x in lines)
    bottom = (330 if story else 150)
    html = (f"<!doctype html><meta charset='utf-8'><style>*{{margin:0}}body{{width:{W}px;height:{H}px;position:relative;overflow:hidden}}"
            f".cap{{position:absolute;left:50px;right:50px;bottom:{bottom}px;text-align:center;color:{t['fg']};font:600 {size}px/1.3 Poppins}}"
            f".w{{position:absolute;left:0;right:0;bottom:{bottom-90}px;text-align:center;color:{t['sub']};font:600 32px Poppins;letter-spacing:1px}}</style>"
            f"<body>{''.join(s)}<div class='cap'>{cap}</div><div class='w'>sheltrx</div></body>")
    tmp = tempfile.mkdtemp(); h = os.path.join(tmp, "p.html"); png = os.path.join(tmp, "p.png")
    open(h, "w", encoding="utf-8").write(html)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", f"--screenshot={png}", "file://" + h], check=True, capture_output=True)
    from PIL import Image
    Image.open(png).convert("RGB").save(out, quality=92)


if __name__ == "__main__":
    render(json.load(open(sys.argv[1], encoding="utf-8")), sys.argv[2], "--story" in sys.argv)
