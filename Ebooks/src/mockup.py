"""Gera Ebooks/mockup-ebook.png (PNG transparente): 2 livros deitados + 1 em pe sobre eles.
Projecao 3D calculada em Python (sem CSS 3D). Uso: python Ebooks/src/mockup.py"""
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'mockup-ebook.png')
S = 2                      # supersample
CW, CH = 1500 * S, 1500 * S
W, H, D = 470.0, 665.0, 50.0
YAW, PITCH = math.radians(-30), math.radians(24)
FOCAL, DIST = 3400.0, 3400.0
CX, CY = CW / 2, CH * 0.60

cover = Image.open(os.path.join(HERE, 'img', 'capa-render.jpg')).convert('RGB')


def font(size):
    for f in ('C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/arialbd.ttf'):
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def spine_tex():
    w, h = int(D * 4), int(H * 4)
    g = np.zeros((h, w, 3), np.uint8)
    xs = np.linspace(0, 1, w)[None, :, None]
    c0, c1, c2 = np.array([185, 63, 24]), np.array([240, 138, 98]), np.array([217, 83, 44])
    col = np.where(xs < .55, c0 + (c1 - c0) * (xs / .55), c1 + (c2 - c1) * ((xs - .55) / .45))
    g[:] = col.astype(np.uint8)
    im = Image.fromarray(g)
    # texto horizontal -> rotaciona (le de cima para baixo)
    t = Image.new('RGBA', (h, w), (0, 0, 0, 0))
    d = ImageDraw.Draw(t)
    f = font(int(w * .36))
    txt = 'LIMPEZA INTESTINAL EM 3 DIAS   |   LUÍS MANOEL'
    tw = d.textlength(txt, font=f)
    d.text(((h - tw) / 2, w * .30), txt, font=f, fill=(255, 255, 255, 255))
    t = t.rotate(-90, expand=True)
    im.paste(t, (0, 0), t)
    return im


def pages_tex(vertical):
    n = 60
    a = np.zeros((n, 8, 3), np.uint8)
    for i in range(n):
        a[i, :] = (255, 255, 255) if i % 4 else (226, 217, 208)
    im = Image.fromarray(a)
    return im.rotate(90, expand=True) if vertical else im


SPINE, PG_V, PG_H = spine_tex(), pages_tex(True), pages_tex(False)


def rot_y(v, a):
    c, s = math.cos(a), math.sin(a)
    return np.array([v[0] * c + v[2] * s, v[1], -v[0] * s + v[2] * c])


def project(p):
    p = rot_y(p, YAW)
    c, s = math.cos(PITCH), math.sin(PITCH)
    y2 = p[1] * c - p[2] * s
    z2 = p[1] * s + p[2] * c
    w = DIST - z2
    return (CX + S * FOCAL * p[0] / w, CY - S * FOCAL * y2 / w), z2


def cam_normal_z(n):
    n = rot_y(n, YAW)
    c, s = math.cos(PITCH), math.sin(PITCH)
    return n[1] * s + n[2] * c


def coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float))


def draw_face(canvas, tex, corners):
    """corners: TL,TR,BR,BL em coords de mundo."""
    pts = [project(c)[0] for c in corners]
    tw, th = tex.size
    src = [(0, 0), (tw, 0), (tw, th), (0, th)]
    co = coeffs(pts, src)
    layer = tex.convert('RGBA').transform((CW, CH), Image.PERSPECTIVE, tuple(co), Image.BICUBIC)
    mask = Image.new('L', (CW, CH), 0)
    ImageDraw.Draw(mask).polygon(pts, fill=255)
    layer.putalpha(Image.composite(layer.getchannel('A'), Image.new('L', (CW, CH), 0), mask))
    canvas.alpha_composite(layer)


def book(canvas, center, r, u, f, yaw):
    r, u, f = [rot_y(np.array(v, float), yaw) for v in (r, u, f)]
    c = np.array(center, float)
    hw, hh, hd = W / 2, H / 2, D / 2
    faces = []
    # frente (capa)
    faces.append((f, cover, [c + f * hd - r * hw + u * hh, c + f * hd + r * hw + u * hh,
                             c + f * hd + r * hw - u * hh, c + f * hd - r * hw - u * hh]))
    # lombada (esquerda)
    faces.append((-r, SPINE, [c - r * hw - f * hd + u * hh, c - r * hw + f * hd + u * hh,
                              c - r * hw + f * hd - u * hh, c - r * hw - f * hd - u * hh]))
    # paginas (direita)
    faces.append((r, PG_V, [c + r * hw + f * hd + u * hh, c + r * hw - f * hd + u * hh,
                            c + r * hw - f * hd - u * hh, c + r * hw + f * hd - u * hh]))
    # cabeca (topo) e pe (base)
    faces.append((u, PG_H, [c + u * hh - r * hw + f * hd, c + u * hh + r * hw + f * hd,
                            c + u * hh + r * hw - f * hd, c + u * hh - r * hw - f * hd]))
    faces.append((-u, PG_H, [c - u * hh - r * hw - f * hd, c - u * hh + r * hw - f * hd,
                             c - u * hh + r * hw + f * hd, c - u * hh - r * hw + f * hd]))
    vis = [(n, t, q) for n, t, q in faces if cam_normal_z(n) > 0]
    vis.sort(key=lambda a: sum(project(p)[1] for p in a[2]) / 4)
    for n, t, q in vis:
        draw_face(canvas, t, q)
    # brilho suave na capa
    return


canvas = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))

# sombra no chao
sh = Image.new('L', (CW, CH), 0)
ring = []
for i in range(48):
    a = 2 * math.pi * i / 48
    ring.append(project((math.cos(a) * 470, 0, math.sin(a) * 540))[0])
ImageDraw.Draw(sh).polygon(ring, fill=150)
sh = sh.filter(ImageFilter.GaussianBlur(40 * S))
shadow = Image.new('RGBA', (CW, CH), (60, 25, 5, 255))
shadow.putalpha(sh)
canvas.alpha_composite(shadow)

# livros deitados: capa para cima (f=+Y, u=-Z, r=+X)
book(canvas, (0, D / 2, 0), (1, 0, 0), (0, 0, -1), (0, 1, 0), math.radians(-5))
book(canvas, (10, D * 1.5, -6), (1, 0, 0), (0, 0, -1), (0, 1, 0), math.radians(6))
# livro em pe sobre os deitados (capa para frente)
book(canvas, (20, D * 2 + H / 2, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), math.radians(12))

bb = canvas.getbbox()
pad = 40 * S
canvas = canvas.crop((max(bb[0] - pad, 0), max(bb[1] - pad, 0), min(bb[2] + pad, CW), min(bb[3] + pad, CH)))
canvas.save(OUT, optimize=True)
print('ok', canvas.size)
