import subprocess 
import xml.etree.ElementTree as ET 
from tabulate import tabulate 

def decompile_apk(apk_file):
    subprocess.run(["apktool", "d", "-f", apk_file]) #decompiling the apk file using apktool

def read_manifest(apk_file):
    tree = ET.parse(f"{apk_file[:-4]}/AndroidManifest.xml") #parsing the AndroidManifest.xml file
    root = tree.getroot()
    package_name = root.attrib.get("package") #getting the package name of the apk
    components = []
    for elem in root.iter():
        if elem.tag in ["activity", "service", "provider", "receiver"]:
            component = {}
            component["name"] = elem.attrib.get("{http://schemas.android.com/apk/res/android}name") #getting the name of the component
            component["type"] = elem.tag #getting the type of the component
            component["exported"] = elem.attrib.get("{http://schemas.android.com/apk/res/android}exported") #getting the exported status of the component
            if elem.find("intent-filter"):
                component["intent-filter"] = "Yes"
            else:
                component["intent-filter"] = "No"
            components.append(component)
    return package_name, sorted(components, key=lambda x: x["type"]) #sorting the components by type and returning package_name

def print_components(package_name,components):
    headers = ["Name", "Type", "Exported","Intent-Filter"] #headers of the tabular column
    table = [[component["name"], component["type"], component["exported"],component["intent-filter"]] for component in components] #table content
    print("Android Package Name:", package_name)
    print(tabulate(table, headers, tablefmt="fancy_grid", numalign="center")) #printing the tabular format of the table

if __name__ == "__main__":
    apk_file = input("Enter the path to the APK file: ") #input file path
    decompile_apk(apk_file) #decompiling the apk file
    package_name,components = read_manifest(apk_file) #getting the package_name and components from the AndroidManifest.xml file
    print_components(package_name,components) #printing the package_name and components
