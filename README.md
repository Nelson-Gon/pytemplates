# Our Project: What the project does 

Welcome to our project. 

**Please note that this is a template repository, click use template (do not fork unless suggesting an improvement) to use in a new project and edit files as required**. Also, see important notes at the end of this file. 

# Installation Guide

```shell
pip install our_project 
```

# Currently implemented features

`our_project` currently does the following:

- [x] Contains base class `HelloWorld` 

- [x] `HelloWorld` has the `print_text` method that prints user supplied text. 

- [x] A github action to test project installation and run tests.

- [x] A github action to release on PyPI (requires adding `PYPI_USERNAME` and `PYPI_PASSWORD` to repository secrets.)

# Features that need further attention 

We intend to work on the following in the future:

- [ ] Make it less cumbersome to init docs with `sphinx`. 


# Document generation 

Please edit `docs/source/index.rst` and `docs/source/modules.rst` as required then run:

```shell
./scripts/mkdocs.sh 

```

The above assumes you are at the root of "our_project". 

Also delete `setup.rst`, `tests.rst`, if they exist. 

Otherwise, run and edit as necessary.  

```shell
sphinx-quickstart
```

Thank you,

NelsonGon
22/10/2021 


---

# Important Notes 

This repository holds templates that follow a typical workflow for new `python` projects.

**A word of caution**

These templates are mostly intended to save time. However, modern IDEs provide project templates that are more mature and less opinionated than the templates here. 

This repository serves an additional purpose of allowing developers new to programming to study project structure using very simple examples. 

For licenses, tests, and workflows, gitignore it is recommended that one generates these automatically either from their IDE of choice or for `.gitignore` files and licenses, via github or gitlab. 

Happy to hear from you in case of any questions and/or feedback.



