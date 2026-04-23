import tkinter as tk
import math

def parametric_points(t_min, t_max, steps=6000):
    points = []
    dt = (t_max - t_min) / steps
    prev_ok = False
    segment = []
    for i in range(steps + 1):
        t = t_min + i * dt
        try:
            x = math.sin(t + math.pi / 2)         
            tan_t = math.tan(t)
            if abs(tan_t) > 1e6:                    
                if segment:
                    points.append(segment)
                segment = []
                continue
            y = math.cos(t) * tan_t             
            if math.isfinite(x) and math.isfinite(y):
                segment.append((x, y))
            else:
                if segment:
                    points.append(segment)
                segment = []
        except (ValueError, ZeroDivisionError):
            if segment:
                points.append(segment)
            segment = []
    if segment:
        points.append(segment)
    return points

root = tk.Tk()
root.title("Параметричний графік — Варіант 5")

W, H = 820, 680
canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

T_MIN, T_MAX = -3 * math.pi, 3 * math.pi
segments = parametric_points(T_MIN, T_MAX, steps=8000)

all_pts = [p for seg in segments for p in seg]
xs = [p[0] for p in all_pts]
ys = [p[1] for p in all_pts]

MARGIN = 70
x_data_min, x_data_max = min(xs) - 0.15, max(xs) + 0.15
y_data_min, y_data_max = max(min(ys), -4) - 0.2, min(max(ys), 4) + 0.2

def to_canvas(x, y):
    cx = MARGIN + (x - x_data_min) / (x_data_max - x_data_min) * (W - 2 * MARGIN)
    cy = H - MARGIN - (y - y_data_min) / (y_data_max - y_data_min) * (H - 2 * MARGIN)
    return cx, cy

def from_canvas_x(cx):
    return x_data_min + (cx - MARGIN) / (W - 2 * MARGIN) * (x_data_max - x_data_min)

def from_canvas_y(cy):
    return y_data_min + (H - MARGIN - cy) / (H - 2 * MARGIN) * (y_data_max - y_data_min)

ox, oy = to_canvas(0, 0)  

arrow_opts = dict(fill="#222222", width=2)

canvas.create_line(MARGIN - 15, oy, W - MARGIN + 20, oy, arrow=tk.LAST, **arrow_opts)
canvas.create_text(W - MARGIN + 25, oy, text="x", font=("Arial", 13, "italic"))

canvas.create_line(ox, H - MARGIN + 15, ox, MARGIN - 20, arrow=tk.LAST, **arrow_opts)
canvas.create_text(ox, MARGIN - 28, text="y", font=("Arial", 13, "italic"))

canvas.create_text(ox - 14, oy + 14, text="0", font=("Arial", 10))

TICK = 5
tick_font = ("Arial", 9)

step_x = 0.5
v = math.ceil(x_data_min / step_x) * step_x
while v <= x_data_max + 1e-9:
    cx, _ = to_canvas(v, 0)
    canvas.create_line(cx, oy - TICK, cx, oy + TICK, fill="#444444")
    if abs(v) > 0.01:
        label = f"{v:.1f}" if abs(v) < 10 else f"{int(v)}"
        canvas.create_text(cx, oy + 14, text=label, font=tick_font)
    v = round(v + step_x, 10)

step_y = 0.5
v = math.ceil(y_data_min / step_y) * step_y
while v <= y_data_max + 1e-9:
    _, cy = to_canvas(0, v)
    canvas.create_line(ox - TICK, cy, ox + TICK, cy, fill="#444444")
    if abs(v) > 0.01:
        label = f"{v:.1f}" if abs(v) < 10 else f"{int(v)}"
        canvas.create_text(ox - 22, cy, text=label, font=tick_font)
    v = round(v + step_y, 10)

for seg in segments:
    if len(seg) < 2:
        continue
    flat = []
    for (x, y) in seg:
        cx, cy = to_canvas(x, y)
        flat += [cx, cy]
    canvas.create_line(flat, fill="#1565C0", width=2, smooth=True)

formula_font = ("Arial", 12, "italic")
canvas.create_text(
    MARGIN + 10, MARGIN - 10,
    anchor="nw",
    text="x(t) = sin(t + π/2)",
    font=formula_font,
    fill="#B71C1C"
)
canvas.create_text(
    MARGIN + 10, MARGIN + 10,
    anchor="nw",
    text="y(t) = cos(t)·tan(t)",
    font=formula_font,
    fill="#B71C1C"
)

canvas.create_text(
    W - 8, H - 8,
    anchor="se",
    text="Кравчук О.С.",         
    font=("Arial", 8),
    fill="#555555"
)

root.mainloop()