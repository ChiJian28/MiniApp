# Profile service

A small Python 3.12 team directory. It uses only the standard library.

People live in `data/users.json`. The shared lookup is `profileapp.users.get_user(user_id)`. `profileapp.roster` is the in-app caller: `show` and `team` both reach the directory through that function.

## Run

From the project root:

```bash
python3 main.py list
python3 main.py show --id 1
python3 main.py team Engineering
python3 -m unittest discover -s tests -t .
```

`python3 -m profileapp` accepts the same commands.

## Expected output

`python3 main.py show --id 1`

```text
Loads user Alice Chen (ID 1)
Title: Backend engineer
Team: Engineering
Email: alice.chen@example.com
```

`python3 main.py list`

```text
1: Alice Chen (Engineering)
2: Ben Wong (Support)
3: Cara Singh (Engineering)
```

An unknown id exits 1 with `No user with id <id>`.

## Layout

```text
data/users.json          synthetic directory records
main.py                  project-root entry point
profileapp/store.py      reads the JSON file
profileapp/users.py      get_user(user_id)
profileapp/roster.py     calls get_user for one person or a team
profileapp/display.py    turns a record into text
profileapp/cli.py        list, show, and team
tests/test_directory.py  checks the current get_user contract
```
