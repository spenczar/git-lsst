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

* **List tickets to work on** with `git lsst list`.

* **Start work on a ticket** with `git lsst start-ticket --ticket=<ID>`, eg `git lsst start-ticket --ticket=DM-24500`.

* **Ship a draft of a PR** with `git lsst draft-pr`.

* **Ask for a review** with `git lsst request-review --jira-reviewer=<username>
  --github-reviewer=<username>`. *TODO: help out by letting user just specify
  one of these two*

* **Merge and mark a ticket as done** with `git lsst merge`.

### `git lsst list`

This command will list tickets that you're assigned to. You can filter by status
with `--status`, which can be specified multiple times. `--to-do`,
`--in-progress`, `--in-review`, `--reviewed`, and `--done` are short aliases for
`--status`.

### `git lsst start-ticket`

This command will create a new branch named `tickets/<ticket-id>` and push it.
It will transition the Jira issue to "In Progress."

### `git lsst draft-pr`

### `git lsst request-reviewer`

This command will transition current ticket (based on parsing the branch) to `In
Review`, setting the reviewer based on the `--jira-reviewer` argument. That
argument is used as a search string, so it can be a name, email, or username. If
there are multiple matches, you'll be prompted to select one.

It will also create a new PR if one doesn't exist for this ticket. It will
request a Github review from by `--github-reviewer`; this argument must be a
github username.

### `git lsst merge`

This command will perform a `--no-ff` merge into the `master` branch of the
current ticket, and it will transition the associated Jira ticket to "Done".
