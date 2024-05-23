def aparitii_keywords(dictionar_siteuri):

    rezultat = {}


    for site, keywords_list in dictionar_siteuri.items():

        for keyword in keywords_list:

            if keyword in rezultat:
                rezultat[keyword] += 1
            else:
                rezultat[keyword] = 1

    return rezultat

dictionar_siteuri = {'upt.ro': ['cristina', 'home', 'homepage', 'marinescu'], 'uvt.ro': ['timisoara', 'university', 'west']}

dictionar_keywords = aparitii_keywords(dictionar_siteuri)

print(rezultat)

{'upt.ro': ['cristina', 'home', 'homepage', 'marinescu'], 'uvt.ro': ['timisoara', 'university', 'west']}
