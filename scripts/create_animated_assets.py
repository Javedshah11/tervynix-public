from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS = ROOT / "screenshots"

SCREENSHOTS.mkdir(exist_ok=True)

WIDTH = 1280
HEIGHT = 720

BG = (10, 14, 22)
CARD = (20, 27, 39)
TEXT = (240, 244, 250)
MUTED = (150, 160, 175)
BLUE = (54, 170, 255)
GREEN = (70, 200, 130)
GRAY = (80, 90, 105)


# ---------------------------------------------------------
# FONTS
# ---------------------------------------------------------

def get_font(size, bold=False):
    fonts = []

    if bold:
        fonts = [
            "C:/Windows/Fonts/segoeuib.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
        ]
    else:
        fonts = [
            "C:/Windows/Fonts/segoeui.ttf",
            "C:/Windows/Fonts/arial.ttf",
        ]

    for font_path in fonts:
        if Path(font_path).exists():
            return ImageFont.truetype(font_path, size)

    return ImageFont.load_default()


TITLE = get_font(44, True)
HEADING = get_font(30, True)
NORMAL = get_font(21)
SMALL = get_font(18)


# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------

def new_frame():
    return Image.new("RGB", (WIDTH, HEIGHT), BG)


def centered_text(draw, text, y, font, color=TEXT):
    box = draw.textbbox((0, 0), text, font=font)
    text_width = box[2] - box[0]

    draw.text(
        ((WIDTH - text_width) / 2, y),
        text,
        font=font,
        fill=color,
    )


def resize_inside(image, max_width, max_height):
    ratio = min(
        max_width / image.width,
        max_height / image.height,
    )

    new_width = int(image.width * ratio)
    new_height = int(image.height * ratio)

    return image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS,
    )


def save_gif(frames, output, duration=120):
    if not frames:
        print(f"No frames for {output.name}")
        return

    frames[0].save(
        output,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=True,
    )

    print(f"Created: {output}")


# ---------------------------------------------------------
# PRODUCT DEMO GIF
# ---------------------------------------------------------

def make_product_slide(image_path, title, description):
    frame = new_frame()
    draw = ImageDraw.Draw(frame)

    centered_text(
        draw,
        "TERVYNIX",
        25,
        TITLE,
        BLUE,
    )

    centered_text(
        draw,
        title,
        82,
        HEADING,
    )

    centered_text(
        draw,
        description,
        125,
        SMALL,
        MUTED,
    )

    # Main screenshot card
    x1 = 60
    y1 = 180
    x2 = WIDTH - 60
    y2 = HEIGHT - 45

    draw.rounded_rectangle(
        (x1, y1, x2, y2),
        radius=24,
        fill=CARD,
    )

    image = Image.open(image_path).convert("RGB")

    image = resize_inside(
        image,
        x2 - x1 - 30,
        y2 - y1 - 30,
    )

    x = (WIDTH - image.width) // 2
    y = y1 + ((y2 - y1) - image.height) // 2

    frame.paste(image, (x, y))

    return frame


def create_product_demo():
    slides = [
        (
            "landing-page(1).png",
            "Landing Experience",
            "A modern developer-first experience.",
        ),
        (
            "dashboard(1).png",
            "Developer Dashboard",
            "Projects, runtime activity and developer tools.",
        ),
        (
            "projects.png",
            "Project Management",
            "Manage development projects from one workspace.",
        ),
        (
            "create-project.png",
            "Create Project",
            "Structured project creation inside Tervynix.",
        ),
    ]

    rendered = []

    for filename, title, description in slides:
        path = SCREENSHOTS / filename

        if not path.exists():
            print(f"Missing screenshot: {filename}")
            continue

        rendered.append(
            make_product_slide(
                path,
                title,
                description,
            )
        )

    if not rendered:
        print("No product screenshots found.")
        return

    frames = []

    for index, current in enumerate(rendered):
        next_frame = rendered[(index + 1) % len(rendered)]

        # Hold current slide
        for _ in range(14):
            frames.append(current.copy())

        # Smooth fade
        for step in range(1, 7):
            alpha = step / 7
            frames.append(
                Image.blend(
                    current,
                    next_frame,
                    alpha,
                )
            )

    save_gif(
        frames,
        SCREENSHOTS / "tervynix-demo.gif",
        120,
    )


# ---------------------------------------------------------
# WORKFLOW GIF
# ---------------------------------------------------------

def workflow_frame(active):
    frame = new_frame()
    draw = ImageDraw.Draw(frame)

    centered_text(
        draw,
        "Tervynix Development Workflow",
        65,
        TITLE,
    )

    centered_text(
        draw,
        "One connected developer environment",
        125,
        NORMAL,
        MUTED,
    )

    stages = [
        "CODE",
        "RUN",
        "DEBUG",
        "MANAGE",
        "COLLABORATE",
        "DEPLOY",
    ]

    margin = 50
    gap = 14

    total_available = WIDTH - margin * 2

    box_width = int(
        (
            total_available
            - gap * (len(stages) - 1)
        )
        / len(stages)
    )

    box_height = 120
    top = 300

    for i, stage in enumerate(stages):
        x1 = margin + i * (box_width + gap)
        y1 = top

        x2 = x1 + box_width
        y2 = y1 + box_height

        enabled = i <= active

        fill = (
            (28, 78, 115)
            if enabled
            else CARD
        )

        outline = BLUE if enabled else GRAY

        draw.rounded_rectangle(
            (x1, y1, x2, y2),
            radius=18,
            fill=fill,
            outline=outline,
            width=3,
        )

        font = SMALL if stage == "COLLABORATE" else NORMAL

        text_box = draw.textbbox(
            (0, 0),
            stage,
            font=font,
        )

        text_width = text_box[2] - text_box[0]

        draw.text(
            (
                x1 + (box_width - text_width) / 2,
                y1 + 46,
            ),
            stage,
            font=font,
            fill=TEXT if enabled else MUTED,
        )

        # arrow
        if i < len(stages) - 1:
            arrow_y = y1 + box_height // 2

            draw.line(
                (
                    x2 + 2,
                    arrow_y,
                    x2 + gap - 2,
                    arrow_y,
                ),
                fill=BLUE if i < active else GRAY,
                width=3,
            )

    centered_text(
        draw,
        "Code → Run → Debug → Manage → Collaborate → Deploy",
        530,
        HEADING,
        BLUE,
    )

    return frame


def create_workflow_demo():
    frames = []

    for stage in range(6):
        frame = workflow_frame(stage)

        for _ in range(8):
            frames.append(frame.copy())

    # hold final result
    for _ in range(15):
        frames.append(
            workflow_frame(5)
        )

    save_gif(
        frames,
        SCREENSHOTS / "workflow-demo.gif",
        120,
    )


# ---------------------------------------------------------
# ARCHITECTURE GIF
# ---------------------------------------------------------

def architecture_frame(level):
    frame = new_frame()
    draw = ImageDraw.Draw(frame)

    centered_text(
        draw,
        "Tervynix Architecture",
        25,
        TITLE,
    )

    centered_text(
        draw,
        "Current architecture + planned infrastructure",
        80,
        NORMAL,
        MUTED,
    )

    def box(
        x1,
        y1,
        x2,
        y2,
        title,
        subtitle="",
        active=True,
        planned=False,
    ):
        if planned:
            fill = (27, 31, 40)
            outline = GRAY
        elif active:
            fill = (27, 67, 94)
            outline = BLUE
        else:
            fill = CARD
            outline = GRAY

        draw.rounded_rectangle(
            (x1, y1, x2, y2),
            radius=18,
            fill=fill,
            outline=outline,
            width=3,
        )

        font = NORMAL

        title_box = draw.textbbox(
            (0, 0),
            title,
            font=font,
        )

        title_width = (
            title_box[2] - title_box[0]
        )

        draw.text(
            (
                x1
                + ((x2 - x1) - title_width) / 2,
                y1 + 19,
            ),
            title,
            font=font,
            fill=TEXT,
        )

        if subtitle:
            sub_box = draw.textbbox(
                (0, 0),
                subtitle,
                font=SMALL,
            )

            sub_width = (
                sub_box[2] - sub_box[0]
            )

            draw.text(
                (
                    x1
                    + ((x2 - x1) - sub_width) / 2,
                    y1 + 52,
                ),
                subtitle,
                font=SMALL,
                fill=MUTED,
            )

    # Root
    box(
        480,
        135,
        800,
        230,
        "TERVYNIX",
        "Developer Platform",
    )

    if level >= 1:
        draw.line(
            (640, 230, 640, 270),
            fill=BLUE,
            width=4,
        )

        draw.line(
            (330, 270, 950, 270),
            fill=BLUE,
            width=4,
        )

        draw.line(
            (330, 270, 330, 300),
            fill=BLUE,
            width=4,
        )

        draw.line(
            (950, 270, 950, 300),
            fill=BLUE,
            width=4,
        )

        box(
            150,
            300,
            510,
            400,
            "Web Application",
            "React + Next.js",
        )

        box(
            770,
            300,
            1130,
            400,
            "Backend API",
            "NestJS + Fastify",
        )

    if level >= 2:
        draw.line(
            (330, 400, 330, 445),
            fill=BLUE,
            width=4,
        )

        box(
            120,
            445,
            540,
            545,
            "Developer Workspace",
            "Monaco • Terminal • Runtime",
        )

        draw.line(
            (950, 400, 950, 445),
            fill=BLUE,
            width=4,
        )

        box(
            740,
            445,
            1160,
            545,
            "Domain Services",
            "Contracts + Application Logic",
        )

    if level >= 3:
        draw.line(
            (950, 545, 950, 585),
            fill=BLUE,
            width=4,
        )

        draw.line(
            (760, 585, 1140, 585),
            fill=BLUE,
            width=4,
        )

        box(
            670,
            610,
            850,
            695,
            "PostgreSQL",
            "Drizzle",
        )

        box(
            870,
            610,
            1050,
            695,
            "Redis",
            "Planned",
            planned=True,
        )

        box(
            1070,
            610,
            1250,
            695,
            "BullMQ",
            "Planned",
            planned=True,
        )

    if level >= 4:
        draw.line(
            (330, 545, 330, 585),
            fill=BLUE,
            width=4,
        )

        box(
            120,
            590,
            540,
            680,
            "Runtime Layer",
            "Processes • PTY • Ports",
        )

    if level >= 5:
        # small label because there is limited height
        draw.rounded_rectangle(
            (170, 685, 490, 715),
            radius=12,
            fill=(27, 31, 40),
            outline=GRAY,
            width=2,
        )

        text = "Rust Runtime Agent • Planned"

        box_text = draw.textbbox(
            (0, 0),
            text,
            font=SMALL,
        )

        text_width = box_text[2] - box_text[0]

        draw.text(
            (
                (WIDTH - text_width) / 2 - 310,
                690,
            ),
            text,
            font=SMALL,
            fill=MUTED,
        )

    return frame


def create_architecture_demo():
    frames = []

    for level in range(6):
        frame = architecture_frame(level)

        for _ in range(9):
            frames.append(frame.copy())

    for _ in range(14):
        frames.append(
            architecture_frame(5)
        )

    save_gif(
        frames,
        SCREENSHOTS / "architecture-demo.gif",
        120,
    )


# ---------------------------------------------------------
# START
# ---------------------------------------------------------

if __name__ == "__main__":
    print("")
    print("Creating Tervynix animated assets...")
    print("")

    create_product_demo()
    create_workflow_demo()
    create_architecture_demo()

    print("")
    print("Finished.")
    print("")
    print("Check your screenshots folder.")