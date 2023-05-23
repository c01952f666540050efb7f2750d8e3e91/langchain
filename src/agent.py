from datetime import datetime
from datetime import timezone
import json
import openai


class Message:
    def __init__(self, role:str, content:str):
        self.role = role
        self.content = content

    def ret(self):
        return {
            "role": self.role,
            "content": self.content
        }
    
    def __repr__(self) -> str:
        return str({
            "role": self.role,
            "content": self.content
        })

    def __str__(self) -> str:
        return str({
            "role": self.role,
            "content": self.content
        })

class Agent:
    def __init__(self, openai_apikey, model, verbose:bool=False):
        self.openai_apikey = openai_apikey
        self.model = model
        self.verbose = verbose

        self.stack = [
            # <function1>
            # <function2>
        ]

        self.context = []

        self.body = {
            'is_init': False,
            'statistics': {
                'total': 0,
                'prompt_tokens': 0,
                'completion_tokens': 0
            },
            'counts': [
                {
                    'name': "Init",
                    'count': 1,
                    'conditions': []
                }
                # Where counts of status' goes -> 
                # {
                #   'name': "Name",
                #   'count': 0
                #   'conditions': [
                #       <function1> 
                #       <function2>
                #   ]
                # }
            ],
            'current_response': [{
                'timestamp': 0,
                'text': ''
            }],
            'current_context':[{
                'timestamp': 0,
                'text': ''
                # Timestamp and text in string
            }],  
            'user_intent': [{
                'timestamp': 0,
                'text': ''
                # Timestamp and text in string
            }], 
            'error_messages': [{
                'timestamp': 0,
                'text': ''
                # Timestamp and text in string
            }],
            'previous troubleshooting': [{
                'timestamp': 0,
                'text': ''
                # Timestamp and text in string
            }],
        }
    
    def initialise(self, _context:str ) -> bool:
        if self.verbose:
            print("Initialising...")

        self.body['current_context'].append({
            'timestamp': int(datetime.now(timezone.utc).timestamp()),
            'text': _context
        })

        self.body['is_init'] = True

    def process_response(self, response):
        print(type(response))
        print(response)
        # return json.loads(response)

    def open_interaction(self, initial_content:str) -> bool:

        
        init_content = Message('user', initial_content)

        init_messages = [
            Message('system', self.body['current_context'][-1]['text']).ret(),
            init_content.ret()
        ]

        if self.verbose:
            for msg in init_messages:
                print(msg)
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=init_messages
        )

        print(self.process_response(response))

    def complete(self, response:str) -> bool:
        if not (self.body['is_init']):
            print("Is not initiated!")
            return False
        else:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[
                        {"role": "system", "content": self.body['current_context'][-1]['text']},
                        {"role": "user", "content":response}
                    ]
                    , temperature=0.5)

            print(response)
            return True


