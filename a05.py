# Your code for get_companies_names goes here
def get_companies_names(companyList):
    l = []
    n = len(companyList)
    for i in range (n):
        l.append(companyList[i]['Company Name'])
    return (l)    

# Your code for get_countries goes here
def get_countries(companyList):
    l = {}
    n = len(companyList)
    for i in range (n):
        counter = 0
        for m in range (n):
            if companyList[i]["Country"] == companyList[m]["Country"]:
                counter = counter + 1
        l[companyList[i]["Country"]]=(counter)
    return l

# Your code for get_companies goes here
def get_companies(companyList,location):
    g = []
    n = len(companyList)
    counter = 0 
    for i in range (n):
        if companyList[i]['City'] == location['city'] and companyList[i]['Country'] == location['country']:
            g.append(companyList[i]['Company Name'])
            counter = counter + 1
    if counter == 0:
        print(None)
    else:
        return (g)
