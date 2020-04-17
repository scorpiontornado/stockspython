# stockspython

## Prerequisites:

- Install python
- Install pip
- The latest version of Google Chrome, installed in the default location for your OS
- If you don't have macOS - the relevant version of chromedriver for your OS

### Installing python

Optionally, if you have a mac, you can install python with Homebrew, which can be done by following [this guide](https://docs.python-guide.org/starting/install3/osx/).

Homebrew is a useful package manager, and will simplify the install process by automatically installing pip (python's package manager) as well, however macOS should already come with a version of python installed so this is not absolutely necessary.

If you're lazy, this should do it:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
```

### Installing pip

If you do not install python using Homebrew, you will need to manually install pip.

This can be accomplished by following [this guide](https://ahmadawais.com/install-pip-macos-os-x-python/), but note that easyinstall has been depreciated, so you should follow the updated section up the top of the guide instead.

If you're lazy, this should do it:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Installing chromedriver

Only do this if you are not using macOS, or I forgot to update the driver to the latest version of Chrome:

**Note**: Find your version of Chrome by following [this link](chrome://settings/help)

Follow [this link](https://sites.google.com/a/chromium.org/chromedriver/downloads) to go install the relevant version of chromedriver for your version of Chrome and your OS

After you have done that, replace the file "chromedriver" with the file you just downloaded.

## How to use:

See below for detailed steps

1. Set up a virtual environment
2. run stocks_automated.py

### Setting up a virtual environment:

If it is your first time setting up the virtual environment, run the following to create and activate a virtual environment and install the necessary packages:

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

After the first time - run the following to activate the virtual environment:

```
. venv/bin/activate
```

### Running main.py:

Run stocks_automated.py:

```
python3 stocks_automated.py
```

## Random stuff that used to be comments in setup.py

【sss】
https://packaging.python.org/discussions/install-requires-vs-requirements/
https://stackoverflow.com/questions/46877667/how-to-push-a-new-initial-project-to-github-using-vs-code
https://github.com/avinassh/rockstar/blob/master/setup.py#L11,#L19
