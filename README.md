#Introduction

##How to install Django on Windows
This document will guide you through installing Python 3.7 and Django on Windows. It also provides instructions for installing virtualenv and virtualenvwrapper, which make it easier to work on Python projects. This is meant as a beginner’s guide for users working on Django projects and does not reflect how Django should be installed when developing patches for Django itself.

The steps in this guide have been tested with Windows 7, 8, and 10. In other versions, the steps would be similar. You will need to be familiar with using the Windows command prompt.
##Install Python
Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.7 is the latest version.

To install Python on your machine go to https://python.org/downloads/. The website should offer you a download button for the latest Python version. Download the executable installer and run it. 

After installation, open the command prompt and check that the Python version matches the version you installed by executing:
```sh
...\> python
```
###About pip
pip is a package manage for Python. It makes installing and uninstalling Python packages (such as Django!) very easy. For the rest of the installation, we’ll use pip to install Python packages from the command line.

###Install virtualenv
virtualenv provides a dedicated environment for each Django project you create. While not mandatory, this is considered a best practice and will save you time in the future when you’re ready to deploy your project. To do this, run:

Create a virtual environment for your project:
```sh
...\> mkvirtualenv friend
```
The virtual environment will be activated automatically and you’ll see “(friend)” next to the command prompt to designate that. If you start a new command prompt, you’ll need to activate the environment again using:
```sh
...\> workon friend
```
##Install Django
Django can be installed easily using pip within your virtual environment.

In the command prompt, ensure your virtual environment is active, and execute the following command:
```sh
...\> py -m pip install Django
```
This will download and install the latest Django release.

### Running test Cases

For running test cases you can run follow script.

```sh
python manage.py test
```

