# PatrowlManagerSDK
Python API Client for PatrowlArsenal, PatrowlEngines and PatrowlArsenal

# Pypi Deployment commands
```
rm -rf dist/ build/ PatrowlEnginesUtils.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*
```

# Local setup for tests
pip install -e .
python tests/test_{name}