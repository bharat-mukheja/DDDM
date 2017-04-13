
# coding: utf-8

# In[5]:

def clean(token):
    token = re.sub('[(,;%$)]', '', token)
    return token

# In[55]:

from bs4 import BeautifulSoup
import requests
import re
import csv
j = 0
ecof = open('data\\economy.csv', 'w')
geof = open('data\\geography.csv', 'w')
demf = open('data\\demographics.csv', 'w')
socf = open('data\\society.csv', 'w')
inff = open('data\\infrastructure.csv')
ecow = csv.writer(ecof)
geow = csv.writer(geof)
demw = csv.writer(demf)
socw = csv.writer(socf)
infw = csv.writer(inff)

countries = ['af', 'ba', 'cy', 'eg', 'ir', 'iz', 'is', 'jo', 'ku', 'le', 'ly', 'mu', 
                'pk', 'qa', 'rs', 'sa', 'su', 'sy', 'tu', 'ae', 'us', 'ym']
for country in countries:
    url = 'https://www.cia.gov//library/publications//the-world-factbook//geos/print_'
    url += country
    url += '.html'
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    categories = soup.find_all(class_='category')
    
    area = 0
    area_wat = 0
    resources = []
    hazards = []
    ethnic_grps = []
    pop = 0 
    religions = []
    age_014 = 0
    age_1524 = 0
    age_2554 = 0
    age_5564 = 0
    age_65p = 0
    dep_rat_total = 0
    dep_rat_youth = 0
    dep_rat_eld = 0
    dep_rat_potsup = 0
    med_age = 0
    pop_growth = 0
    birth_rate = 0
    death_rate = 0
    net_mig = 0
    urban_pop = 0
    urban_rate = 0
    maternal_mort = 0
    infant_mort = 0
    life_exp = 0
    fertility = 0
    health_exp = 0
    imp_wat = 0
    imp_san = 0
    hiv_rat = 0
    obesity = 0
    education = 0
    lit = 0
    gdp_exch = 0
    gdp_percap = 0
    agriculture = []
    industries = []
    ind_growth = 0
    unemploy = 0
    poverty = 0
    exports = 0
    imports = 0
    exch_rat = 0
    elec_prod = 0
    elec_ff = 0
    oil_prod = 0
    oil_exp = 0
    ref_pet_prod = 0
    ref_pet_exp = 0
    nat_gas_prod = 0
    nat_gas_exp = 0
    co2 = 0
    internet = 0
    mil_exp = 0
    
    i = 0
    try: 
        while i < 500:
            cur = categories[i]
            cat = categories[i].get_text()
            cur = cur.find_next_sibling()
            while re.search(":$", cur.get_text()) == None:
                abc = cur.get_text().split()
                labc = len(abc)
                if (cat == 'Religions:'):
                    for l in range(0,labc - 1):
                        t1 = clean(abc[l])
                        t2 = clean(abc[l+1])
                        if t1 == 'Muslim':
                            religions.append(t1 + ' ' + t2)
                        elif t1 == 'Shia':
                            religions.append(t1 + ' ' + t2)
                        elif t1 == 'Sunni':
                            religions.append(t1 + ' ' + t2)            
                elif (cat == 'Age structure:'):
                    for l in range(0,labc - 3):
                        t1 = clean(abc[l])
                        t2 = clean(abc[l+2])
                        if t1 == '0-14':
                            age_014 = t2
                        elif t1 == '15-24':
                            age_1524 = t2
                        elif t1 == '25-54':
                            age_2554 = t2
                        elif t1 == '55-64':
                            age_5564 = t2
                        elif t1 == '65':
                            age_65p = clean(abc[l+4])
                elif (cat == 'Dependency ratios:'):
                    for l in range(0,labc - 3):
                        t1 = clean(abc[l])
                        t2 = clean(abc[l+3])
                        if t1 == 'total' and dep_rat_total == 0:
                            dep_rat_total = t2
                        elif t1 == 'youth' and dep_rat_youth == 0:
                            dep_rat_youth = t2
                        elif t1 == 'elderly' and dep_rat_eld == 0:
                            dep_rat_eld = t2
                        elif t1 == 'potential' and dep_rat_potsup == 0:
                            dep_rat_potsup = t2
                elif (cat == 'Median age:'):
                    for l in range(0,labc - 1):
                        t1 = clean(abc[l])
                        t2 = clean(abc[l+1])
                        if t1 == 'total:':
                            med_age = t2
                elif (cat == 'Population growth rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        pop_growth = t1
                elif (cat == 'Birth rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        birth_rate = t1
                elif (cat == 'Death rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        death_rate = t1
                elif (cat == 'Net migration rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        net_mig = t1
                elif (cat == 'Urbanization:'):
                    for l in range(0,labc - 3):
                        t1 = clean(abc[l])
                        t2 = clean(abc[l+2])
                        if t1 == 'urban':
                            t2 = clean(abc[l+2])
                            urban_pop = t2
                        elif t2 == 'urbanization:':
                            t2 = clean(abc[l+3])
                            urban_rate = t2
                elif (cat == 'Maternal mortality rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        maternal_mort = t1
                elif (cat == 'Infant mortality rate:'):
                    t1 = clean(abc[0])
                    if t1 == 'total:':
                        t2 = clean(abc[1])
                        infant_mort = t2
                elif (cat == 'Life expectancy at birth:'):
                    t1 = clean(abc[0])
                    if t1 == 'total':
                        t2 = clean(abc[2])
                        life_exp = t2
                elif (cat == 'Total fertility rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        fertility = t1
                elif (cat == 'Health expenditures:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        health_exp = t1
                elif (cat == 'HIV/AIDS - adult prevalence rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        hiv_rat = t1
                elif (cat == 'Obesity - adult prevalence rate:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        obesity = t1
                elif (cat == 'Education expenditures:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        education = t1
                elif (cat == 'Literacy:'):
                    t1 = clean(abc[0])
                    if t1 == 'total':
                        t2 = clean(abc[2])
                        lit = t2
                elif (cat == 'GDP (official exchange rate):'):
                    t1 = clean(abc[0])
                    t2 = clean(abc[1])
                    if t1 != 'country' and t1 != 'note':
                        if t2 == 'billion':
                            gdp_exch = t1
                        elif t2 == 'million':
                            gdp_exch = float(t1) / 1000.0
                        elif t2 == 'trillion':
                            gdp_exch = float(t1) * 1000.0
                elif (cat == 'GDP - per capita (PPP):'):
                    if gdp_percap == 0:
                        t1 = clean(abc[0])
                        if t1 != 'country' and t1 != 'note:':
                            gdp_percap = t1
                elif (cat == 'Agriculture - products:'):
                    for l in range(0,labc):
                        t1 = clean(abc[l])
                        agriculture.append(t1)
                elif (cat == 'Industries:'):
                    abc = cur.get_text().replace(';',',').split(',')
                    labc = len(abc)
                    for l in range(0,labc):
                        t1 = clean(abc[l])
                        industries.append(t1)
                elif (cat == 'Industrial production growth rate:'):
                    t1 = clean(abc[0])
                    if ind_growth == 0:
                        ind_growth = t1
                elif (cat == 'Unemployment rate:'):
                    t1 = clean(abc[0])
                    if unemploy == 0:
                        unemploy = t1
                elif (cat == 'Population below poverty line:'):
                    t1 = clean(abc[0])
                    if poverty == 0:
                        poverty = t1
                elif (cat == 'Exports:'):
                    if exports == 0:
                        t1 = clean(abc[0])
                        t2 = clean(abc[1])
                        if t1 != 'country' and t1 != 'note':
                            if t2 == 'billion':
                                exports = t1
                            elif t2 == 'million':
                                exports = float(t1) / 1000.0
                            elif t2 == 'trillion':
                                exports = float(t1) * 1000.0
                elif (cat == 'Imports:'):
                    if imports == 0:
                        t1 = clean(abc[0])
                        t2 = clean(abc[1])
                        if t1 != 'country' and t1 != 'note':
                            if t2 == 'billion':
                                imports = t1
                            elif t2 == 'million':
                                imports = float(t1) / 1000.0
                            elif t2 == 'trillion':
                                imports = float(t1) * 1000.0
                elif (cat == 'Electricity - production:'):
                    if elec_prod == 0:
                        t1 = clean(abc[0])
                        t2 = clean(abc[1])
                        if t1 != 'country' and t1 != 'note':
                            if t2 == 'billion':
                                elec_prod = t1
                            elif t2 == 'million':
                                elec_prod = float(t1) / 1000.0
                            elif t2 == 'trillion':
                                elec_prod = float(t1) * 1000.0
                elif (cat == 'Electricity - from fossil fuels:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        elec_ff = t1
                elif (cat == 'Crude oil - production:'):
                    if oil_prod == 0:
                        t1 = clean(abc[0])
                        t2 = clean(abc[1])
                        if t1 != 'country' and t1 != 'note':
                            if t2 == 'million':
                                oil_prod = float(t1) * 1000000.0
                            else:
                                oil_prod = t1
                elif (cat == 'Crude oil - exports:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        oil_exp = t1
                elif (cat == 'Refined petroleum products - production:'):
                    if ref_pet_prod == 0:
                        t1 = clean(abc[0])
                        t2 = clean(abc[1])
                        if t1 != 'country' and t1 != 'note':
                            if t2 == 'million':
                                ref_pet_prod = float(t1) * 1000000.0
                            else:
                                ref_pet_prod = t1
                elif (cat == 'Refined petroleum products - exports:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        ref_pet_exp = t1
                elif (cat == 'Natural gas - production:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        nat_gas_prod = t1
                elif (cat == 'Natural gas - exports:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        nat_gas_exp = t1
                elif (cat == 'carbon dioxide emissions from consumption of energy:'):
                    t1 = clean(abc[0])
                    if t1 != 'country':
                        co2 = t1
                elif (cat == 'Internet users:'):
                    t1 = clean(abc[0])
                    if t1 == 'percent':
                        t2 = clean(abc[3])
                        internet = t2
                elif (cat == 'Military expenditures:'):
                    if mil_exp == 0:
                        t1 = clean(abc[0])
                        t2 = clean(abc[1])
                        if t1 != 'country' and t1 != 'note':
                            if t2 == 'billion':
                                mil_exp = t1
                            elif t2 == 'million':
                                mil_exp = float(t1) / 1000.0
                            elif t2 == 'trillion':
                                mil_exp = float(t1) * 1000.0
                elif (cat == 'Area:'):
                    t1 = clean(abc[0])
                    if t1 == 'total:':
                        t2 = clean(abc[1])
                        area = t2
                    elif t1 == 'water:':
                        t2 = clean(abc[1])
                        area_wat = t2
                elif (cat == 'Natural resources:'):
                    abc = cur.get_text().replace(';',',').split(',')
                    labc = len(abc)
                    for l in range(0,labc):
                        t1 = clean(abc[l])
                        resources.append(t1)
                elif (cat == 'Natural hazards:'):
                    abc = cur.get_text().replace(';',',').split(',')
                    labc = len(abc)
                    for l in range(0,labc):
                        t1 = clean(abc[l])
                        hazards.append(t1)
                elif (cat == 'Ethnic groups:'):
                    abc = cur.get_text().replace(';',',').split(',')
                    labc = len(abc)
                    for l in range(0,labc):
                        t1 = clean(abc[l])
                        if t1.split()[0][0].isupper():
                            ethnic_grps.append(t1)
                elif (cat == 'Population:'):
                    if pop == 0:
                        t1 = clean(abc[0])
                        pop = t1
                elif (cat == 'Country name:'):
                    for l in range(0,labc - 1):
                        t1 = clean(abc[l])
                        t2 = clean(abc[l+1])
                        if t1 == 'local' and t2 == 'short':
                            pass
                tmp = cur.find_next_sibling()
                if tmp == None:
                    break
                if tmp == cur:
                    break
                cur = tmp
            i += 1
    except Exception as e:
        pass
    ecow.writerow([country, exports, imports, gdp_exch, gdp_percap, oil_prod, ref_pet_prod])
    geow.writerow([country, area, area_wat, resources, hazards, agriculture])
    demw.writerow([country, pop, ethnic_grps, dep_rat_total, unemploy, lit, poverty, pop_growth])
    socw.writerow([country, net_mig, urban_pop, obesity, life_exp, fertility, internet, infant_mort])
    infw.writerow([country, mil_exp, industries, health_exp, education, ind_growth, elec_prod])
ecof.close()
geof.close()
demf.close()
socf.close()
inff.close()


# In[ ]:




# In[ ]:



