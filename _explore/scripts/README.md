# Software Portal Exploration Scripts

These are a set of scripts for updating the local github data in this repository, used as the source for displaying the content on software.llnl.gov

## Getting Started

```
# Create a Python virtual environment
virtualenv -p python3 venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script to get details from an awesome list
bash grabNewRepos.sh

# Run the collection script
bash BUILD.sh
```
