# fetch_issues
Fetches all issues from a github repository and outputs them as CSV.

usage is:
`fetch_issues.py -o <repository owner> -r <repository name> [-s <issue state: open, closed, or all>]`

This will make successive requests to:

*api.github.com/repos/\<owner>/\<repository>/issues?state=\<state>&page=\<n>* 

incrementing the page so long as issues continue to be returned.  The complete set of issues is output in CSV format w/ the issue number and issue title.  That output can then be read into a spreadsheet for loads of fun.

