class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,urlToImage):
        self.id =id
        self.name = name
        self.urlToImage = str(urlToImage)


class Article:

    all_articles = []

    def __init__(self,id,name,urlToImage,author,title,url,publishedAt,content):
        self.id = id
        self.name = name
        self.urlToImage = urlToImage
        self.author = author
        self.title = title
        self.url = url
        self.publishedAt = publishedAt
        self.content = content


 #   def save_review(self):
     #   Review.all_reviews.append(self)


   # @classmethod
  #  def clear_reviews(cls):
        Review.all_reviews.clear()

   # @classmethod
 #   def get_reviews(cls,id):

       # response = []

  #      for review in cls.all_reviews:
       #     if review.movie_id == id:
          #      response.append(review)

      #  return response
