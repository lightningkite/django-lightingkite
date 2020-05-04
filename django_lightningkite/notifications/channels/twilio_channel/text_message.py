

class TextMessage():

    def __init__(self, body=None, to_number=None, from_number=None):
        self.body = body
        self.to_number = to_number
        self.from_number = from_number

    def get_kwargs(self):
        return {
            'body': self.body,
            'from_': self.from_number,
            'to': self.to_number
        }
