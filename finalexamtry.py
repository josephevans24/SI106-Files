x = 2.035
print "%.2f" % x 
a = ['hi', 'bye', 'try']
print a.sort()
sample_post = { 
    "from": { 
        "id": "2220453",  
        "name": "Paul Resnick" 
    },  
    "likes": { 
        "data": [ 
            { 
                "id": "6912",  
                "name": "LB" 
            },  
            { 
                "id": "730",  
                "name": "JL" 
            },  
            { 
                "id": "123948",  
                "name": "???" 
            },  
            { 
                "id": "848",  
                "name": "KR" 
            } 
        ] 
    },  
    "comments": { 
        "data": [ 
            { 
                "from":
                { 
                    "id": "8237",  
                    "name": "MB" 
                } 
                
            },  
            { 
                "from": { 
                    "id": "58763",  
                    "name": "JO" 
                } 
            } 
        ] 
    } 
}  
def likers(sample_post):
    like_ids = []
    for a in sample_post['likes']['data']:
        like_ids.append(a["id"])
    print like_ids
    like_ids = [a["id"] for a in sample_post['likes']['data']]
    print like_ids



    lst = ""
    for a in sample_post['likes']['data']:
        lst += a['id'] + ' '
        like_ids = [word for word in lst.split()]
    return like_ids
print likers(sample_post)