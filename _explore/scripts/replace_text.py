import os
import in_place
import re
import os
import yaml


path_back_to_root_from_scripts_folder = "../../"

config_file_name = "_config.yml"

path_to_config_file = os.path.join(path_back_to_root_from_scripts_folder,config_file_name )

# Load YAML data from the _config.yml file
with open(path_to_config_file) as file:
    try:
        config = yaml.safe_load(file)   
        print(config)
    except yaml.YAMLError as exc:
        print(exc)

#### In the _config.yml file, there are these parts
# replace_all_instances_of_this_string_with_string_below_in_config: open_geosciene_code_projects_viz
# replaced_all_instances_of_string_above_in_config_with: awesome-list-visual-explorer-template
# files_to_not_replace_string_in: 
#   - _config.yml
#   - README.md

#### Below we'll call the key:value pairs from the _config.yml file that is in root of this repo
replace_all_instances_of_this_string_with_string_below_in_config = config["replace_all_instances_of_this_string_with_string_below_in_config"]
replaced_all_instances_of_string_above_in_config_with = config["replaced_all_instances_of_string_above_in_config_with"]
files_to_not_replace_string_in = config["files_to_not_replace_string_in"]

# also_replace="Awesome-Open-Geoscience"

paths_to_replace_from_root_of_repo = ["category","_includes","_posts","_site","_site/category","_site/assets/","_site/assets/images/","_site/assets/images/logos/","site/assets/images/logos/Category_LLNLSoftwarePortal_files/","_site/assets/images/logos/","assets/images/logos/Category_LLNLSoftwarePortal_files/","_site/assets/images/logos/","assets/images/logos/","js","css","css/_site"]


def make_paths_to_replace_from_root_of_repo_relative_to_this_file(paths_to_replace_from_root_of_repo,path_back_to_root_from_scripts_folder):
    new_list = []
    for i in range(len(paths_to_replace_from_root_of_repo)):
        paths_to_replace_from_root_of_repo[i] = os.path.join(path_back_to_root_from_scripts_folder, paths_to_replace_from_root_of_repo[i])
    return paths_to_replace_from_root_of_repo

#### 
paths_to_directory_to_searc_for_string_to_replace = make_paths_to_replace_from_root_of_repo_relative_to_this_file(paths_to_replace_from_root_of_repo,path_back_to_root_from_scripts_folder)
root_level_index_path = "../../index.html"

# Get the current working
# directory (CWD)
cwd = os.getcwd()
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)


def replace(file_path, old_text, new_text):
    with in_place.InPlace(file_path) as f:
        for line in f:
            f.write(line.replace(old_text, new_text))

def replace_text_in_these_files(paths_to_directory_to_searc_for_string_to_replace,files_to_not_replace_string_in,replace_all_instances_of_this_string_with_string_below_in_config,replaced_all_instances_of_string_above_in_config_with):
    for directory in paths_to_directory_to_searc_for_string_to_replace:
        print("now working in directory", directory)
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file in files_to_not_replace_string_in:
                    print("skipping file: ",file)
                else:
                    print("replacing text in file: ",file)
                    path_to_file = os.path.join(root, file)
                    try:
                        replace(path_to_file, replace_all_instances_of_this_string_with_string_below_in_config, replaced_all_instances_of_string_above_in_config_with)
                    except:
                        print("error in replace_text_in_these_files: ",path_to_file)


replace_text_in_these_files(paths_to_directory_to_searc_for_string_to_replace,files_to_not_replace_string_in,replace_all_instances_of_this_string_with_string_below_in_config,replaced_all_instances_of_string_above_in_config_with)


##### Calling two files explicitly here as they are either in top folder of the repository and I don't want to call anything 
##### except them as in the case of index.html or
##### the seemed to sometimes fail to be rewritten for some reason as in the case of category_info.json
print("replacing text in index.html next")
replace(root_level_index_path, replace_all_instances_of_this_string_with_string_below_in_config,replaced_all_instances_of_string_above_in_config_with)
print("just run command replacing text in index.html")

##### replace repo name in ../../_site/category/category_info.json
print("replacing text in ../../_site/category/category_info.json")
replace("../../_site/category/category_info.json",replace_all_instances_of_this_string_with_string_below_in_config,replaced_all_instances_of_string_above_in_config_with)

