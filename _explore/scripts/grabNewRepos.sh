#!/bin/bash

#### This is a test script so we don't actually run MASTER.sh in the same folder while testing GitHubActions

echo Hello World, we got into the test.sh scripts

#### use curl to call one or more markdown files and put them in a place to be used later
#### these file URLs should be ideally be pulled from the central place any changes are made
#### ..which is: _config.yml https://github.com/softwareunderground/open_geosciene_code_projects_viz/blob/main/_config.yml

export PATH_TO_CONFIG="../../_config.yml"

arr=($(cat ../../_config.yml | grep "raw_link_to_awesome_list_readme_to_parse:"))
raw_link_to_awesome_list_readme_to_parse=${arr[1]}
echo the link to the README that will be parsed is $raw_link_to_awesome_list_readme_to_parse

arr=($(cat ../../_config.yml | grep "path_to_directory_to_save_awesome_list_readme:"))
path_to_directory_to_save_awesome_list_readme=${arr[1]}
echo This directory where the file should be saved to is $path_to_directory_to_save_awesome_list_readme

arr=($(cat ../../_config.yml | grep "filename_to_save_awesome_list_readme:"))
filename_to_save_awesome_list_readme=${arr[1]}
echo The filename to save the README under is $filename_to_save_awesome_list_readme

#### If ___ True, the inputs_lists.json will be wiped of existing orgs,users, and repos.
arr=($(cat ../../_config.yml | grep "wipe_existing_content_from_input_lists_json:"))
wipe_existing_content_from_input_lists_json=${arr[1]}
echo value of wipe_existing_content_from_input_lists_json is $wipe_existing_content_from_input_lists_json

if [ $wipe_existing_content_from_input_lists_json = True ]; then
    echo "wiping existing content from input_lists.json"
    rm ../input_lists.json
    cp ../input_lists_blankStarter.json ../input_lists.json
    echo "got just past line that runs cp ../input_lists_blankStarter.json ../input_lists.json" 
fi

curl $raw_link_to_awesome_list_readme_to_parse -o ../$filename_to_save_awesome_list_readme

#### Doing this as pyyaml doesnt' work correctly if installed via requirements.txt sometimes
pip install pyyaml

# Basic script run procedure
function runScript() {
    echo "Run - $1"
    python -u $1
    ret=$?
    # errorCheck "$1"
}

# RUN THIS FIRST
echo about to run python script parse_markdown_for_github_links.py
runScript parse_markdown_for_github_links.py
echo ran script parse_markdown_for_github_links.py
