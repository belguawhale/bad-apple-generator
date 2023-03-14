from PIL import Image
import json

WIDTH = 36
HEIGHT = 28

PIXEL_SIZE = 50

source_imgs = [Image.open("data/0alice.png").resize((PIXEL_SIZE, PIXEL_SIZE)), Image.open("data/1marisa.jpg").resize((PIXEL_SIZE, PIXEL_SIZE))]

with open("data.json") as f:
    data = json.load(f)

    for i, frame in enumerate(data): # 4382 frames
        if i % 100 == 0:
            print("Processing frame", i)
        frame_out = Image.new("RGB", (WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE))
        for j, row in enumerate(frame): # 28 rows
            for k, pixel in enumerate(row): # 36 pixels
                frame_out.paste(source_imgs[pixel], (PIXEL_SIZE * k, PIXEL_SIZE * j))
        frame_out.save(f"output/{i:04}.jpg")