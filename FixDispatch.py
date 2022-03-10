import os
import zipfile
import pandas
import shutil

# Extract zip files in Fix_Dispatch
def unzip(file, folder):
    with zipfile.ZipFile(file, "r") as zipref:
        zipref.extractall(folder)


def apply_fix():
    os.chdir("./Fix_Dispatch")
    cwd = (os.getcwd() + "/").replace("\\", "/")
    dispatch_location = (cwd + "dispatch.html")
    styles = {
        "applied_interactive_modules": "Applied Interactive",
        "gamified_interactive": "Gamified",
        "mini_game": "Mini Game"
    }
    style_files = [f for f in os.listdir(cwd) if os.path.isfile(f) and ".zip" in f]
    data = pandas.read_csv("../ssa_modules.csv")
    module_obj = data.to_dict(orient="records")
    for file in style_files:
        for style, value in styles.items():
            if style in file:
                print(value)
                unzip(file, value)
                break

    folders = [folder for folder in os.listdir(cwd) if os.path.isdir(folder)]

    for folder in folders:
        files = [f for f in os.listdir(cwd + folder) if ".zip" in f]
        os.chdir(cwd + folder)
        print(f"\n Fixing {folder} Modules")
        print("-" * 50)
        for file in files:
            file_directory = f"{cwd}{folder}/{file}"
            for module in module_obj:
                if module["Module"] in file:
                    formatted_name = module["Proper Name"]
                    print(formatted_name)
                    break
            unzip(file, formatted_name)
            temp_path = f"{cwd}{folder}/{formatted_name}"
            bad_dispatch = f"{cwd}{folder}/{formatted_name}/dispatch.html"
            os.remove(bad_dispatch)
            shutil.copy(dispatch_location, temp_path)
            os.remove(file)
            shutil.make_archive(temp_path, "zip", temp_path)
            shutil.rmtree(temp_path)
        os.chdir(cwd)
        shutil.make_archive(cwd + folder, "zip", cwd + folder)
        shutil.rmtree(cwd + folder)


