# open_geosciene_code_projects_viz

## Description

This is a website that attempts to offer new ways to understand the variety of open source subsurface geoscience code available for use that people think is valuable.

<b>THIS README WILL BE UPDATED AS THIS REPO IS CHANGED TO BE MORE OF A TEMPLATE. SOME LANGUAGE IS SPECIFIC TO A SINGLE USE CASE STILL</b>

## Live Pages
- Explore page: https://softwareunderground.github.io/open_geosciene_code_projects_viz/explore/
- Dependencies analysis: https://softwareunderground.github.io/open_geosciene_code_projects_viz/explore/dependencies/
- Most popular repositories: https://softwareunderground.github.io/open_geosciene_code_projects_viz/explore/popular-repos/

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
