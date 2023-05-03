#!/usr/bin/env python3

from os import path,environ
from github import Github

GITHUB_TOKEN = environ.get( 'GITHUB_TOKEN', None )

if GITHUB_TOKEN == None:
    print( "Reading token file..." )
    with open( '.token' ) as f:
        GITHUB_TOKEN = f.read().strip()

g = Github( GITHUB_TOKEN )
for repo in g.get_user().get_repos():
    print( F"{repo.name}" )
    for release in repo.get_releases():
        print( F"  - {release.tag_name}" )
        print( F"    - {release.title}" )
        print( F"    - {release.zipball_url}" )