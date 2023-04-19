# python-tox-example
A Python project with tox configuration and pyenv

# Use case
the example to test if the python script working well with 3.7, 3.8, 3.9, 3.10, 3.11

# How to 
1. install tox in the global environment
```
pip install tox
```

2. install pytest in the global environment
```
pip install pytest
```

3. install python versions
```
pyenv install 3.7
pyenv install 3.8
pyenv install 3.9
pyenv install 3.10
pyenv install 3.11
```

4. run tox
```
tox run
```


5. result

tox shows you the most compatible python versions in the reports