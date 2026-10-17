class message_print():
    def __init__(self,message):
        self.msg = message

    def display_message(self):
        print(self.msg)

msg = message_print('This is message value')
msg.display_message()