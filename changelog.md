# My project's changelog

- There is now a `replace_text.sh` simple script to replace project templates in files. One can also use an IDE's global replacement abilities. 

- Changes in project versioning 

- Project root is now automatically detected for codecov uploads using Github actions. See [Issue #1](https://github.com/Nelson-Gon/pytempltaes/issues/1). 

- For the install step, we now use `pip install -e .` in lieu of the now deprecated `setup.py install` and/or `easy_install`. 

- The `install_requires` field in `setup.py` is now automatically generated by reading each line in `requirements.txt`. See [Issue #2](https://github.com/Nelson-Gon/pytemplates/issues/2). 
- We added support for some feature
- We fixed some bug(s). See link to some issue related to the bug. 
