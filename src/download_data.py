import os
import subprocess

def download_dataset():
    print("Descargando dataset desde Kaggle...")
    # Requiere tener configurado ~/.kaggle/kaggle.json
    dataset_name = "usuario/nombre-del-dataset" 
    dest_path = "../data/raw"
    
    os.makedirs(dest_path, exist_ok=True)
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name, "-p", dest_path, "--unzip"])
    print("Descarga completada.")

if __name__ == "__main__":
    download_dataset()
