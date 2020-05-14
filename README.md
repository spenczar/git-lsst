# git-lsst #

This is a set of extensions to `git` for working on the LSST project.

## Installation

Clone this repo, and then `pip install .` inside it.

Then, make a config file with credentials at `~/.config/git-lsst.conf`. The file
should look like this:

```conf
[jira]
username=swnelson
password=YOURPASSWORDHERE

[github]
token=deadbeefdeadbeefdeadbeef
```

The Jira section has your LSST Jira username and password. The Github section
has a github access token, or can take a `username` and `password` if you
prefer.

## Usage

Start work on a ticket with `git lsst start-ticket --ticket=<ID>`, eg `git lsst start-ticket --ticket=DM-24500`.

Ask for a review with `git lsst request-review`, eg

Basic command:
```
-> % git lsst
usage: git-lsst [-h] [-c CONFIG]
                {start-ticket,draft-pr,request-review,merge,list}
                ...

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        config file with Jira auth information

subcommands:
  {start-ticket,draft-pr,request-review,merge,list}
    start-ticket        start work on a ticket
    draft-pr            write a draft PR in Github without
                        requesting a review
    request-review      request a review of the active ticket's
                        state
    merge               merge a PR and mark a ticket as done
    list                list Jira tickets
```

### List Jira tickets you're assigned to
```
-> % git lsst list --help
usage: git-lsst list [-h] [-S, --status STATUSES] [--to-do]
                     [--in-progress] [--in-review] [--reviewed]
                     [--done]

optional arguments:
  -h, --help            show this help message and exit
  -S, --status STATUSES
                        only list issues which match this status.
                        Can be specified multiple times, which will
                        list issues that match any of the specified
                        statuses. By default, everything but Done is
                        listed.
  --to-do               alias for --status 'To Do'
  --in-progress         alias for --status 'In Progress'
  --in-review           alias for --status 'In Review'
  --reviewed            alias for --status 'Reviewed'
  --done                alias for --status 'Done'
```

#### List tickets in progress

```
-> % git lsst list --in-progress
DM-24644 - In Progress - Provide a distributable package for the alert stream simulator
DM-24649 - In Progress - Add integration tests to alert stream simulator
```
