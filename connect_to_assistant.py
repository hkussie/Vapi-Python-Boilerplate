import click
from vapi_python import Vapi

@click.command()
@click.option('--opening', default='Hello! How are you')
@click.option('--context', default='Friendly conversation')
@click.option('--model', prompt='Pick the model to use', type=click.Choice(['gpt-3.5-turbo', 'gpt-4', 'mixtral-8x7b-32768']))
@click.option('--voice', prompt='Pick the voice to talk to', type=click.Choice(['jennifer-playht', 'will-playht', 'chris-playht', 'matt-playht']))
def main(opening, context, model, voice):
    assistant = {
        'firstMessage': f'{opening}',
        'context': f'{context}',
        'model': f'{model}',
        'voice': f'{voice}',
        'recordingEnabled': True,
        'interruptionsEnabled': False
    }
    vapi = Vapi(api_key='21289a2f-f002-46d4-aa5f-b98c4d1c6212')
    vapi.start(assistant=assistant)

if __name__ == "__main__":
	main()