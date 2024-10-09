import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_joke():
    try:
        clear()
        put_html(
            '<p align="left">'
            '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Joke Generator</h2>'
            '</p>'
        )
        
        url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Spooky?format=txt&amount=2"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = json.loads(response.text)
        
        for joke in data['jokes']:
            style(put_text(joke['joke']), 'color:blue; font-size: 30px')
            put_text('...')
        
        put_buttons(
            [dict(label='Click me', value='outline-success', color='outline-success')],
            onclick=get_joke
        )
    
    except requests.exceptions.RequestException as e:
        put_text("Error fetching joke: " + str(e))
    
    except json.JSONDecodeError as e:
        put_text("Error parsing joke data: " + str(e))
    
    except Exception as e:
        put_text("An unexpected error occurred: " + str(e))

if __name__ == '__main__':
    try:
        put_html(
            '<p align="left">'
            '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Joke Generator</h2>'
            '</p>'
        )
        
        put_buttons(
            [dict(label='Click me', value='outline-success', color='outline-success')],
            onclick=get_joke
        )
        hold()
    
    except Exception as e:
        put_text("An unexpected error occurred: " + str(e))