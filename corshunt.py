import requests
from requests.exceptions import HTTPError


def get_urls():    
    file=open("urls.txt","r")
    if file.mode == "r":
        contents = file.readlines()
        connector(contents)
def connector(contents):
    for url in contents:
        try:
            response = requests.get(url)
            if (response.status_code == 200):
                print("URL:",url)
                print("Header:",response.headers)
                print(response.elapsed)
                print(response.content)
                print(response.text)
                
                
        except HTTPError as http_err:
            print(f'HTTP Error:{http_err}')
        except Exception as err:
            print(f'Other error:{err}')
        
    

def main():
    get_urls()

if __name__ == "__main__":
    main()
    
