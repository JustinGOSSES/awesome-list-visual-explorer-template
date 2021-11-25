# awsome-list-visual-explorer-template

## DESCRIPTION of the awsome-list-visual-explorer-template TEMPLATE
<i>NOTE: You may be looking at a repository made with the template https://github.com/JustinGOSSES/awsome-list-visual-explorer-template or you may be looking at the actual code repository https://github.com/JustinGOSSES/awsome-list-visual-explorer-template. If the name of the code repository is not <b>awsome-list-visual-explorer-template</b>, you are looking at a code repository made with the template.</i>


## What Does the Template Build?

The template builds a website with a variety of visualizations, usually deployed as a GitHub pages page, that attempts to offer new ways to understand the implicit community innate to any Awesome List of another type of collection of code repositories. 

It visualizes characteristics of communities of code repositories. 
- Rate of new code repositories over time?
- How does the rate of stars vary over time for invidual repositories and groups of them?
- What licenses does the commmunity prefer?
- What dependencies are shared across code projects?
- What languages are most used across code projects?
- What user or org contributes to the most projects or connect project groups?
- etc. 

The idea is by being able to quickly understand trends and relationships in a community of related code repositories, it will nudge developers who are a part of that implicit community how think about those projects, where they might contribute, and who is working on the things they are also interested in. All this information has long technically been available, but it is usually slow and difficult to surface so most people don't bother. 

<b><i>The goal of this project is to surface those characteristics, trends, connections, relationships, etc. about the implicit community of developers and repositories in an Awesome List and make them available to the same people who get value from an Awesome List in list form.</i></b>

## Overview of How awsome-list-visual-explorer-template Template Works
At a very high level, there a variety of bash and Python scripts that grab github repository URLs from an Awesome List README location you supply as configuration, get details about those repositories from the GitHub API, and then rebuild the webpages with that information and information from a configuration file. 

#### A step-by-step high level overview is:
- Developer clicks on green "Use This Template" button on the <a href="https://github.com/JustinGOSSES/awsome-list-visual-explorer-template">awsome-list-visual-explorer-template repository page</a>. This builds them a clone repository, not a fork!. 
- They change information in the _config.yml file that sits at the top of the repository directory to reflect their name of the repositry, the location of the Awesome-list they want to build from, and other details. 
- They install ruby and jekyl following the full "installation" instructions below. 
- They change directory into `_explore/scripts` and follow the README there to install the python dependencies in an virtualenv. 
- They run the bash script in the `_explore/scripts` directory called `grabNewRepos.sh`. This grabs github URLs from the README whose address was added to the `_config.yml` file and puts them in the `_explore/input_lists.json` file. 
- They run the bash script in the `_explore/scripts` directory called `BUILD.sh`. This is the main build script for the repository and runs a bunch of python files in the scripts folder and also calls the GitHub API to get information like stars and contributors from each GitHub code repository listed in `input_lists.json`. It also replaces the name of the repository used in the template with the name of the new repository listed in `_config.yml`.
- Lastly, they will run `bundle exec jekyll serve` to start up a server that will show a local version of the webpage at  http://127.0.0.1:4000/nameOfYourRepositoryThatWasSetInConfigYamlFile.

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

## Summary of Where This Start and Where It is Going
IN PROGRESS!

### What is it based off of?
This site was created by taking a fork of the <a href="https://github.com/LLNL/llnl.github.io">Lawrence Livermore National Laboratory's open source software catalog</a> and changing <a href="https://github.com/softwareunderground/open_geosciene_code_projects_viz">a bunch of stuff</a> to make it useful for SWUNG.

### When was it created?
It was initially created as part of the Transform 21' hackathon put on by The Software Underground or SWUNG.

Original Project Plan: https://github.com/softwareunderground/transform-2021-hackathon/discussions/14

The project plan has now been moved to issues: https://github.com/softwareunderground/open_geosciene_code_projects_viz/projects/1


## Prerequisites

Before you begin, make sure you have working installs of Git, Ruby, and Bundler <https://bundler.io/> You will need these tools for development.

## Getting Started

To work locally, first clone into the repository:

```
git clone https://github.com/softwareunderground/open_geosciene_code_projects_viz.git
```

Make sure you are in the directory you just created by running `cd llnl.github.io` Then you can use `bundler` to install the Ruby dependencies (see the [Jekyll installation docs](https://jekyllrb.com/docs/installation/) for step-by-step guides to setting this up):

```
bundle install
```

Running this will install everything in your Gemfile (including Jekyll). Finally, run the development web server with:

```
bundle exec jekyll serve
```

Followed by opening <http://127.0.0.1:4000/open_geosciene_code_projects_viz/> in a web browser.


### Tips

The gems in your sourcefile get updated frequently. It is a good idea to occasionally run `bundle update` from within your project's root directory to make sure the software on your computer is up to date.

Sometimes there can be dependency conflicts if your local version of Ruby is different from this repo or github pages deployment settings. You can find the version number of each of GitHub Page's current dependency's [here](https://pages.github.com/versions/). You can often avoid dependency issues if you use the same versions, including for Ruby. 

As an example, the default version of Ruby used to deploy GitHub Pages on github.com as of 2021-04-08 was Ruby	2.7.1. If you tried running Ruby version 3.0.0 locally on macOS, you'll need to do some extra steps to correctly install the dependencies for this repository. You'd need to run `bundle add webrick` as it is no longer a prepackaged dependency with Ruby in 3.0.0. You may also need to run `gem install eventmachine -- --with-openssl-dir=/usr/local/opt/openssl@1.1` as MacOS >10.14 doesn't use openssl from the same path as is still assumed to be in by eventmachine.






## How to get changes from the template after your repository is already built?
IN PROGESS



# README INFORMATION SPECIFIC TO THIS README AND NOT THE TEMPLATE!




--------------------------------------------------
# OLD README BELOW

### What is the value of this?

The basic idea is that within smaller communities it can be difficult to find applicable open source code for your problem. A lot of what code you use is based on word of mouth and stumbling upon someone else's repository working on similar problems. This can be inefficient. 

<a href="https://github.com/sindresorhus/awesome">Awesome lists</a> are a great way to source code specific to a domain, problem, or use case that others think is "awesome", but they are limited in that they don't show connections between projects or directly show you how popularity of projects might have changed over time.

<i>If it was easier to understand what code is being most used, what code uses similar dependencies, and what projects are attracting the same groups of contributers, community participants might be nudged into more impactful contributions more often.</i>

##### This site uses code repository metadata sourced through the Github API to create new interfaces for exploring code repositories and their connections with the idea that extra view can help drive more impactful contribution & use.  

<br/>

## Summary of Where This Start and Where It is Going

### What is it based off of?
This site was created by taking a fork of the <a href="https://github.com/LLNL/llnl.github.io">Lawrence Livermore National Laboratory's open source software catalog</a> and changing <a href="https://github.com/softwareunderground/open_geosciene_code_projects_viz">a bunch of stuff</a> to make it useful for SWUNG.

### When was it created?
It was initially created as part of the Transform 21' hackathon put on by The Software Underground or SWUNG.

Original Project Plan: https://github.com/softwareunderground/transform-2021-hackathon/discussions/14

The project plan has now been moved to issues: https://github.com/softwareunderground/open_geosciene_code_projects_viz/projects/1

### How to get additional code repositories tracked
Check out the instructions in this <a href="https://github.com/softwareunderground/open_geosciene_code_projects_viz/issues/5">issue</a>.

Also, the plan is to eventually automatically pull in any repository that on github.com that is a part of <a href="https://github.com/softwareunderground/awesome-open-geoscience">AWESOME OPEN GEOSCIENCE</a> awesome list. Awesome lists are a standardized way to share code that many people think is useful to a particular problem, domain, or use case.

### Completed Changes From Original Project & Possible Future Changes Roadmap 
https://github.com/softwareunderground/open_geosciene_code_projects_viz/blob/main/changes_needed.md

### Presentations on What's trying to be accomplished with this repository

SLIDES PRESENTED DURING HACKATHON: https://observablehq.com/@justingosses/more-visible-connections-between-projects-can-nudge-devel 

MEDIUM STORY: https://justingosses.medium.com/beyond-awesome-lists-3ccb074f7859

### How to contribute code improvements
Check out the <a href="https://github.com/softwareunderground/open_geosciene_code_projects_viz/projects/1">issue board </a>. There will be a separate contributions instructions soonish.

