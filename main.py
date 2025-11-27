import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

fig, ax = plt.subplots()
center = 64

def make_tree(ax, on, x_space, y_space, light_color = None, black = False):
    # Create a fresh 128x128 RGB image each frame
    img = np.zeros((128, 128, 3), dtype=np.uint8)
    if black:
        ax.imshow(img)
        return None
    def draw_layer(img, y_top, y_bottom, spread, color, num_lights, on=on, x_space = x_space,
                  y_space = y_space, light_color = light_color):
        for y in range(y_top, y_bottom):
            half_width = int((y - y_top) * spread)
            img[y, center-half_width:center+half_width] = color

            low  = center - half_width
            high = center + half_width
            lx = list(range(low, high, x_space))
            if y%y_space == 0:
                colors = classic_light_colors = [
                        [255, 244, 214],  # warm white
                        [255, 0, 0],      # red
                        [0, 255, 0],      # green
                        [0, 102, 255],    # blue
                        [255, 215, 0],    # yellow/gold
                        [255, 140, 0],    # orange
                        [255, 105, 180],  # pink
                        [160, 32, 240],   # purple
                    ]
                if on:
                    if light_color is None:
                        img[y, lx] = random.choice(classic_light_colors)
                    else:
                        img[y, lx] = light_color # lights ON
                else:
                    img[y, lx] = [0, 0, 0]     # lights OFF

    # Draw layers
    draw_layer(img, 10, 45, 0.6, [0,150,0], 20)
    draw_layer(img, 35, 80, 0.8, [0,150,0], 20)
    draw_layer(img, 70, 105, 1.0, [0,150,0], 20)

    # Trunk
    img[105:122, 56:72] = [120, 70, 20]

    # Draw on the animation axes
    ax.imshow(img)
    ax.axis("off")

def update(frame):
    ax.clear()
    if frame > 1 and frame <= 2:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 2 and frame <= 3:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 30, light_color = [255,255,0])
    elif frame > 3 and frame <= 4:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])
    elif frame > 10 and frame <= 11:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 11 and frame <= 12:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 30, light_color = [255,255,0])
    elif frame > 12 and frame <= 13:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])
    elif frame > 18 and frame <= 19:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 19 and frame <= 20:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 30, light_color = [255,255,0])
    elif frame > 20 and frame <= 21:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])
    elif frame > 22 and frame <= 23:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 23 and frame <= 24:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 30, light_color = [255,255,0])
    elif frame > 24 and frame <= 25:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])
    elif frame > 26 and frame <= 27:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 28 and frame <= 29:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 30, light_color = [255,255,0])
    elif frame > 29 and frame <= 30:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])
    elif frame > 35 and frame <= 36:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 36 and frame <= 37:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 30, light_color = [255,255,0])
    elif frame > 37 and frame <= 38:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])   
    elif frame > 38 and frame <=53:
        lights_on = (frame % 2 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 30, light_color = [255,255,0])
    elif frame > 53 and frame <= 54:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 54 and frame <= 55:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 15, light_color = [255,255,0])
    elif frame > 55 and frame <= 56:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 7, light_color = [255,255,0])
    elif frame > 57 and frame <= 58:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, light_color = [255,255,0])
    elif frame > 58 and frame <= 59:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 3, y_space = 15, light_color = [255,255,0])
    elif frame > 59 and frame <= 60:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 7, light_color = [255,255,0]) 
    elif frame>60 and frame<=195:
        lights_on = (frame % 2 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 7)
    elif frame>195 and frame<=213:
        lights_on = (frame % 2 == 0)
        make_tree(ax, lights_on, x_space = 1, y_space = 5, light_color = [255,255,255])
    elif frame>213 and frame<=225:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3)
    elif frame>225 and frame<=227:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3, light_color = [255,0,0])
    elif frame>227 and frame<=230:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3, light_color = [0,255,0])
    elif frame>230 and frame<=242:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3)
    elif frame>242 and frame<=244:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3, light_color = [255,0,0])
    elif frame>244 and frame<=247:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3, light_color = [0,255,0])
    elif frame>247 and frame<=270:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3)
    elif frame>270 and frame<=273:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 6)
    elif frame>273 and frame<=276:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 12)
    elif frame>276 and frame<=279:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30)
    elif frame >288:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 30, black = True)
    else:
        lights_on = (frame % 1 == 0)
        make_tree(ax, lights_on, x_space = 5, y_space = 3, light_color = [0,150,0])


ani = FuncAnimation(
    fig,
    update,
    frames=300,      # True/False alternating
    interval=250,   # ms
    repeat=True
)

ani
