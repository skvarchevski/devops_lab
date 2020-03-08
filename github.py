#! /usr/bin/env python3

import argparse
import dateutil.parser
import getpass
import requests
import time

parser = argparse.ArgumentParser()

parser.add_argument("--version", help="version", action="version",
                    version="1.0")
parser.add_argument("-u", dest="user", type=str, required=True,
                    help="User whose statistics are gathering (required)")
parser.add_argument("-r", dest="repo", type=str, required=True,
                    help="Repository whose statistics are gathering (required)")
parser.add_argument("-o", dest="opened", action="store_true",
                    help="User who opened pull request")
parser.add_argument("-c", dest="closed", action="store_true",
                    help="User who closed pull request")
parser.add_argument("-d", dest="days", action="store_true",
                    help="Number of days pull requests opened")
parser.add_argument("--stat", dest="stat", action="store_true",
                    help="Basic statistics about merged/closed rate")
parser.add_argument("--deletions", dest="deletions", action="store_true",
                    help="Number of lines deleted in each pull request")

args = parser.parse_args()

def opened_pr(user, repo):
    print("Enter your GitHub login:")
    data_pr = requests.get("https://api.github.com/"
                           "repos/%s/%s/pulls?per_page=100" % (user, repo),
                           auth=(input(), getpass.getpass()))

    
    data_pr = data_pr.json()

    for i in range(len(data_pr)):
        data_tmp = data_pr[i]["user"]["login"]
        title_pr = data_pr[i]["title"]
        print("[OPENED][USER]:The pull request \"%s\" was opened by user:"
              % title_pr, data_tmp)


def closed_pr(user, repo):
    print("Enter your GitHub login:")
    data_pr = requests.get("https://api.github.com/repos/%s/%s/pulls?"
                           "state=closed&per_page=100" % (user, repo),
                           auth=(input(), getpass.getpass()))
    data_pr = data_pr.json()

    
    for i in range(len(data_pr)):
        data_tmp = data_pr[i]["user"]["login"]
        title_pr = data_pr[i]["title"]
        print("[CLOSED][USER]:The pull request \"%s\" "
              "was closed by user:" % title_pr, data_tmp)


def days_opened(user, repo):
    print("Enter your login from GitHub:")
    data_pr = requests.get("https://api.github.com/"
                           "repos/%s/%s/pulls?per_page=100"
                           % (user, repo), auth=(input(), getpass.getpass()))
    data_pr = data_pr.json()

   
 for i in range(len(data_pr)):
        data_tmp = data_pr[i]["created_at"]
        obj_date = dateutil.parser.isoparse(data_tmp)
        obj_date = time.mktime(obj_date.timetuple())
        days = (time.time() - obj_date) / 60 / 60 // 24

        title_pr = data_pr[i]["title"]
        print("[DAYS_AMOUNT]:Number of days the pull request with title "
              "\"%s\" opened:%d" % (title_pr, days))


def stat_merg_closed(user, repo):
    print("Enter your GitHub login:")
    data_pr = requests.get("https://api.github.com/"
                           "repos/%s/%s/pulls?state=all&per_page=100"
                           % (user, repo),
                           auth=(input(), getpass.getpass()))
    
    
    data_pr = data_pr.json()
    j = k = 0
    for i in range(len(data_pr)):
        if data_pr[i]["merged_at"]:
            j += 1
        if data_pr[i]["closed_at"]:
            k += 1
    print("%s pull requests were merged. %s pull requests were closed"
          % (j, k))


def deletions(user, repo):
    print("Enter your GitHub login:")
    login = input()
    passw = getpass.getpass()
    data_pr = requests.get("https://api.github.com/repos/%s/%s/"
                           "pulls?state=all&per_page=100"
                           % (user, repo), auth=(login, passw))
    data_pr = data_pr.json()
    for i in range(len(data_pr)):
        number_pr = data_pr[i]["number"]
        data_tmp = requests.get("https://api.github.com/"
                                "repos/%s/%s/pulls/%s" %
                                (user, repo, number_pr), auth=(login, passw))
        data_tmp = data_tmp.json()
        print("Number of lines deleted in pool request \"%s\":"
              % data_pr[i]["title"], data_tmp["deletions"])


def main():
    user = args.user
    repo = args.repo

    if args.opened:
        opened_pr(user, repo)
    elif args.closed:
        closed_pr(user, repo)
    elif args.days:
        days_opened(user, repo)
    elif args.stat:
        stat_merg_closed(user, repo)
    elif args.deletions:
        deletions(user, repo)
    else:
        print("No arguments for statistics were provided")

main()
