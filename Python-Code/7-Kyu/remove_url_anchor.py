def remove_url_anchor(url):
    for i in range(len(url)):
        if url[i] == '#':
            url = url[:i]
            break
    return url

print(remove_url_anchor('www.codewars.com#about'))