import turtle

#import the Client class from the turtle_chat_client module
from turtle_chat_client import Client

#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
from turtle_chat_widgets import Button , TextInput

#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
class TextBox(TextInput):
    
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box
    def draw_box(self):
        self.writer.penup() 
        self.writer.goto(self.pos)
        self.writer.pendown()
        self.writer.goto(0,self.height)
        self.writer.goto(self.width,self.height)
        self.writer.goto(self.width,0)
        self.writer.goto(self.pos)
        self.writer.mainloop()


    def write_msg(self):
        self.setup_listeners()
        print(self.new_msg)

        
        
