from elem import Elem


class Html(Elem):
    
    def __init__(self, tag='html', attr=..., content=None, tag_type='double'):
        super().__init__(tag, attr, content, tag_type)