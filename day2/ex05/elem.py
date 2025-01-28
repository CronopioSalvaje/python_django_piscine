#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        tt = super().__str__()
        tt = tt.replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')
        return tt
    


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    
    count = 0

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if str(type(content)) == "<class 'str'>":
            raise Elem.ValidationError
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = "<" + self.tag + self.__make_attr() + ">"

        if Elem.check_type(self.content):
            result += self.__make_content()
        if self.tag_type == 'double':
            result += "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            pass
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if isinstance(self.content, Elem):
            return '\n  ' + self.content.__str__() + '\n'
        elif len(self.content) == 0:
            return ''
        result = ''
        elems = 0
        for elem in self.content:
            if isinstance(elem, Elem):
                elems += 1
                result += '\n  ' + elem.__str__()
            elif len(elem) == 0:
                continue
            else:
                elems += 1
                result +='\n  ' + elem
        if elems > 0:
            result += '\n'
        return result

    class ValidationError(Exception):
        def __init__(self, *args):
            super().__init__(*args)    


    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == "__main__" :
    elem = Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double')
    print (elem.__str__())


     # Default behaviour :
    elem = Elem() # == '<div></div>'
    print ("1\n" + elem.__str__())
    # Arguments order :
    elem = Elem('div', {}, None, 'double') # == '<div></div>'
    print ("2\n" + elem.__str__())
    # Argument names :
    elem = Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double') #== '<body>\n  <div></div>\n</body>'
    print ("3\n" + elem.__str__())
    # With elem as content :
    elem = Elem(content=Elem())#== '<div>\n  <div></div>\n</div>'
    print ("4\n" + elem.__str__())
    # With list as content :
    elem = Elem(content=[Text('foo'), Text('bar'), Elem()])# == '<div>\n  foo\n  bar\n \
# <div></div>\n</div>'
    print ("5\n" + elem.__str__())
    elem = Elem(content=Elem(content=Elem(content=Elem())))
    print ("6\n" + elem.__str__())
    elem = Elem(content=[Text(''), Text('')])
    print ("7\n" + elem.__str__())

    elem = Elem(content='')