class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,urlToImage):
        self.id =id
        self.name = name
        self.url = url
        self.urlToImage = str(urlToImage)


class Article:

    def __init__(self,id,name,urlToImage,author,title,url,description,publishedAt,content):
        self.id = id
        self.name = name
        self.urlToImage = urlToImage
        self.author = author
        self.title = title
        self.url = url
        self.description = description
        self.publishedAt = publishedAt
        self.content = content


