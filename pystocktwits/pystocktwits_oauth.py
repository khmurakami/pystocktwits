import requests

class OAuthClient():

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = str(consumer_key)
        self.consumer_secret = str(consumer_secret)
        self.url = "https://api.stocktwits.com/api/2/"
        self.headers = {'Content-Type': 'application/json', 'Authorization': self.consumer_key}


    def authorize(self, client_id, response_type, redirect_uri, scope, prompt=1):

        """
        Description and param's are straight from the documentation

        Allows an application to request user authorization. There are two different flow options depending if your application is client side or server side.
        param client_id: consumer key
        """

        url = self.url + 'oauth/authorize'
        data = {
                 'client_id': '{}'.format(self.consumer_key),
                 'response_type' : '{}'.format(response_type),
                 'redirect_uri' : '{}'.format(redirect_uri),
                 'scope' : '{}'.format(scope),
                 'prompt' : '{}'.format(prompt)
                }

        r = requests.get(url, headers=self.headers, params=data)
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'.format(r.status_code))

        raw_data = r.json()
        print("Sucess")
        return True

    #Get Access Token. This allows a user to use Access level Rest Calls
    def get_access_token(self, grant_type, redirect_uri):
        url = self.url + 'oauth/authorize'
        data = {
                 'client_id': '{}'.format(self.consumer_key),
                 'client_secret' : '{}'.format(self.consumer_secret),
                 'grant_type' : '{}'.format(grant_type),
                 'redirect_uri' : '{}'.format(redirect_uri)
                }

        r = requests.post(url, headers=self.headers, data=data)
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'.format(r.status_code))

        raw_data = r.json()


        print("Sucess")
        return True

if __name__ == "__main__":
    twit = OAuthClient(consumer_key = "", consumer_secret="")
    twit.get_access_token("authorization_code", "")
