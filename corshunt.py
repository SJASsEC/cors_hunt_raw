import requests
from requests.exceptions import HTTPError

def get_urls():    
    file = open(r'CORS_Hunter\urls.txt', "r")
    if file.mode == "r":
        contents = file.readlines()
    return contents

def get_valid_headers():
    contents= get_urls()
    header_keys = "Access-Control-Allow"
    #header_keys = "Test"
    for url in contents:
        try:
            response = requests.get(url)
            if (response.status_code == 200):
                header = response.headers
            res = dict(
                filter(lambda item: header_keys in item[0], header.items()))

            print("URL:",url,"Header:",res.keys())
        except HTTPError as http_err:
            print(f'HTTP Error:{http_err}')
        except Exception as err:
            print(f'Other error:{err}')

def advance_hunt():
    same_content= get_urls()
    header_keys = "Access-Control-Allow"
    headers = {'Origin': 'bing.com'}
    for url in same_content:
        try:
            response= requests.post(url,headers=headers)
            if (response.status_code == 200):
                header = response.headers
            res = dict(
                filter(lambda item: header_keys in item[0], header.items()))

            print("URL:", url, "Header:", res.keys())


        
   
def main():
    get_urls()
    
if __name__ == "__main__":
    main()
