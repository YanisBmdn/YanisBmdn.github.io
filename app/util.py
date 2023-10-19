import os
from PIL import Image

def resize_image(image_path, max_size=4 * 1024 * 1024):  # max_size en octets
    img_size = os.path.getsize(image_path)  # en octets

    if img_size <= max_size:
        return "Taille OK"

    with Image.open(image_path) as img:
        aspect_ratio = img.width / img.height
        scaling_factor = (max_size / img_size) ** 0.5
        new_width = int(img.width * scaling_factor)
        new_height = int(new_width / aspect_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)
        
        img.save(image_path, "PNG")

# Boucle pour traiter toutes les images
for subdir, _, files in os.walk("./app/static/scans"):
    print(f"Parcours du sous-répertoire: {subdir}")  # Debug print
    for file in files:
        print(f"Fichier trouvé: {file}")  # Debug print
        if file.endswith('.png'):
            full_path = os.path.join(subdir, file)
            result = resize_image(full_path)
            print(f"{file}: {result}")

