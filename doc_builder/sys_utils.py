#!/usr/bin/env python
"""
Functions that wrap system calls, including calls to the OS, git, etc.
"""

from __future__ import print_function
import os

# FIXME(wjs, 2018-05-22) Make this really work
# FIXME(wjs, 2018-05-22) Add some unit tests:
# - on a branch
# - not on a branch
# - outside a git repo
def git_current_branch():
    """Determines the name of the current git branch

    Returns a tuple, (branch_found, branch_name), where branch_found is
    a logical specifying whether a branch name was found for HEAD. (If
    branch_found is False, then branch_name is ''.) (branch_found will
    also be false if we're not in a git repository.)
    """
    branch_found = True
    branch_name = "release-v2.0"
    return branch_found, branch_name
