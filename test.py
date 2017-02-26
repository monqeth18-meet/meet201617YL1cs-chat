import turtle

from turtle_chat_client import Client

from turtle_chat_widgets import Button , TextInput

zft =turtle.Screen()
zft.bgpic('monqeth.gif')

class TextBox(TextInput):
    
    def draw_box(self):
        turtle.clear()
        self.pos = (-100,0)
        turtle.pensize(5)
        turtle.penup() 
        turtle.goto(self.pos)
        turtle.pendown()
        turtle.goto(-100,self.height)
        turtle.goto(self.width-100,self.height)
        turtle.goto(self.width-100,0)
        turtle.goto(self.pos)
        
    def write_msg(self):
        self.setup_listeners()
        self.writer.clear()
        print(self.new_msg)
        self.writer.goto(-90,self.height - 30)
        self.writer.write(self.new_msg,font=('Ariel',10,'normal'))
'''
        length = 3

        if len(self.new_msg) >= length:
            turtle.penup()
            turtle.goto(-90 , self.height - 60)
            old_msg = self.new_msg[0:length] + '\r' + self.new_msg[length:]
            
            self.writer.goto(10 , self.height - 30)
            self.writer.write(self.new_msg[length:],font=('Ariel',15,'normal'))

        else:
            self.writer.clear()
            self.writer.write(self.new_msg,font=('Ariel',15,'normal'))
'''

class SendButton(Button):
    def __init__(self,my_turtle=None,shape=None,pos=(0,-50) ,view=None):
        
        super(SendButton,self).__init__(my_turtle=None, shape=None, pos=(0,-50))
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
        self.sb = SendButton(view = self)
        self.setup_listeners()

    def send_msg(self):
        Client.send(self.my_client,self.tb.new_msg)
        self.msg_queue.append(self.tb.new_msg)
        self.tb.clear_msg()
        self.display_msg()

    def get_msg(self):
        return self.textbox.get_msg()

    def setup_listeners(self):
        pass
        
    def msg_received(self , msg):
        print(msg)
        show_this_msg = self.partner_name + ' says:\r' + msg
        self.msg_queue.append(msg)
        self.display_msg()

    def display_msg(self):
        self.view_t.pensize(10)
        self.view_t.color('white')
        self.view_t.penup()
        self.view_t.hideturtle()
        self.view_t.goto(-90, 115)
        self.view_t.clear()
        self.view_t.write(self.msg_queue[-1],font=('Noto Sans Mono CJK JP Bold',10,'normal'))


if __name__ == '__main__':
    print('helloworld')
    my_view=View()
    _WAIT_TIME=200 
    def check() :
        msg_in=my_view.my_client.receive()
        if not(msg_in is None):
            if msg_in==my_view.my_client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) 
    check()
    turtle.mainloop()
