def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 419 | 403 | 413:
            return "Якась фігня #1"
        case _:
            #return "Something's wrong with the internet"
            return "Якась невідома фігня"
        
print(http_error(419))

# #####
