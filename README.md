# Profile service

A small Python 3 program. `users.py` defines `get_user(user_id)`. `main.py` loads user 1 through that function.

## Run

```bash
python3 users.py
python3 main.py
```

Expected output:

```text
user 1: id=1 name=Alice Chen
Loads user Alice Chen (ID 1)
```

`python3 main.py` prints both lines. `python3 users.py` prints only the first.
