"""Render SheltrX Instagram carousel slides (1080x1350) to JPEG with headless Chrome.

Usage: python3 make_slides.py slides.json out_dir
slides.json: {"slides": [{"kind": "cover|stake|point|recap|cta", ...}]}
"""
import base64, json, os, subprocess, sys, tempfile

NAVY = "#18293D"
PURPLE = "#6856E6"
BG = "#F4F2FF"
HANDLE = "@sheltrx"

LOGO = base64.b64encode(open(os.path.join(os.path.dirname(__file__), "img/logo.png"), "rb").read()).decode()

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{BG};font-family:'Poppins',sans-serif;color:{NAVY};
 position:relative;overflow:hidden}}
.wrap{{position:absolute;inset:130px 120px 170px 120px;display:flex;flex-direction:column;justify-content:center}}
.brand{{position:absolute;left:120px;bottom:70px;display:flex;align-items:center;gap:16px;font:600 32px Poppins}}
.brand img{{height:46px}}
.count{{position:absolute;right:120px;bottom:76px;font:500 30px Inter;color:{PURPLE}}}
.kicker{{font:600 34px Inter;color:{PURPLE};letter-spacing:2px;text-transform:uppercase;margin-bottom:36px}}
h1{{font:700 112px/1.08 Poppins;letter-spacing:-2px}}
h2{{font:700 84px/1.12 Poppins;letter-spacing:-1px}}
p{{font:400 46px/1.45 Inter;margin-top:44px;color:#33445a}}
.num{{font:700 220px/1 Poppins;color:{PURPLE};opacity:.18;position:absolute;right:100px;top:110px}}
.bar{{width:120px;height:14px;background:{PURPLE};border-radius:7px;margin-bottom:48px}}
ul{{list-style:none;margin-top:30px}}
li{{font:500 50px/1.3 Inter;padding:26px 0;border-bottom:3px solid #dcd7fb;display:flex;gap:30px}}
li b{{color:{PURPLE};font-weight:700;min-width:50px}}
.cta{{background:{NAVY};color:#fff}}
.cta p{{color:#d9d6f5}}
.cta .brand{{color:#fff}}
.cta .brand img{{background:#fff;border-radius:12px;padding:6px}}
.pill{{display:inline-block;margin-top:60px;background:{PURPLE};color:#fff;font:600 44px Inter;padding:26px 46px;border-radius:60px;align-self:flex-start}}
"""


def body(s, i, n):
    k = s["kind"]
    foot = f'<div class="brand"><img src="data:image/png;base64,{LOGO}">{HANDLE}</div>'
    if k != "cover":
        foot += f'<div class="count">{i}/{n}</div>'
    if k == "cover":
        inner = f'<div class="bar"></div><h1>{s["title"]}</h1><p>{s["sub"]}</p>'
    elif k == "stake":
        inner = f'<h2>{s["title"]}</h2><p>{s["sub"]}</p>'
    elif k == "point":
        inner = (f'<div class="num">{s["n"]}</div><div class="kicker">Sawaal {s["n"]}</div>'
                 f'<h2>{s["title"]}</h2><p>{s["sub"]}</p>')
    elif k == "recap":
        items = "".join(f"<li><b>{j+1}</b>{t}</li>" for j, t in enumerate(s["items"]))
        inner = f'<div class="kicker">{s["title"]}</div><ul>{items}</ul>'
    elif k == "cta":
        inner = f'<h2>{s["title"]}</h2><p>{s["sub"]}</p><div class="pill">{s["pill"]}</div>'
    cls = ' class="cta"' if k == "cta" else ""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body{cls}><div class='wrap'>{inner}</div>{foot}</body></html>"


def main(spec, out):
    os.makedirs(out, exist_ok=True)
    slides = json.load(open(spec))["slides"]
    n = len(slides)
    tmp = tempfile.mkdtemp()
    for i, s in enumerate(slides, 1):
        html = os.path.join(tmp, f"s{i}.html")
        open(html, "w", encoding="utf-8").write(body(s, i, n))
        png = os.path.join(tmp, f"s{i}.png")
        subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--window-size=1080,1350",
                        f"--screenshot={png}", "file://" + html], check=True, capture_output=True)
        from PIL import Image
        Image.open(png).convert("RGB").save(os.path.join(out, f"{i:02d}.jpg"), quality=92)
        print("slide", i)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
