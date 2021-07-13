def domain_name(url):
    urlList = url.split(".")
    if (len(urlList[0]) == 10) or (urlList[0] == "www"):
        return urlList[1]
    #elif urlList[0] == "www":
        #return urlList[1]
    
    ans = urlList[0].split("/")
    return ans[-1]

print(domain_name("https://github.com/Tnguye98/CodeWars/tree/main/Python-Code"))