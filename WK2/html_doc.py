class Tag:
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        if self.contents == None :
            return "{0.start_tag}".format(self)
        else:
            return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)

class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML', '')
        self.end_tag = ''   # DOCTYPE heeft geen endtag

class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        self._head_contents = []
    
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)
    
    def display(self, file=None):
        for tag in self._head_contents:
            self.contents += str(tag)

        super().display(file=file)


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')   # De inhoud van de body wordt apart opgebouwd
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)

class HtmlDoc(object):
    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()
    
    def add_tag_head(self, name, contents):
        self._head.add_tag(name, contents)
    
    def add_tag_body(self, name, contents=None):
        self._body.add_tag(name, contents)
    
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML Document')
    my_page.add_tag_head('title', 'Muziekschool Session')
    my_page.add_tag_body('h1', 'Muziekschool Session')
    my_page.add_tag_body('h2', 'de specialist in drums en piano')
    my_page.add_tag_body('p', 'verdere informatie staat in deze paragraaf')
    my_page.add_tag_body('br')
    my_page.add_tag_body('p', 'En hier ook! YES IT WORKSSSSS')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)