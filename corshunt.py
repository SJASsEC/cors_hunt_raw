import requests
from requests.exceptions import HTTPError

def get_urls():    
    file = open(r'urls.txt', "r")
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
            # headers containting Access-Control-Allow
            is_empty = not res #if true dictionary is empty
            final_exploit(is_empty,url)

            #print("URL:", url, "Header:", res.keys())
        except HTTPError as http_err:
            print(f'HTTP Error:{http_err}')
        except Exception as err:
            print(f'Other error:{err}')

def final_exploit(is_empty,url):
   # print(is_empty)
    if is_empty:
        print(url,"-> Not Vulnerable to CORS")
    else:
        print(url,"Vulnerable to CORS")

def main():
    get_urls()
    advance_hunt()
   
if __name__ == "__main__":
    main()
