class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url):
        self.id =id
        self.name = name
        self.url = url


class Article:

    def __init__(self,urlToImage,author,title,url,description,publishedAt):
        self.urlToImage = urlToImage
        self.author = author
        self.title = title
        self.url = url
        self.description = description
        self.publishedAt = publishedAt


