import os.path
import json
from PIL import Image, ImageDraw, ImageFont


INSPIRE_BLUE = (60, 105, 204)

MAX_NUMBER = 100


def make_icons(width: int = 500, height: int = 500):
    # get a font
    fnt = ImageFont.truetype("/Users/nicholasbarrow/Library/Fonts/PublicSans-Black.ttf", width // 2)

    out_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist")

    for i in range(1, MAX_NUMBER):

        # create the main sprite
        out = Image.new("RGBA", (width, height), (255, 255, 255, 0))

        fnt_w, fnt_h = fnt.getsize(str(i))

        w_pos = ((width - fnt_w) // 2)
        h_pos = ((height - fnt_h) // 2) - (width//16)  # end is custom offset

        # get a drawing context
        draw_tool = ImageDraw.Draw(out)

        # draw the circle
        draw_tool.ellipse((0, 0, width, height - 1,), fill=(255, 255, 255), outline=INSPIRE_BLUE, width=width // 16)

        # draw text
        draw_tool.text((w_pos, h_pos), f"{i}", font=fnt, fill=INSPIRE_BLUE)

        # save the image
        out.save(os.path.join(out_dir, f"inspire-stop-{i}.png"))


def make_sprite(width: int = 32, height: int = 32, is_2x: bool = False):

    # get a font
    fnt = ImageFont.truetype("/Users/nicholasbarrow/Library/Fonts/PublicSans-Black.ttf", width // 2)

    # create the main sprite
    sprite = Image.new("RGBA", (width, MAX_NUMBER * height), (255, 255, 255, 0))

    out_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist")

    for i in range(1, MAX_NUMBER):

        fnt_w, fnt_h = fnt.getsize(str(i))

        w_pos = ((width - fnt_w) // 2)
        h_pos = ((height - fnt_h) // 2) - 2  # - 2 is custom offset

        # get a drawing context
        sprite_d = ImageDraw.Draw(sprite)

        # draw the circle
        sprite_d.ellipse((0, (height * i) - height, width, (height * i) - 1), fill=(255, 255, 255), outline=INSPIRE_BLUE, width=width // 16)

        # draw text
        sprite_d.text((w_pos, (height * i) - height + h_pos), f"{i}", font=fnt, fill=INSPIRE_BLUE)

    # save the sprite
    filename = f"sprite@2x.png" if is_2x else f"sprite.png"
    sprite.save(os.path.join(out_dir, filename))

    # generate the sprite json
    stops = {}
    for i in range(1, MAX_NUMBER):
        stops[f"inspire-stop-{i}"] = {
            "width": width,
            "height": height,
            "x": 0,
            "y": (height * i) - height,
            "pixelRatio": 1
        }

    # save the JSON
    filename = f"sprite@2x.json" if is_2x else f"sprite.json"
    out_path = os.path.join(out_dir, filename)
    if os.path.exists(out_path):
        os.remove(out_path)
    with open(out_path, "w") as outfile:
        json.dump(stops, outfile)


if __name__ == "__main__":
    make_sprite(32, 32, False)
    make_sprite(64, 64, True)
    make_icons(500, 500)
