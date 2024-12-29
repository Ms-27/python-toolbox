- create venv
```
python -m venv .venv
```

- start / stop
```
source venv/bin/activate
deactivate
```

- add to `.bash_profile`
```
alias sv='source venv/bin/activate'
```

- exclude .venv from source control but add requirements.txt
```
pip freeze > requirements.txt
pip install -r requirements.txt
```
