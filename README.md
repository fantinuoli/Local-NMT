# Run a pre-trained Huggingface Machine Translation engine with UI on your local computer

## Installation

You need to have Python (3.8 or 3.9), [Tensorflow](https://www.tensorflow.org/install), [Torch](https://pytorch.org/get-started/locally/) and any VirtualEnv tool (in this example [pipenv](https://pypi.org/project/pipenv/)) installed on your machine. Please refer to the respective installation pages should you have any problem during installation.

The following supposes you are using `pipenv` as virtual environment management, but it will work with any other (just substitute `pipenv`with the usual way you install modules):

- Clone the repository on your local machine (click on the `code` button and download as zip file. Unzip it in a known location.)
- open Terminal/Shell
- navigate to App directory
- pipenv shell
- pipenv install

This will install the required dependencies: flask, transformers, torch, sentencepiece. You can also install these modules manually with `pipenv install`and the name of the module.

Note: I tested this on a macOS with Intel processor. I have not been able to install all dependencies on macOS with the new ARM/M1 processors. On macOS you may need to install `XCode` (you can install it freely from App Store). On Windows the same procedure should work out-of-the-box.  

## Pre-trained translation models
Refer to the [Huggingface](https://huggingface.co/Helsinki-NLP) page for a list of all pre-trained Helsinki MT models. See the language code of the model in the last two parts of the model name (for example `opus-mt-it-en` for Italian to English).

## Run
- modify the desired language combination directly in app.py, where `source_lang`is the language code for the source and `target_lang` for the target language (as in the model name). The corresponding language model will be automatically downloaded.
- open Terminal/Shell
- navigate to App directory
- pipenv shell
- python app.py
- open Browser and copy and paste URL indicated in prompt (typically: http://127.0.0.1:5000/)

## User Interface

![alt text](screen.png?raw=true "User Interface")

## License
MIT
 
