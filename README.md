# Local-NMT: Tutorial to run a pre-trained Machine Translation engine with UI on your local computer

## Installation

On your machine you need to have Python and an VirtualEnv (in this example [pipenv](https://pypi.org/project/pipenv/)) installed.

In case of `pipenv`, clone the repository on your local machine:

- open Terminal/Shell
- navigate to App directory
- pipenv shell
- pipenv install

This will install the required dependencies: flask, transformers, torch, sentencepiece

## Run
- modify the desired language combination directly in app.py, where `source_lang`is the ISO code for the source and `target_lang` for the target language. The corresponding language model, if available, will be automatically downloaded.
- open Terminal/Shell
- navigate to App directory
- pipenv shell
- python app.py
- open Browser and copy and paste URL (typically: http://127.0.0.1:5000/)


 
