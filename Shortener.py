import requests


class URLShortener():

    def __init__(self):
        self.apiKey = '6352a071252f432d9d051c3e05b8fc0ed7c9e'
        self.baseURL = 'https://cutt.ly/api/api.php'

    def shortenLink(self, fullLink, linkName):
        self.payload = {'key': self.apiKey, 'short': fullLink, 'name': linkName}
        self.req = requests.get(self.baseURL, params=self.payload)
        self.data = self.req.json()

        print('')
        
        try:
            Title = self.data['url']['title']
            Shortlink = self.data['url']['shortLink']
            print('Title: ', Title)
            print('Link: ', Shortlink)

        except:
            Status = self.data['url']['status']
            print('Error Status: ', Status)


if __name__ == '__main__':
    URLShortener().shortenLink(input('Enter link >> '), input('Name your Link >> '))


################################################
# With Pyshortener
################################################



import pyshorteners


class  Shortener(): 
    def shortenURL(self, url):
        self.shortLink = pyshorteners.Shortener()
        print(self.shortLink.tinyurl.short(url))

if __name__ == '__main__':
    Shortener().shortenURL(input('Enter URL: '))
