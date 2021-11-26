# awsome-list-visual-explorer-template

## Is this the awsome-list-visual-explorer-template TEMPLATE or a repository made from the template?
<i>NOTE: You may be looking at a repository made with the template https://github.com/JustinGOSSES/awsome-list-visual-explorer-template or you may be looking at the actual code repository https://github.com/JustinGOSSES/awsome-list-visual-explorer-template. If the name of the code repository is not <b>awsome-list-visual-explorer-template</b>, you are looking at a code repository made with the template.</i>

## Description of this code repository if not the template:
- Repository Name: 
- Repository Authors: 
- Purpose:
- Link To Awesome List Parsed In This Code Project:
- Link to Live Website: <b><a href="">none yet</a></b>
- Last Ran in Full On: YYYY-MM-DD

### Contributing to this repository if not the template
------------ INFORMATION GOES HERE ------------

<i>----- REST OF INFORMATION ABOUT THIS SPECIFIC CODE REPOSITORY IF NOT THE TEMPLATE ITSELF GOES HERE ------</i>

## What Does the awsome-list-visual-explorer-template Template Build?

<b><i>The goal of this project is to surface the characteristics, trends, connections, relationships, etc. that can describe the implicit community of developers and repositories in an Awesome List and make them available in a visual form to the same people who get value from an Awesome List in list form.</i></b>

The template builds a website with a variety of visualizations, usually deployed as a GitHub pages page.

The idea behind its creation is by being able to quickly understand visually the trends and relationships in a community of related code repositories, it will nudge developers who are a part of that implicit community how think about those projects, where they might contribute, and who is working on the things they are also interested in. All this information has technically long been available, but it is usually slow and difficult to surface so most people don't bother. 

## Key Pages That The Template Builds
##### Front Page
This is a catalog of all the code repositories. The organizational structure is based on topics tags on the github repositories themselves and categories that organize those tags set in `category/category_info.json`. 
##### About Page
This is an about page for the template itself. 
##### Explore Page
A series of visualizations that give a high level overview of how the community of Awesome List GitHub code repositories has changed over time, including:
- groupings of organizations that contribute many repos
- contributions over time
- stars over time
- ratios of open and closed issues and pull requests
- repository topic word map
- repository license breakdown

##### Dependencies Page
An interactive graph network of dependencies and organizational connections between code repositories.

##### Popular Repositories Page
Visualization of the most popular repositories including:
- organizations as bubbles scaled by the number of repositories they've created
- line chart of count of repositories created over time
- number of stars over time of the top 10 most popular repositories
- activity over time of the top 10 most popular repositories
- licenses of the most popular repositories

## Examples Webpages Exploring An Awesome List Built With This Template

- https://JustinGOSSES.github.io/awsome-list-visual-explorer-template/
- https://softwareunderground.github.io/open_geosciene_code_projects_viz/
- https://github.com/JustinGOSSES/Awesome-Earth-Artificial-Intelligence-visual-explorer

### Prior Work
<i>What is it based off of?</i>
This site was created by taking a fork of the <a href="https://github.com/LLNL/llnl.github.io">Lawrence Livermore National Laboratory's open source software catalog</a> and changing <a href="https://github.com/softwareunderground/open_geosciene_code_projects_viz">a bunch of stuff</a> to make it useful for visualizing Software Underground's Awesome-Open-Geoscience list.

It was initially created as part of the Transform 21' hackathon put on by The Software Underground or SWUNG.

Original Project Plan: https://github.com/softwareunderground/transform-2021-hackathon/discussions/14

The project plan has now been moved to issues: https://github.com/softwareunderground/open_geosciene_code_projects_viz/projects/1

The code is still largely that of the original  <a href="https://github.com/LLNL/llnl.github.io">Lawrence Livermore National Laboratory's open source software catalog</a>.

### Completed Changes From Original Project & Possible Future Changes Roadmap 
https://github.com/softwareunderground/open_geosciene_code_projects_viz/blob/main/changes_needed.md

### Presentations on What's trying to be accomplished with this repository

SLIDES PRESENTED DURING HACKATHON: https://observablehq.com/@justingosses/more-visible-connections-between-projects-can-nudge-devel 

MEDIUM STORY: https://justingosses.medium.com/beyond-awesome-lists-3ccb074f7859


## Overview of How awsome-list-visual-explorer-template Template Works
At a very high level, there a variety of bash and Python scripts that grab github repository URLs from an Awesome List README location you supply as configuration, get details about those repositories from the GitHub API, and then rebuild the webpages with that information and information from a configuration file. 

#### A step-by-step high level overview of how the template is used:
- Developer clicks on green "Use This Template" button on the <a href="https://github.com/JustinGOSSES/awsome-list-visual-explorer-template">awsome-list-visual-explorer-template repository page</a>. This builds them a clone repository, not a fork!. 
- They change information in the _config.yml file that sits at the top of the repository directory to reflect their name of the repositry, the location of the Awesome-list they want to build from, and other details. 
- They install ruby and jekyl following the full "installation" instructions below. 
- They change directory into `_explore/scripts` and follow the README there to install the python dependencies in an virtualenv. 
- They run the bash script in the `_explore/scripts` directory called `grabNewRepos.sh`. This grabs github URLs from the README whose address was added to the `_config.yml` file and puts them in the `_explore/input_lists.json` file. 
- They run the bash script in the `_explore/scripts` directory called `BUILD.sh`. This is the main build script for the repository and runs a bunch of python files in the scripts folder and also calls the GitHub API to get information like stars and contributors from each GitHub code repository listed in `input_lists.json`. It also replaces the name of the repository used in the template with the name of the new repository listed in `_config.yml`.
- Lastly, they will run `bundle exec jekyll serve` to start up a server that will show a local version of the webpage at  http://127.0.0.1:4000/nameOfYourRepositoryThatWasSetInConfigYamlFile.


## Prerequisites

Before you begin, make sure you have working installs of Git, Ruby, and Bundler <https://bundler.io/> You will need these tools for development.

## Getting Started

First, use the template repository as your template. Got to https://github.com/JustinGOSSES/awsome-list-visual-explorer-template/ and click the big green button that say "Use This Template". 

You'll probably want to give it a name that somewhat aligns with the Awesome List repository that you'll use for your data.

Next, to work locally, clone your repository:

```
git clone https://github.com/JustinGOSSES/awsome-list-visual-explorer-template/   <--- or your name of the repository!
```

Make sure you are in the directory you just created by running `cd nameOfRepositoryHere` Then you can use `bundler` to install the Ruby dependencies (see the [Jekyll installation docs](https://jekyllrb.com/docs/installation/) for step-by-step guides to setting this up):

```
bundle install
```

Running this will install everything in your Gemfile (including Jekyll). 

After all the data is updated and the pages are built fresh, you'll want to the development web server with:

```
bundle exec jekyll serve
```

Followed by opening <http://127.0.0.1:4000/open_geosciene_code_projects_viz/> in a web browser.

You probably want to visualize details of an Awesome list specific to you though, so we'll get to that now. 

Go to the `_config.yml` file and change some of the details. The important ones to change are:
- name
- authour
- title
- description
- shortname
- baseurl <=== This should be your repository name for GitHhub Pages deployment to work!!!
- raw_link_to_awesome_list_readme_to_parse
- filename_to_save_awesome_list_readme
- twitter.username
- repository <=== This should be your username/repositoryName!!!
- replaced_all_instances_of_string_above_in_config_with <== This should be the name of your repository again. Where awsome-list-visual-explorer-template is found across HTML, JavaScript, and CSS files, it will be replaed with this string.

The python scripts call the GitHub API, which means the environment you run your code in requires a GitHub API Token as an environmental variable. The token only needs READ access to public repositories. You can read about how to get a GitHub API token <a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">here</a> and <a href="https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api">here</a>. If running locally in a terminal, you probably want to get it into your environment by running something like `export GITHUB_API_TOKEN digitsOfYourTokenGoHere`. If running in the GitHubActions, the `.github/workflows/update.yml` file already has you covered. 

Next, we'll work with the scripts that pull in data and rebuild the pages. 

Change directory to `_explore/scripts` and read the README there for instructions on how to start a virtual environment and install the dependencies in requirements.txt. 

Once you've done that, you can proceed to run the first bash script to gather GitHub code repository URLs from the Awesome List URL you added to `_config.yml`. This done by running `bash grabNewRepos.sh`.

Next step is to run `bash BUILD.sh`. This is the main build script for the repository and runs a bunch of python files in the scripts folder and also calls the GitHub API to get information like stars and contributors from each GitHub code repository listed in `input_lists.json`. It also replaces the name of the repository used in the template with the name of the new repository listed in `_config.yml`.

<i>NOTE: the build.sh script does many calls to the GitHub API, which means it can sometimes take 15-30 minutes to complete its full run!</i>

Lastly, change directory back to the root of the directory by running `cd ../../` and then run `bundle exec jekyll serve` to start up a server that will show a local version of the webpage at  http://127.0.0.1:4000/nameOfYourRepositoryThatWasSetInConfigYamlFile.

#### GithubActions 
The steps to gather data from the Awesome List defined in the _config.yml file and rebuild the page is also built into a GitHubActions configuration file at `.github/workflows/update.yml`. 

Currently, this is set to only run on manual trigger or what's called workflow dispatch. Once changes are stabled, the GitHubActions scripts could be used to pull in new data from the Awesome list on some predetermined timing or upon pull request to keep the page visualizations up to date with the Awesome List it pulls from. 

#### Tips

The gems in your sourcefile get updated frequently. It is a good idea to occasionally run `bundle update` from within your project's root directory to make sure the software on your computer is up to date.

Sometimes there can be dependency conflicts if your local version of Ruby is different from this repo or github pages deployment settings. You can find the version number of each of GitHub Page's current dependency's [here](https://pages.github.com/versions/). You can often avoid dependency issues if you use the same versions, including for Ruby. 

As an example, the default version of Ruby used to deploy GitHub Pages on github.com as of 2021-04-08 was Ruby	2.7.1. If you tried running Ruby version 3.0.0 locally on macOS, you'll need to do some extra steps to correctly install the dependencies for this repository. You'd need to run `bundle add webrick` as it is no longer a prepackaged dependency with Ruby in 3.0.0. You may also need to run `gem install eventmachine -- --with-openssl-dir=/usr/local/opt/openssl@1.1` as MacOS >10.14 doesn't use openssl from the same path as is still assumed to be in by eventmachine.

#### How to get additional code repositories tracked not in the awesome list in the _config.yml file?
------------ IN PROGESS ------------


## Contributing to the Template
------------ IN PROGESS ------------


## How to get changes from the template after your repository is already built?
------------ IN PROGESS ------------

