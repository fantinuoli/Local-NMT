# Run a pre-trained Huggingface Machine Translation engine with UI on your local computer

## Installation

You need to have Python, [Tensorflow](https://www.tensorflow.org/install), [Torch](https://pytorch.org/get-started/locally/) and an VirtualEnv (in this example [pipenv](https://pypi.org/project/pipenv/)) installed on your machine. Please refer to the respective installation pages.

In case of `pipenv`, clone the repository on your local machine:

- open Terminal/Shell
- navigate to App directory
- pipenv shell
- pipenv install

This will install the required dependencies: flask, transformers, torch, sentencepiece

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
Apache License 2.0
 
