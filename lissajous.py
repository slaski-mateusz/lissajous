import tkinter as tk
import colorsys as cs
from matplotlib import colors
from time import sleep
from math import sin, cos

num_of_segments = 1024
cv_width = 500
cv_height = 500

fig_scale = 0.8

fig_ws = 0.5 * fig_scale * cv_width
fig_hs = 0.5 * fig_scale * cv_height

rad_speed_1 = 0.19
rad_speed_2 = 0.23

animation_refresh = 0.0

base_width = 4
min_width = 3
base_fill = "#ffffff"

line_ids = []


def main():
    window = tk.Tk()
    window.geometry(f"{cv_width}x{cv_height}")
    cv = tk.Canvas(window)
    cv.configure(bg="black")
    cv.pack(fill="both",expand=True)
    rad_1 = 0.0
    rad_2 = 0.0
    px = cv_width/2 +fig_ws * sin(rad_1)
    py = cv_height/2 + fig_hs * cos(rad_2)
    
    while True:
        window.update()
        sleep(animation_refresh)
        rad_1 += rad_speed_1
        rad_2 += rad_speed_2
        nx = cv_width/2 +fig_ws * sin(rad_1)
        ny = cv_height/2 + fig_hs * cos(rad_2)
        lid = cv.create_line(
            (px, py, nx, ny),
            fill=base_fill,
            width=base_width,
            smooth=True,
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND
            )
        line_ids.append(lid)
        if len(line_ids) > num_of_segments:
            cv.delete(line_ids[0])
            line_ids.pop(0)
        num_segments = len(line_ids)
        for ll in line_ids:
            lw  = float(cv.itemcget(ll, "width"))
            nlw = lw - base_width / num_segments
            if nlw < min_width:
                nlw = min_width
            fill = cv.itemcget(ll, "fill")
            rgb = colors.hex2color(fill)
            new_rgb = []
            for cch in rgb:
                new_cch = cch - 1/num_segments
                if new_cch <= 0:
                    new_cch = 1/256
                new_rgb.append(new_cch)
            new_fill = colors.rgb2hex(new_rgb)
            cv.itemconfig(ll, fill=new_fill, width=nlw)
        px = nx
        py = ny


if __name__ == "__main__":
    main()