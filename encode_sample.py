import re
from urllib.parse import urlparse

class Encode:
    def having_ip_address(url):
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4 with port
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
            '([0-9]+(?:\.[0-9]+){3}:[0-9]+)|'
            '((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?)', url)  # Ipv6
        if match:
            return -1
        else:
            return 1
    
    def isLongURL(url):
        length = len(url)
        if (length < 54):
            return 1
        elif (length >= 54 and length <= 75):
            return 0
        else:
            return -1
        
    def Shortining_Service(url):
        match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                        'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                        'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                        'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                        'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                        'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                        'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                        'tr\.im|link\.zip\.net',
                        url)
        if match:
            return -1
        else:
            return 1
        
    def isHaveSymbol(url):
        return 1 if url.find('@') == -1 else -1
    
    def isUsingRedirect(url):
        if url.find('http') != -1:
            return -1 if url.find('//') != -1 else 1
        else:
            return -1 if url[8::].find('//') != -1 else 1
        
    def isAddPrefixSuffix(url):
        return -1 if url.find('-') != -1 else 1
    
    def isHavingSubDomains(url):
        splitURL = url.split('.')
        numOfSubDomains = len(splitURL) - 1
        if numOfSubDomains == 1:
            return 1
        elif numOfSubDomains == 2:
            return 0
        else:
            return -1
        
    def secure_http(url):
        scheme = urlparse(url).scheme
        if scheme == 'https':
            return 1
        else:
            return -1
        
    def convertURL(url):
        result = []
        url = url.replace('www.', '')
        # 'UsingIP'
        result += [Encode.having_ip_address(url)]
        #'LongURL'
        result += [Encode.isLongURL(url)]
        #'ShortURL'
        result += [Encode.Shortining_Service(url)]
        #'Redirecting//',
        result += [Encode.isUsingRedirect(url)]
        #'PrefixSuffix-'
        result += [Encode.isAddPrefixSuffix(url)]
        #'Symbol@'
        result += [Encode.isHaveSymbol(url)]
        #'SubDomains'
        result += [Encode.isHavingSubDomains(url)]
        #'HTTPS',
        result += [Encode.secure_http(url)]

        return result