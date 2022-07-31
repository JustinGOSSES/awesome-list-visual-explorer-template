print("testing if this python script ran by a print statement")

#import markdown
import re
import os
import yaml

# Load YAML data from the _config.yml file
with open('../../_config.yml') as file:
    try:
        config = yaml.safe_load(file)   
        print(config)
    except yaml.YAMLError as exc:
        print(exc)

url_of_readme = config["raw_link_to_awesome_list_readme_to_parse"]
name_of_awesome_list = config["filename_to_save_awesome_list_readme"]
name_of_code_platform_searched = config["name_of_code_platform_searched"]

exclude_these_usernames = config["exclude_these_usernames"]

# Get the current working
# directory (CWD)
cwd = os.getcwd()
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

## hardcoded as it is relative to this file
path_back_to__explore = "../"

print("path_back_to__explore = ",path_back_to__explore)
print("name_of_awesome_list = ",name_of_awesome_list)

path_to_markdown_test_file = os.path.join(path_back_to__explore ,name_of_awesome_list)


#### Open and read the file at the path established above
f = open(path_to_markdown_test_file, 'r') 
text = f.read() 

#### Placing a copy elsewhere in case it gets messed up
path_to_markdown_test_file_copied_for_safe_keeping = os.path.join(path_back_to__explore,"previous_versions_for_safe_keeping",name_of_awesome_list)

with open(path_to_markdown_test_file_copied_for_safe_keeping, 'a+') as safe_copy:
    safe_copy.write(text)
    safe_copy.close()

#### Commenting out this line to print the entire markdown for now but it might be useful later!
# print("text is:",text)

#### Initially this will just work with things on the public github.com. 
#### However, eventually, it would be nice if it would work for any code platform. 
#### To plan for this future, we'll add the variable below

arrayOfAllCodePlatforms = ["https://github.com","https://gitlab.com","https://bitbucket.org/"]


#### FOR NOW HOWEVER, we'll just use the hardcoded github.com as shown below

#### Finds all the strings that match the expression below looking for https://github.com/ and then some characters then / then characters then / before end of word.
found_in_search = re.findall(r'https://github.com/\w+/\w+',text,re.IGNORECASE)

#### Printing for testing right now but will likely remove or comment out or make only print in verbose mode later?
#print("found_in_search",found_in_search,"which is ",len(found_in_search)," items.")
#print(type(found_in_search))

#### Take out duplicates
found_in_search_no_duplicates = list(dict.fromkeys(found_in_search))
#print(len(found_in_search_no_duplicates))

def takeOutAnyWithExcludedUserNames(exclude_these_usernames, found_in_search_no_duplicates):
    new_list = []
    for name in found_in_search_no_duplicates:
        for bannedName in exclude_these_usernames:
            if bannedName not in name:
                new_list.append(name)
            else:
                print("found an excluded username string",bannedName," in the URL for ",name, "and will therefore exclude it. The usernames to exclude are defined in _config.yml")
    return new_list

found_in_search_no_duplicates = takeOutAnyWithExcludedUserNames(exclude_these_usernames, found_in_search_no_duplicates)

print("found ",len(found_in_search_no_duplicates), "different URLs to github of the form https://github.com/ ... / ... / in the markdown file",name_of_awesome_list)
print("They are:",found_in_search_no_duplicates)

# url_of_readme = "https://raw.githubusercontent.com/softwareunderground/awesome-open-geoscience/main/README.md"
# name_of_awesome_list = "awesome-open-geoscience"
# name_of_code_platform_searched = "https://github.com"

def makeDictFromList(found_in_search_no_duplicates,url_of_readme,name_of_awesome_list,name_of_code_platform_searched):
    array_for_objects = []
    print("length of found_in_search_no_duplicates",len(found_in_search_no_duplicates))
    
    for item in found_in_search_no_duplicates:
        tempKeyValues = {"repoURL":"","url_of_readme":url_of_readme,"name_of_awesome_list":name_of_awesome_list,"name_of_code_platform_searched":name_of_code_platform_searched}
        tempKeyValues["repoURL"] = item
        array_for_objects.append(tempKeyValues)
    return array_for_objects

found_in_search_no_duplicates_final = makeDictFromList(found_in_search_no_duplicates,url_of_readme,name_of_awesome_list,name_of_code_platform_searched)

#### Write python lists to JSON
import json
jsonStr = json.dumps(found_in_search_no_duplicates_final)
#print(jsonStr)


#### Create path to output file location
output_file = "awesome-open-geoscience_github-repos.json"
path_to_output_file = os.path.join(path_back_to__explore,output_file)



#### Open file and write string to it and the close.
jsonFile = open(path_to_output_file, "w")
jsonFile.write(jsonStr)
jsonFile.close()

#### Function to strip out https://github.com/
#### Function to get the orgs and/or usernames as a list with a count of how many repos from each orgname/username
#### Function to get results in form username/reponame

#### Load inputs_lists.json
path_to_input_lists_json = "../input_lists.json"
with open(path_to_input_lists_json) as file:
    input_lists = json.load(file)


#### Placing a copy elsewhere in case it gets messed up
path_to_input_lists_json_file_copied_for_safe_keeping = os.path.join("../","previous_versions_for_safe_keeping","input_lists.json")

with open(path_to_input_lists_json_file_copied_for_safe_keeping, 'a+') as safe_copy_inputs_list:
    safe_copy_inputs_list.write(json.dumps(input_lists))
    safe_copy_inputs_list.close()


# input_lists_f = open(path_to_input_lists_json,)
# input_lists = json.loads(input_lists_f)
print("input_lists = ",input_lists)


#### Add username/reponame to inputs_lists.json if not already there...
#### load inputs_lists.json
#### add item if not there

def add_any_new_repos_to_input_lists(found_in_search_no_duplicates_final,input_lists):
    new_code_projects = []
    for item in found_in_search_no_duplicates_final:
        #print('item',item)
        item_without_github = item["repoURL"].replace("https://github.com/","")
        #print("thest this line here")
        if item_without_github in input_lists["repos"]:
            print("the item",item_without_github," was found in the list already")
        else:
            new_code_projects.append(item_without_github)
    print("new items being added to input_lists are:",new_code_projects)
    input_lists["repos"].extend(new_code_projects)
    return input_lists

appended_input_lists_string = add_any_new_repos_to_input_lists(found_in_search_no_duplicates_final,input_lists)
print("appended_input_lists_string = ",appended_input_lists_string)

#### save and overwrite
# input_lists_f = open(path_to_input_lists_json, "w")
# appended_input_lists_string_dumped = json.dumps(appended_input_lists_string)
path_to_input_lists_json = "../input_lists.json"
with open(path_to_input_lists_json, 'w') as file:
    json.dump(appended_input_lists_string,file)
    # file.close()


# input_lists_f.write(appended_input_lists_string_dumped)
# input_lists_f.close()

print("new input_lists = ",appended_input_lists_string)
