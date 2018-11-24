import urllib
website = 'http://www.google.com/'
proxylist = ('http://75.101.215.123:9090', 'http://94.198.47.6:3128')
connlist = (urllib.urlopen(website, proxies = {'http': proxy}) for proxy in proxylist)
for conn in connlist:
    print conn.read()
    conn.close()