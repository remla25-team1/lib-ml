# lib-ml
## To trigger the automated version release:
1) Go to repo model-training on GitHub.
2) Click on the "Actions" tab.
3) Select "Automated Pre-Release Versioning" from the list on the left (the name from name: Automated Pre-Release Versioning).
4) Click the “Run workflow” button.

## To do version bump:
1) Update VERSION.txt to new base version.
2) Commit and push it.
3) Run above steps to trigger automated version release.

## Install
- To install the package, execute the following command:
    '''
    pip install git+https://github.com/remla25-team1/lib-ml.git@VERSION
    '''