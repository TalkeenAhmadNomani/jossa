import os

project_structure = {
    "config": ["config.yaml", "schema.yaml"],
    "src": {
        "api": ["__init__.py", "routes.py"],
        "core": ["__init__.py", "compare.py"],
        "services": ["__init__.py", "cutoff_service.py"],
        "data_access": ["__init__.py", "mongo_handler.py"],
        "logger": ["__init__.py", "logger.py"],
        "exception": ["__init__.py", "custom_exception.py"],
        "constants": ["__init__.py"],
        "utils": ["__init__.py"],
    }
}

base_files = [
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "README.md"
]

def create_file(path):
    with open(path, "w") as f:
        pass

def create_structure(base_path="."):
    for folder, content in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        if isinstance(content, list):
            for file in content:
                create_file(os.path.join(folder_path, file))
        elif isinstance(content, dict):
            for subfolder, files in content.items():
                subfolder_path = os.path.join(folder_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                for file in files:
                    create_file(os.path.join(subfolder_path, file))

    for file in base_files:
        create_file(os.path.join(base_path, file))

    print("✅ Project template created successfully!")

if __name__ == "__main__":
    create_structure()
