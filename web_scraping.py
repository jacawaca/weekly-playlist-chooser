def scrap_c_dict(save_file=False, file_name='c_dict.json'):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    browser = webdriver.Firefox()

    # geting spotify genres 
    browser.get('https://everynoise.com/everynoise1d.cgi?scope=all')
    genres = []

    tbody = browser.find_element(By.XPATH, '/html/body/table/tbody')
    trs = tbody.find_elements(By.TAG_NAME, 'tr')
    for tr in trs:
        genre = tr.find_elements(By.CLASS_NAME, 'note')[2]
        genres.append(genre.text)
        
    # nations adjectives
    browser.get('https://en.wikipedia.org/wiki/List_of_adjectival_and_demonymic_forms_for_countries_and_nations')

    import re
    def cleanString(string):
        return re.sub('\[.*\]','',string).lower()

    country_3table = []

    table = browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    trs = tbody.find_elements(By.TAG_NAME, 'tr')
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        nation_3list = []
        for td in tds:
            td_list = []
            cslist = td.find_elements(By.CLASS_NAME, 'cslist')
            if len(cslist) == 1:
                lis = cslist[0].find_elements(By.TAG_NAME, 'li')
                for li in lis:
                    td_list.append(cleanString(li.text))
            elif len(cslist) > 1:
                print(f'Łola Boga, Śniący: {len(cslist)}')
            elif len(cslist) == 0:
                td_list.append(cleanString(td.text))
            nation_3list.append(td_list)
        country_3table.append(nation_3list)
        
    # init dicts for each country
    c_dict = {}
    for CR in country_3table: # Country Row
        country_name = CR[0][0]
        c_dict[country_name] = []

    for genre in genres:
        for CR in country_3table:
            country_key = CR[0][0]
            adjs = CR[1]
            for adj in adjs:
                match = re.search(adj,genre)
                if match != None:
                    c_dict[country_key].append(genre)
    import json
    if save_file:
        with open(file_name, 'w') as f:
            json.dump(c_dict,f,indent=4, sort_keys=True)
    return c_dict

def read_c_dict(file_name='c_dict.json'):
    import json
    with open(file_name, 'r') as f:
        c_dict = json.load(f)
    return c_dict