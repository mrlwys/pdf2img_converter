from pdf2image import convert_from_path
import os
import sys
import platform
import subprocess
import shutil

# Set Poppler path based on OS
if platform.system() == "Windows":
    poppler_path = os.path.join(os.getcwd(), "poppler", "poppler-24.08.0", "Library", "bin")
elif platform.system() in ["Linux", "Darwin"]:  # macOS uses Darwin
    poppler_path = os.path.join(os.getcwd(), "poppler", "poppler-24.08.0", "installed", "bin")
else:
    print("Unsupported system")
    sys.exit(1)

# Check if Poppler is installed
if not os.path.exists(poppler_path):
    print("Poppler not found. Installing automatically...")
    if platform.system() == "Windows":
        subprocess.run(["install_poppler.bat"], shell=True)
    else:
        subprocess.run(["bash", "install_poppler.sh"], check=True)

# Directories
pdf_folder = "pdfs"
image_folder = "images"  # Fixed variable name (was 'pasta_images')
done_folder = "done"
os.makedirs(done_folder, exist_ok=True)  # Create 'done' folder

# Create image folder if not exists
os.makedirs(image_folder, exist_ok=True)  # Fixed from 'pasta_imagens'

# List all PDFs
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

# Convert each PDF
for pdf in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf)
    print(f"Converting {pdf}...")

    # Convert PDF to images
    images = convert_from_path(pdf_path, poppler_path=poppler_path)

    # Save images
    base_name = os.path.splitext(pdf)[0]
    output_folder = os.path.join(image_folder, base_name)
    os.makedirs(output_folder, exist_ok=True)

    for i, img in enumerate(images):
        img_path = os.path.join(output_folder, f"{base_name}_page_{i+1}.png")
        img.save(img_path, "PNG")

    # Move PDF to 'done'
    src_pdf = os.path.join(pdf_folder, pdf)
    dest_pdf = os.path.join(done_folder, pdf)
    
    if os.path.exists(dest_pdf):
        os.remove(dest_pdf)
    
    shutil.move(src_pdf, dest_pdf)
    print(f"File {pdf} moved to {done_folder}/")

    print(f"PDF '{pdf}' converted and saved to '{output_folder}'.")

print("🔥 Conversion complete!")