# lib-ml
We have two kinds of tags: 
- Experimental versions of the style vX.X.X-pre-DATE-XXX.These versions don''t need to be working, and are for developing use.
- Production versions of the style vX.X.X. These are always working versions with new features implemented.

## To trigger the automated version release:
1) Go to repo model-training on GitHub.
2) Click on the "Actions" tab.
3) Select "Versioning Workflow (SemVer + Dated Pre-Releases)" from the list on the left.
4) Choose the type of tag you want: dated-pre for experimental versions, and semver for production versions.
5) Click the “Run workflow” button.
6) When this workflow has been finished, you can go to "Release lib-ml" in the list on the left.
7) As you can see a workflow has automatically been triggered by the releasing of a new version.

## Install
- To install the package, execute the following command and fill in latest VERSION from git:
    '''
    pip install git+https://github.com/remla25-team1/lib-ml.git@VERSION
    '''