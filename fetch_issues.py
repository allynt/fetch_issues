__author__ = "allyn.treshansky"

"""
stand-alone script to get all issues from a github repository and output as CSV
"""

import sys, getopt, json, urllib2

##########################
# global fns & variables #
##########################

GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repository}/issues?state={state}&per_page=100&page={page}"
ISSUE_STATES = ["open", "closed", "all"]


def usage():
    """
    print usage instructions
    :return: usage string
    """
    print(u"usage: %s -o <repository owner> -r <repository name> [-s <issue state: open, closed, or all>]" % sys.argv[0])

##########################
# parse cmd-line options #
##########################

owner = None
repository = None
state = "open"

try:
    opts, args = getopt.getopt(sys.argv[1:], 'o:r:s:')
except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-h':
        usage()
        sys.exit(2)
    elif o == '-o':
        owner = a
    elif o == '-r':
        repository = a
    elif o == '-s':
        state = a
    else:
        usage()
        sys.exit(2)

if not (owner and repository):
    usage()
    sys.exit(2)
if state not in ISSUE_STATES:
    usage()
    sys.exit(2)

############
# do stuff #
############

page = 0
issues = []
remaining_issues = True
while remaining_issues:
    page += 1
    try:
        url = GITHUB_API_URL.format(repository=repository, owner=owner, state=state, page=page)
        request = urllib2.urlopen(url=url)
        remaining_issues = json.loads(request.read())
        issues += remaining_issues
        request.close()
    except urllib2.HTTPError as e:
        print "{0} [{1}]".format(e, url)
        sys.exit(2)

for issue in issues:
    print "{0}, {1}".format(
        issue.get("number"),
        issue.get("title").replace(',', '')
    )

###########
# the end #
###########
