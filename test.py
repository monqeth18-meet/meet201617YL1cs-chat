import turtle


from turtle_chat_client import Client


from turtle_chat_widgets import Button , TextInput


class TextBox(TextInput):
    

    def draw_box(self):
        turtle.clear()
        turtle.penup() 
        turtle.goto(self.pos)
        turtle.pendown()
        turtle.goto(0,self.height)
        turtle.goto(self.width,self.height)
        turtle.goto(self.width,0)
        turtle.goto(self.pos)
        turtle.mainloop()
        
    def write_msg(self):
        self.setup_listeners()
        self.writer.clear()
        print(self.new_msg)
        self.writer.goto(10,self.height - 15)
        self.writer.write(self.new_msg)
    
DB = TextBox()

class SendButton(Button):
    def __init__(self,my_turtle=None,shape=None,pos=(0,0) ,view=None):
        super(SendButton,self).__init__(my_turtle=None, shape=None, pos=(0,0))
        self.view=view
    def fun(self, x=None, y=None):
        self.view.send_msg()

class View:
    _MSG_LOG_LENGTH = 5
    _SCREEN_WIDTH = 300
    _SCREEN_HEIGHT = 600
    _LINE_SPACING = round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self, username = 'Me', partner_name='Partner'):
        self.username = username
        self.partner_name = partner_name

        self.my_client = Client()

        turtle.setup(View._SCREEN_WIDTH , View._SCREEN_HEIGHT)

        self.msg_queue=[]

        self.view_t = turtle.clone()
        self.tb = TextBox()
        self.sb = SendButton()

        self.setup_listeners()

    def send_msg(self):
        Client.send(self.my_client,self.tb.new_msg)
        self.msg_queue.append(self.tb.new_msg)
        self.tb.clear_msg()
        self.display_msg()

    def get_msg(self):
        return self.textbox.get_msg()
    
