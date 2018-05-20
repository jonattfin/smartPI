import json
import requests

class CommonApi(object):

    def __init__(self, url):
        self.url = url

    def write(self, params):
        try:
            requests.post(self.url, data=params)
        except Exception as e:
            print("Error while writing to API")

# class LedApi(object):

#     def __init__(self, url):
#         self.url = url

#     def write(self, color):
#         try:
#             params = {'color': color}
#             response = requests.post(self.url, data=params)
#         except Exception as e:
#             print("Error while writing led to API")

# if __name__ == '__main__':
#     print('writing temperatures')

#     common_api = CommonApi("temperatures");
#     common_api.write(1234);

#     led_api = LedApi();
#     led_api.write(1);
#     led_api.write(2);
#     led_api.write(3);
#     led_api.write(4);
