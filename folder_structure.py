import os
import shutil
import zipfile
import subprocess

# Define file paths
src_zip = "src.zip"         # Replace with actual path if needed
pipeline_zip = "pipeline.zip" # Replace with actual path if needed

# Define extraction directories
src_extracted = "src"
pipeline_extracted = "pipeline"

# Function to unzip a file
def unzip_file(zip_path, extract_to):
    if os.path.exists(zip_path):
        os.makedirs(extract_to, exist_ok=True)
        shutil.unpack_archive(zip_path, extract_to, 'zip')
        print(f"Extracted {zip_path} to {extract_to}")
    else:
        print(f"Zip file {zip_path} not found!")

# Step 1: Unzip src and pipeline folders
unzip_file(src_zip, src_extracted)
unzip_file(pipeline_zip, pipeline_extracted)

# Step 2: Install requirements.txt if present
requirements_path = "requirements_pipeline.txt"
if os.path.exists(requirements_path):
    subprocess.run(["pip", "install", "-r", requirements_path], check=True)
    print("Installed dependencies from requirements.txt")
else:
    print("requirements.txt not found!")

# Step 3: Create models directory inside the extracted pipeline folder
models_path = os.path.join(pipeline_extracted, "models")
os.makedirs(models_path, exist_ok=True)
print(f"Created folder: {models_path}")

# Step 4: Remove zip files
for zip_file in [src_zip, pipeline_zip]:
    if os.path.exists(zip_file):
        os.remove(zip_file)
        print(f"Removed {zip_file}")

print("Setup completed successfully!")
