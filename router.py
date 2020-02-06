from view import DateHandler
from service import DateService
import pymongo

mg = pymongo.MongoClient('192.168.1.103', 27017)

urlpatterns = [
    (r'/api/date', DateHandler,
     {"service": DateService,
      "MongoDB": mg}),
]
