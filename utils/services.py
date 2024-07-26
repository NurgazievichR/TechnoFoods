import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def convert_image(img_path, WIDTH = 1280, HEIGHT = 720):
    with Image.open(img_path) as img:
        img = img.convert('RGB')
        width, height = img.size
        
        if width <= WIDTH and height <= HEIGHT:
            img.save(img_path, quality=85, optimize=True)
            return
        
        aspect_ratio = width / height
        if width > height:
            new_width = WIDTH
            new_height = int(WIDTH / aspect_ratio)
        else:
            new_height = HEIGHT
            new_width = int(HEIGHT * aspect_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(img_path, quality=85, optimize=True)
        print(f"Изображение изменено и сохранено как {img_path}")

def to_webp(image):
    img = Image.open(image)
    img_io = BytesIO()
    img.save(img_io, format='WEBP', quality=85)
    webp_filename = os.path.splitext(image.name)[0] + '.webp'
    image.save(webp_filename, ContentFile(img_io.getvalue()), save=False)