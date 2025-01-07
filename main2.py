import os

def generate_items_wikitable(image_folder, output_file):
    if not os.path.exists(image_folder):
        raise Exception(f"The folder {image_folder} does not exist.")
    
    image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not image_files:
        raise Exception(f"No image files found in {image_folder}.")
    
    wikicode = '{| class="wikitable sortable"\n! Nome !! Uso !! Localização\n'
    
    for image_file in image_files:
        item_name = os.path.splitext(image_file)[0]
        wikicode += f'|-\n| [[File:{image_file}|50px]] {item_name} || TBD || TBD\n'
    
    wikicode += '|}'
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(wikicode)
    
    print(f"Wikitable successfully saved to {output_file}.")

image_folder_path = "./Items"
output_file_path = "items_wikitable.txt"

try:
    generate_items_wikitable(image_folder_path, output_file_path)
except Exception as e:
    print(f"An error occurred: {e}")
