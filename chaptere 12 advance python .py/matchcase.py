
# match case is similar as switch case in c language 
def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server errror"     
             
        case _:
            return "unknown status"     # default case 
        
            
            
n= int(input("enter number for check status"))            
print(http_status(n))            