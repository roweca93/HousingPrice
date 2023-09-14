'''
#This algorithm accepts a directory of HTML files, a list of initial keywords, and a list of selected house price predictor variables and WRITES the gathered data points to
    a CSV txt file data table so the data is in a universally usable format and saved for later use for faster access. THEN DOES ANALYSIS?
#Selected House Price Predictor Variables = ['Address', 'County', 'Price', 'Beds', 'Baths' , 'Garage', 'Pool', 'Sqft', 'Lot_Sqft', 'Stories','Year Built','Cooling', 'Heating']
I) def HTML_DATA_EXTRACT(file, init_keywords)| return (main_extract)
    #Extract data containing substrings form HTML file
    #This function's inputs are an HTML file and a set of manually selected unique keywords found by using the Inspect Element and the Find tool
        The unique keywords identify the 'starting points' of  the substrings that contain the data needed for the selected house price predictor variables.
        init_keywords = ['LDPHomeFactsstyles__H1-sc-11rfkby-3', 'LDPListPricestyles__StyledPrice-sc-1m24xh0-1 jyBxDQ','"description":{']
II) def Clean_Data(main_extract, features)| return(file_data_list)
    #clean/process raw_data extract
III) def WRITE_CSV...
    #append data_row to data CSV txt file
IV) DATA ANALYSIS?
'''
#I)
def INIT_HTML_EXTRACT(file_location, init_keywords):
    raw_data = []
    raw_data.append(address)
    raw_data.append(county)
    with open(file_location,encoding="utf-8") as f:
        text = f.readlines()
        for line in text[1:]: #avoids finding < at first line of document
            if line[0] == '<':
                #print(line)
                for keyword in init_keywords:
                    #Price
                    if keyword == '"list_price":':
                        init_start_pos = line.find(keyword)
                        temp_string = line[init_start_pos:]
                        term_start_pos = temp_string.find(':')
                        end_pos = temp_string.find(',')
                        a = temp_string[term_start_pos + 1:end_pos]
                        a = str(a)
                        raw_data.append(a)
                    #BED, BATH, GARAGE, Pool, SQFT, LOT_SQFT, STORIES, YEAR BUILT
                    elif keyword == '":null,"description":{"b': #some list year built elsewhere maybe sqft too
                        pred_vars = ['"beds"','"baths_consolidated"','"garage"', '"pool"','"sqft"', "lot_sqft", "stories"] #lot_sqft, pool, etc there but null values
                        init_start_pos = line.find(keyword)
                        temp_string = line[init_start_pos:init_start_pos+800]
                        for predictor in pred_vars:
                            pred_start_pos = temp_string.find(predictor)
                            if pred_start_pos <0:
                                raw_data.append('Missing')
                            else:
                                pred_start_pos = temp_string.find(predictor)
                                temp_string2 = temp_string[pred_start_pos:]
                                term_start_pos = temp_string2.find(':')
                                end_pos = temp_string2.find(',')
                                raw_data.append(temp_string2[term_start_pos + 1:end_pos])
                    elif keyword == '<span aria-hidden="false">Year built</span>':
                        init_start_pos = line.find(keyword)
                        if init_start_pos == -1:
                            #Build Complete</span></div><div class="base__StyledType-rui__sc-108xfm0-0 bHKrcK">Dec 2023<
                            init_start_pos = line.find('Build Complete')
                            temp_string = line[init_start_pos:init_start_pos + 800]
                            temp_start_pos = temp_string.find('bHKrcK"')
                            temp_string2 = temp_string[temp_start_pos:temp_start_pos + 32]
                            print(temp_string2)
                            term_start_pos = temp_string2.find('>')
                            end_pos = temp_string2.find('<')
                            raw_data.append(temp_string2[term_start_pos + 1:end_pos])
                        else:
                            temp_string = line[init_start_pos:init_start_pos+800]
                            temp_start_pos = temp_string.find('gMZrrg"')
                            temp_string2 = temp_string[temp_start_pos:temp_start_pos+32]
                            print(temp_string2)
                            term_start_pos = temp_string2.find('>')
                            end_pos = temp_string2.find('<')
                            raw_data.append(temp_string2[term_start_pos + 1:end_pos])
                    else:
                        break
        next
        return (raw_data)
#II)
def Clean_Data(raw_data, features):
    column_names = ['Address','County', 'Price', 'Beds', 'Baths', 'Garage', 'Pool', 'Sqft', 'Lot_Sqft', 'Stories','Year Built']
    data_row = []
    for i in range(0,len(column_names)):
        t = (column_names[i],raw_data[i])
        if t[1] == 'null':
            if t[0] == 'Pool':
                t = list(t)
                t[1] = 'No'
                t = tuple(t)
            else:
                t = list(t)
                t[1] = 'Missing'
                t = tuple(t)
        else:
            next
        data_row.append(t)
    data_row[2] = list(data_row[2])
    data_row[2][1] = data_row[2][1].replace(',', '')
    data_row[2][1] = data_row[2][1].replace('$', '')
    return(data_row)
#III)

import os
directory = 'C:/Users/Chris/Desktop/VirginiaHousingRawDataHTML_NEW/'
directory2 = 'C:/Users/Chris/Desktop/HTML_DATA/650_850/' #need to debug some for variance in webpage coding cuz erros baths--sqft etc
#directory_list = []
i=1
for html_file in os.listdir(directory2):
    file_location = [directory2, html_file]
    file_location = ''.join(file_location)
    print(file_location)
    geo_location = html_file
    geo_location = geo_location.split(',')
    address = geo_location[0]
    county = geo_location[1]
    init_keywords = ['"list_price":', '":null,"description":{"b', '<span aria-hidden="false">Year built</span>']
    feature_keywords = ['Address', 'County', '"list_price":', '"beds"', '"baths_consolidated"', '"garage"', '"pool"', '"sqft"', '"lot_sqft"', '"stories"', 'Year Built']
    raw_data = INIT_HTML_EXTRACT(file_location, init_keywords)
    print(raw_data)
    data_row = Clean_Data(raw_data, feature_keywords)
    print(i,data_row) #need to categorize for county better maybe transform county to region lvl, nova, rva, etc
    i +=1

