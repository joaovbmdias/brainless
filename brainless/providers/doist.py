# import requests

# from oauthlib.oauth2 import BackendApplicationClient
# from requests_oauthlib import OAuth2Session
# from requests.auth import HTTPBasicAuth

# def connect():
#     client_id = input('Input client id: ')#          fd6fdae4018a4d2cbf42333a53216bcc
#     client_secret = input('Input client secret: ')#      054bdbffdf784ac48a1981a743ba663b

#     auth = HTTPBasicAuth(client_id, client_secret)
#     client = BackendApplicationClient(client_id=client_id)
#     oauth = OAuth2Session(client=client)
#     token = oauth.fetch_token(token_url='https://todoist.com/oauth/authorize', auth=auth)

#     #secret_string = "we4otry2v389wncoh4vomieiothc"
#     #result = requests.get("https://todoist.com/oauth/authorize?client_id=fd6fdae4018a4d2cbf42333a53216bcc&scope=data:read_write:delete&state={}".format(secret_string))
#     print(token)

# def get_tasks():
#     result = requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer %s" % "0b752352ce6ab62348195a8efc218130bbc5da8d"}).json()
#     print(result)

# if __name__ == "__main__":
#     connect()