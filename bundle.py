import os
import pandas
import shutil


def bundle():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    cwd = os.getcwd()
    files = [f for f in os.listdir("./BundleFiles") if os.path.isfile("./BundleFiles/" + f) if ".zip" in f]

    data = pandas.read_csv("ssa_modules.csv")
    module_obj = data.to_dict(orient="records")
    bundle_folder = "./BundleFiles/"

    for file in files:
        for module in module_obj:
            if module["Module"] in file:
                formatted_name = module["Proper Name"]
                print(formatted_name)
                if module["Active"] == "Yes":
                    try:
                        os.replace(bundle_folder + file,
                                   bundle_folder + module["Style"] + "/" + formatted_name + ".zip")
                    except FileNotFoundError:
                        os.makedirs(bundle_folder + module["Style"])
                        os.replace(bundle_folder + file,
                                   bundle_folder + module["Style"] + "/" + formatted_name + ".zip")
                    break
    os.chdir(cwd + "/BundleFiles")
    folders = [folder for folder in os.listdir(os.getcwd()) if os.path.isdir(folder)]

    for folder in folders:
        shutil.make_archive(folder, "zip", folder)
        shutil.rmtree(folder)
