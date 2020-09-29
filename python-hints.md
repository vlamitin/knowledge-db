# Python hints

## venv
- `python3 -m venv venv` - создась venv в папку env
- `source venv/bin/activate`

## pip
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install requests`
- `pip freeze > requirements.txt`

## idea, modules, packages
```
knowledge-db
L python_scripts <-- [mark this directory as sources root](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000646984--Solved-Warnings-import-local-package-Unresolved-references-inspection)
    L pr_helper
        L __init__.py
        L file1.py <-- here import pr_helper.file2
        L file2.py <-- execute from knowdedge-db/python_scripts as python -m pr_helper.file2 
```

## Jypiter notebook
- `pip install ipykernel`
- `python -m ipykernel install --user --name=env` - чтобы venv применилась в ноутбуке
- `jupiter notebook`

# Wheel
- .whl is a simple zip file - change ext to .zip to see the contents
