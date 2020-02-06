import traceback
import tornado.web
import tornado.ioloop
import json

class DateHandler(tornado.web.RequestHandler):
    """"""

    def initialize(self, service, mongodb):
        self.service = service(mongodb)
        

    def post(self):
        # 处理输入信息，无论处理是否失败都返回
        try:
            count = self.service.do(date=req['date'])
            response = {"code": 0, "msg": "success",
                        "data": {"count": count}}
        except Exception as e:
            traceback.print_exc()
            response = {"code": -1, "msg": str(e)}
            raise e
        print(response)
        self.write(json.dumps(response))

def test():
    '''
    curl -H "Content-Type:application/json" -X POST --data '{}' http://127.0.0.1:8588/
    '''
    import requests
    url = "127.0.0.1:5011/api/date"
    j = {
        "data": {
            "date": "20200205"
        }
    }
    rs = requests.post(
        url, headers={'Content-Type': 'application/json'}, json=j)
    print(rs)


if __name__ == '__main__':
    test()
