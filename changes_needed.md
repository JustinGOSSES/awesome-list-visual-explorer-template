## Future Vision
### Read about potential vision for using this approach as an Awesome List add-on:
https://justingosses.medium.com/beyond-awesome-lists-3ccb074f7859

### Read slides presented during hackathon when development work first occured:
https://observablehq.com/@justingosses/more-visible-connections-between-projects-can-nudge-devel

----------------------------------------------------------------

## Types of Changes from LLNL Original Already Done
### LLNL content that is just removed or links to them take away
- Entire folders & markdown removed
  - About/FAQ
  - posts/*
  - news/*
  - radiuss/*
  - JS/Explore/pie_activityCommits.js
  - JS/Explore/pie_activityLines.js
  - JS/Explore/line_repoCreationHistory.js

### LLNL content that is swapped out
#### Swapped out individual words
  - About/index.md
  - Changes across a variety of files.... Most common = "LLNL" => "SWUNG"
  - Changes across a variety of files.... Less common = "LLNL" => ""
#### HTML Elements Removed
- Links to certain pages that have been replaced
  - header 
    - github repo
    - fork this repo
    - twitter
  - -in progress-
- Links to certain pages have been removed entirely:
    - header: -in progress-
    - homepage: -in progress-

### Configuration Changed in _config.yml
- replaced
```
url: "https://software.llnl.gov"
repo_u
```
with 
```
baseurl: "/open_geosciene_code_projects_viz"
```


--------------------------------------------------------------------------------
## Future Improvements

### Components of a Version of this that Could be Ready Made Add-on to Awesome Lists

#### Getting the list of code projects Automatically Updated

The code currently takes in a manually generated list of projects on GitHub stored in this JSON file. It can also be given an org or user accounts and then it also gets every repository owned by those entities in addition to the specifically listed repositories. A major limitation is it won't work with anything not on GitHub, because it uses the Github API to find all the metadata. 

Currently, I'm manually copied the github links from https://github.com/softwareunderground/awesome-open-geoscience into the JSON file, but ideally you'd have a GitHub Actions script that would scrape all GitHub repository links from the README.md file used in the Awesome list and populate any updates into the JSON file used to fetch the metadata. 

- <b>Specifically add CI/CD automation such that any changes in <a href="https://github.com/softwareunderground/awesome-open-geoscience">AWESOME OPEN GEOSCIENCE</a> awesome list show up here.</b> 

This approach is a little fragile in the sense that if someone where to add a project to the Awesome List and not follow the standard, format, GitHub Actions script that scrapes the GitHub repo links might fail. I've also considered changing the Awesome List repo's structure such that contributors add new projects to a CSV and CI/CD adds those projects to an automatically created markdown file that forms the human readable Awesome List. This has the advantage that the GitHub repo links are in a structured file in a known location. The cost is the process of submitting a new project is slightly elevated in complexity. This idea is being discussed in this WIP (Work in Progress) Pull Request. 

#### Getting the metadata

The original LLNL project has a variety of pre-written scripts for the GitHub API that do all the heavy lifting. I've pretty much used them exactly as is and didn't need to change a thing. If I wanted additional metadata from the API or the Github API changed structure, then there might be some needed changes here.

#### Adding to the visualizations
The visualizations are d3.js based. Most of the code for each individual visualization list in separate files. 

This makes updates or adding new one relatively straight forward, but there could be some documentation and best practices for this in order to ensure long-term updats and reusability.

##### Modifications to Existing Visualizations in the LLNL version
The visualizations were mostly used as is with exception of some LLNL branding and content that was removed as well as file paths. 

The file paths needed to be changed as the original ones only work if the website is deployed on its own domain. As a Github Pages page under a repository path, there needed to be changes both to the configuration file _config.yml and to individual file paths in various HTML and JavaScript files. A small number of these are listed in here. 

For most people who would want to deploy this a a GitHub Pages off their repository, starting with a fork of open_geoscience_code_projects_viz would be easier than starting from the original llnl.github.io repository but there's more to be done that could minimize these complications.

#### The web framework
The original LLNL software catalog is a Jekyll site with some content written directly in HTML, CSS, and JavaScript and other pages written in markdown that generates HTML, CSS, and JavaScript when deployed. As it is Jekyll site, it can be deployed as a Github Pages website (static front-end only) deployed directly on GitHub.com.

#### The content
The original LLNL software catalog repository is primarily the repository of their actual software catalog website. As such, it has a lot of content that is LLNL specific and not useful to anyone trying to reuse their repository for their own purposes.

Most of this content is in markdown files within specific sections of the website, which makes removing it relatively simple. You just comment out the links in the header.html file and then delete specific folders and their content. For example, I deleted the news and radiuss folders. 

Slightly harder is the content that is written into the homepage.html file and other CSS, JavaScript, and HTML layout files that are reused. In the open_geosciene_code_projects_viz repo, I've tried to limit project specific content within these files as much as possible. There's more that could be done in terms of having more of the page names, titles, etc. be generated from the _config.yml file and not be hardcoded into the CSS, JavaScript, and HTML files.

--------------------------------------------------------------------------------

## Issues are in a Project Template:
Here: https://github.com/softwareunderground/open_geosciene_code_projects_viz/projects/1


