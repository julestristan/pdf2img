import os
from pdf2image import convert_from_path

# Input PDF and Output Images
input_dir = './pdf'
output_dir = './images'

# Create output directory if needed
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Folder '{output_dir}' created!")

# Convert PDF to images
images = convert_from_path(os.path.join(input_dir,"tickets-USA2026.pdf"), dpi=200)

# Save imaages
for i, image in enumerate(images):
    file_path = os.path.join(output_dir, f'ticket_page_{i+1}.png')
    image.save(file_path, 'PNG')