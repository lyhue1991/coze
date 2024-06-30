import sys,os
import requests,json 
import pandas as pd 
from IPython.display import display,clear_output,Markdown

class Coze:
    def __init__(self,
                 bot_id=None,
                 api_token=None,
                 max_chat_rounds=20,
                 stream=True,
                 history=None
                ):
        self.bot_id = os.environ['COZE_BOT_ID']
        self.api_token = api_token if api_token else os.environ['COZE_API_TOKEN']
        self.history = [] if history is None else history
        self.max_chat_rounds = max_chat_rounds
        self.stream = stream
        self.url = 'https://api.coze.cn/open_api/v2/chat'
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json','Accept': '*/*',
            'Host': 'api.coze.cn','Connection': 'keep-alive'
        }
        try:
            self.register_magic() 
            response = self('你好')
            if not self.stream:
                print(response)
            print('register magic %%chat sucessed ...',file=sys.stderr)
            self.history = self.history[:-1]
        except Exception as err:
            print('register magic %%chat failed ...',file=sys.stderr)
            print(err)
             
    @classmethod
    def build_messages(cls,history=None):
        messages = []
        history = history if history else [] 
        for prompt,response in history:
            pair = [{"role": "user", "content": prompt,
                     "content_type":"text"},
                {"role": "assistant", "content": response}]
            messages.extend(pair)
        return messages

    @staticmethod
    def get_response(messages):
        clear_output(wait=True)
        dfmsg = pd.DataFrame(messages)
        dftool = dfmsg.loc[dfmsg['type']=='function_call']
        for content in dftool['content']:
            info =json.loads(content)
            s = 'call function: '+str(info['name'])+'; args ='+str(info['arguments'])
            print(s,file=sys.stderr)
        dfans = dfmsg.loc[dfmsg['type']=='answer']
        if len(dfans)>0:
            response = ''.join(dfans['content'].tolist())
        else:
            response = ''
        display(Markdown(response))
        return response

    def chat(self,query,stream=False):
        data = {
            "conversation_id": "123",
            "bot_id": self.bot_id,
            "user": "一个有毅力的吃货",
            "query": query,
            "stream": stream,
            "chat_history": self.build_messages(self.history)
        }
        json_data = json.dumps(data)
        result = requests.post(self.url, headers=self.headers, 
            data=json_data, stream=data["stream"])
    
        if not data["stream"] and result.status_code == 200:
            dic = json.loads(result.content.decode('utf-8'))
            response = self.get_response(dic['messages'])
                
        elif data['stream'] and result.status_code == 200:
            messages = []
            for line in result.iter_lines():
                if not line:
                    continue
                try:
                    line = line.decode('utf-8')
                    line = line[5:] if line.startswith('data:') else line
                    dic = json.loads(line)
                    if dic['event']=='message':
                        messages.append(dic['message'])
                    response = self.get_response(messages)
                except Exception as err:
                    print(err)
                    break 
        else:
            print(f"request failed, status code: {result.status_code}")
        result.close()
        return response
        
        
    def __call__(self,query):
        from IPython.display import display,clear_output 
        len_his = len(self.history)
        if len_his>=self.max_chat_rounds+1:
            self.history = self.history[len_his-self.max_chat_rounds:]
        response = self.chat(query,stream=self.stream) 
        self.history.append((query,response))
        return response 

    def register_magic(self):
        import IPython
        from IPython.core.magic import (Magics, magics_class, line_magic,
                                        cell_magic, line_cell_magic)
        @magics_class
        class ChatMagics(Magics):
            def __init__(self,shell, pipe):
                super().__init__(shell)
                self.pipe = pipe

            @line_cell_magic
            def chat(self, line, cell=None):
                "Magic that works both as %chat and as %%chat"
                if cell is None:
                    return self.pipe(line)
                else:
                    self.pipe(cell)       
        ipython = IPython.get_ipython()
        magic = ChatMagics(ipython,self)
        ipython.register_magics(magic)
        