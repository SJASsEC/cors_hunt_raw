import requests
from requests.exceptions import HTTPError

def get_urls():    
    file = open(r'urls.txt', "r")
    if file.mode == "r":
        contents = file.read().splitlines
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
            print(f'Other error in get_valid_headers :{err}')

def advance_hunt():
    result=[]
    same_content= get_urls()
    header_keys = ["Access-Control-Allow-Credentials",
                   "Access-Control-Allow-Origin"]
    header1 = {'Origin': 'bing.com'}
    for urll in same_content():  
        # https://stackoverflow.com/questions/30234630/builtin-function-or-method-object-is-not-iterable
        try:
            response= requests.get(urll,headers=header1)
            if (response.status_code == 200):
                header = response.headers  

            for hkey in header_keys:
                res = dict(filter(lambda item: hkey in item[0], header.items()))
                result.append(not res)     #if true dictionary is empty

            final_exploit(result,urll)
            

        except HTTPError as http_err:
            print(f'HTTP Error:{http_err}')
        except Exception as err:
            print(f'Other error in advance_hunt:{err}')

def final_exploit(result,urll):
   # print(is_empty)
    if 'True'in result:
        print(urll,"-> Not Vulnerable to CORS...")
    else:
        print(urll,"Vulnerable to CORS")

def main():
    advance_hunt()
   
if __name__ == "__main__":
    main()
