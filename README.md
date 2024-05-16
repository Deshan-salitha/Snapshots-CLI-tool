# snapshots
> A tool to import files into a database with ease!

## Introduction

The goal of this challenge is to see how you approach programming and to serve as a basis for a conversation.

We'll be discussing your solution during our next interview.

## What we want from you

1. You'll have to write a solution to the tasks listed below.
2. When you're done, push the code directly to the Github repository and send us an email.

## Additionnal information

- Timebox. We think you can do this in less than 3 hours without any issue, but if you get stuck, don't spend all your
  weekend on it. These tasks are the basis of a conversation for us.
  Structure your work in a state that you'd be able to pick it up later.
- You can write this in any programming language you like. We prefer Python.
- We expect to be able to run the code on our computers, mostly MacOS / Linux.

---

## Tasks

### Task 1 - Load snapshot into a database

Implement a CLI tool called `snapshots` which loads the csv files found under `data/` into a mysql database.
```
$ snapshots --database localhost:5432 data/snapshot_20230101.csv data/snapshot_20230603.csv
```

### Task 2 - Snapshot Metadata

Implement a solution which lists the snapshots which were imported into the database.
```
$ snapshots list
# A list of relevant information about imported snapshots should show here.
```
This command should help us understand:
- Which snapshots were imported?
- When were the snapshots imported?
- Is this snapshot file already imported the database?

You are free to design any solution that helps us answer these questions.


### Task 3 - Snapshot Service

Implement a long-running service which continuously imports snapshots into the database:
```
snapshots sync --database localhost:5432 --data-dir data/
```
The service should detect snapshot files added to the `data/` directory after it was launched and load them as well.

You'll get bonus points if you are able to add some basic telemetry!


## Final Words

Complete as much of the challenge as you can. We'll be talking thru your solution in our interview.
