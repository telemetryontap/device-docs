"""Generate annotated screenshots for YUM machine documentation."""
from PIL import Image, ImageDraw, ImageFont
import os

IMG_DIR = os.path.join(os.path.dirname(__file__), "images")

def get_font(size):
    """Try to load a bold font, fall back to default."""
    try:
        return ImageFont.truetype("arialbd.ttf", size)
    except OSError:
        try:
            return ImageFont.truetype("arial.ttf", size)
        except OSError:
            return ImageFont.load_default()

def draw_circle_highlight(draw, cx, cy, radius, color="red", width=4):
    """Draw a circle highlight around a point."""
    draw.ellipse(
        [cx - radius, cy - radius, cx + radius, cy + radius],
        outline=color, width=width
    )

def draw_rect_highlight(draw, x1, y1, x2, y2, color="red", width=4):
    """Draw a rectangle highlight."""
    draw.rectangle([x1, y1, x2, y2], outline=color, width=width)

def draw_label(draw, x, y, text, font, color="red", bg_color="white"):
    """Draw a label with background."""
    bbox = draw.textbbox((x, y), text, font=font)
    padding = 6
    draw.rectangle(
        [bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding],
        fill=bg_color, outline=color, width=2
    )
    draw.text((x, y), text, fill=color, font=font)

def draw_arrow_line(draw, x1, y1, x2, y2, color="red", width=3):
    """Draw a line (arrow body)."""
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)


def annotate_recipe_build():
    """Annotate recipe_build.png - highlight trash icon, add ingredient button, quantity fields."""
    img = Image.open(os.path.join(IMG_DIR, "recipe_build.png"))
    draw = ImageDraw.Draw(img)
    font = get_font(20)
    small_font = get_font(16)
    w, h = img.size

    # Highlight trash icon on Ingredient 1 (icon at ~x=564-578, y=230-309)
    # Use a rectangle instead of circle to avoid right-edge clipping
    draw_rect_highlight(draw, 505, 245, 578, 300, color="#FF4444", width=4)
    draw_label(draw, 390, 220, "Delete", font, color="#FF4444", bg_color="#FFFFFF")
    draw_arrow_line(draw, 470, 238, 503, 260, color="#FF4444", width=3)

    # Highlight Quantity field on Ingredient 1 (text at y=401, +/- at y=420-429)
    draw_rect_highlight(draw, 240, 388, 515, 435, color="#44AAFF", width=3)
    draw_label(draw, 80, 395, "Amount", font, color="#44AAFF", bg_color="#FFFFFF")
    draw_arrow_line(draw, 170, 412, 238, 412, color="#44AAFF", width=3)

    # Highlight Flow Rate slider on Ingredient 1 (slider at y=460-476, x=256-524)
    draw_rect_highlight(draw, 240, 430, 530, 480, color="#44FF44", width=3)
    draw_label(draw, 80, 445, "Speed", font, color="#44FF44", bg_color="#FFFFFF")
    draw_arrow_line(draw, 150, 460, 238, 460, color="#44FF44", width=3)

    # Highlight ADD INGREDIENT button (y=999-1119, x=11-575)
    draw_rect_highlight(draw, 8, 995, 578, 1123, color="#FFaa00", width=5)
    draw_label(draw, 200, 1130, "Add New", font, color="#FFaa00", bg_color="#FFFFFF")

    img.save(os.path.join(IMG_DIR, "recipe_build_annotated.png"))
    print("Created recipe_build_annotated.png")


def annotate_product_select():
    """Annotate product_select.png - highlight menu icon and navigation."""
    img = Image.open(os.path.join(IMG_DIR, "product_select.png"))
    draw = ImageDraw.Draw(img)
    font = get_font(20)

    # Highlight menu icon (hamburger, top-left)
    draw_circle_highlight(draw, 43, 28, 30, color="#FFaa00", width=4)
    draw_label(draw, 85, 10, "Menu", font, color="#FFaa00", bg_color="#FFFFFF")
    draw_arrow_line(draw, 85, 28, 73, 28, color="#FFaa00", width=3)

    # Highlight PREV/MORE navigation (PREV around y=1065-1090, MORE same)
    draw_rect_highlight(draw, 0, 1060, 120, 1090, color="#44AAFF", width=3)
    draw_rect_highlight(draw, 630, 1060, 750, 1090, color="#44AAFF", width=3)
    draw_label(draw, 260, 1040, "More Drinks", font, color="#44AAFF", bg_color="#FFFFFF")

    img.save(os.path.join(IMG_DIR, "product_select_annotated.png"))
    print("Created product_select_annotated.png")


def annotate_drink_build():
    """Annotate drink_build.png - highlight size, room, start pour."""
    img = Image.open(os.path.join(IMG_DIR, "drink_build.png"))
    draw = ImageDraw.Draw(img)
    font = get_font(20)

    # Highlight Size column
    draw_rect_highlight(draw, 20, 85, 290, 265, color="#44AAFF", width=4)
    draw_label(draw, 80, 62, "Pick Size", font, color="#44AAFF", bg_color="#FFFFFF")

    # Highlight Room column
    draw_rect_highlight(draw, 300, 85, 565, 265, color="#44FF44", width=4)
    draw_label(draw, 355, 62, "Pick Room", font, color="#44FF44", bg_color="#FFFFFF")

    # Highlight Start Pour
    draw_rect_highlight(draw, 45, 830, 540, 880, color="#FFaa00", width=5)

    img.save(os.path.join(IMG_DIR, "drink_build_annotated.png"))
    print("Created drink_build_annotated.png")


def annotate_source_edit():
    """Annotate source_edit.png - highlight Dispense Product button for cleaning."""
    img = Image.open(os.path.join(IMG_DIR, "source_edit.png"))
    draw = ImageDraw.Draw(img)
    font = get_font(20)

    # Highlight DISPENSE PRODUCT button (y=936-1015, x=70-495)
    draw_rect_highlight(draw, 55, 930, 500, 1020, color="#FFaa00", width=5)
    draw_label(draw, 100, 1025, "Use for Cleaning", font, color="#FFaa00", bg_color="#FFFFFF")

    # Highlight BEGIN CALIBRATION button (y=816-895, x=70-495)
    draw_rect_highlight(draw, 55, 810, 500, 900, color="#44AAFF", width=4)
    draw_label(draw, 130, 785, "Advanced", small_font, color="#44AAFF", bg_color="#FFFFFF")

    img.save(os.path.join(IMG_DIR, "source_edit_annotated.png"))
    print("Created source_edit_annotated.png")

small_font = get_font(16)

if __name__ == "__main__":
    annotate_recipe_build()
    annotate_product_select()
    annotate_drink_build()
    annotate_source_edit()
    print("Done! All annotated screenshots created.")
