# Vapi-Python-Boilerplate
A boilerplate project for using the Vapi API with Python and the command line framework click

## Installation
You can install all of the necessary dependencies to run the project via pip:

``` pip install -r requirements.txt ```

## Usage
All you need to run the project is your Vapi API key, which should be used here:

```vapi = Vapi(api_key='{{api_key_goes_here}}')```

## Prompts
You'll be presented with a series of prompts which will create the settings for your assistant:
  
  1. firstMessage will be how your assistant will greet you
  2. context will be the overall context of the conversation
  3. model will be the llm model used by your assistant
  4. voice will be the voice your assistant uses to talk to you
