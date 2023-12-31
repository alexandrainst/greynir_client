<a href="https://github.com/alexandrainst/greynir_client"><img src="https://github.com/alexandrainst/greynir_client/raw/main/gfx/alexandra_logo.png" width="239" height="175" align="right" /></a>
# greynir_client

Python client for Miðeind's Greynir language models

______________________________________________________________________
[![Code Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](https://github.com/alexandrainst/greynir_client/tree/main/tests)


Developer(s):

- Peter Bjørn Jørgensen (peter.jorgensen)


## Setup

### Installation

1. Run `make install`, which sets up a virtual environment and all Python dependencies therein.
2. Run `source .venv/bin/activate` to activate the virtual environment.

### Adding and Removing Packages

To install new PyPI packages, run:
```
poetry add <package-name>
```

To remove them again, run:
```
poetry remove <package-name>
```

To show all installed packages, run:
```
poetry show
```


## A Word on Modules and Scripts
In the `src` directory there are two subdirectories, `greynir_client`
and `scripts`. This is a brief explanation of the differences between the two.

### Modules
All Python files in the `greynir_client` directory are _modules_
internal to the project package. Examples here could be a general data loading script,
a definition of a model, or a training function. Think of modules as all the building
blocks of a project.

When a module is importing functions/classes from other modules we use the _relative
import_ notation - here's an example:

```
from .other_module import some_function
```

### Scripts
Python files in the `scripts` folder are scripts, which are short code snippets that
are _external_ to the project package, and which is meant to actually run the code. As
such, _only_ scripts will be called from the terminal. An analogy here is that the
internal `numpy` code are all modules, but the Python code you write where you import
some `numpy` functions and actually run them, that a script.

When importing module functions/classes when you're in a script, you do it like you
would normally import from any other package:

```
from greynir_client import some_function
```

Note that this is also how we import functions/classes in tests, since each test Python
file is also a Python script, rather than a module.


## Features

### Docker Setup

A Dockerfile is included in the new repositories, which by default runs
`src/scripts/your_script.py`. You can build the Docker image and run the Docker
container by running `make docker`.

### Automatic Documentation

Run `make docs` to create the documentation in the `docs` folder, which is based on
your docstrings in your code. You can view this by running `make view-docs`.

### Automatic Test Coverage Calculation

Run `make test` to test your code, which also updates the "coverage badge" in the
README, showing you how much of your code base that is currently being tested.

### Continuous Integration

Github CI pipelines are included in the repo, running all the tests in the `tests`
directory, as well as building online documentation, if Github Pages has been enabled
for the repository (can be enabled on Github in the repository settings).

### Code Spaces

Code Spaces is a new feature on Github, that allows you to develop on a project
completely in the cloud, without having to do any local setup at all. This repo comes
included with a configuration file for running code spaces on Github. When hosted on
`alexandrainst/greynir_client` then simply press the `<> Code` button
and add a code space to get started, which will open a VSCode window directly in your
browser.


## Project structure
```
.
├── .devcontainer
│   └── devcontainer.json
├── .github
│   └── workflows
│       └── docs.yaml
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── README.md
├── config
│   ├── __init__.py
│   ├── config.yaml
│   └── hydra
│       └── job_logging
│           └── custom.yaml
├── data
│   ├── final
│   │   └── .gitkeep
│   ├── processed
│   │   └── .gitkeep
│   └── raw
│       └── .gitkeep
├── docs
│   └── .gitkeep
├── gfx
│   ├── .gitkeep
│   └── alexandra_logo.png
├── makefile
├── models
│   └── .gitkeep
├── notebooks
│   └── .gitkeep
├── poetry.toml
├── pyproject.toml
├── src
│   ├── scripts
│   │   ├── fix_dot_env_file.py
│   │   └── your_script.py
│   └── greynir_client
│       ├── __init__.py
│       └── your_module.py
└── tests
    ├── __init__.py
    └── test_dummy.py
```
