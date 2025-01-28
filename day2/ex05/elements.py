from elem import Elem


class Html(Elem):
    
    def __init__(self, attr={}, content=None):
        super().__init__('html', attr, content, 'double')


class Head(Elem):
    
    def __init__(self, attr={}, content=None):
        super().__init__('head', attr, content, 'double')


class Body(Elem):
    
    def __init__(self, attr={}, content=None):
        super().__init__('body', attr, content, 'double')

class Div(Elem):
    
    def __init__(self, attr={}, content=None):
        super().__init__('div', attr, content, 'double')

if __name__ == "__main__" :
    elem = Html(attr={}, content=[Head(), Body(content=Div())])
    print (elem.__str__())

