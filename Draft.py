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
IV) DATA ANALYSIS
'''
#I) INIT_HTML_EXTRACT
def INIT_HTML_EXTRACT(file_location, init_keywords):
    raw_data = []
    raw_data.append(address)
    raw_data.append(county)
    with open(file_location,encoding="utf-8") as f:
        text = f.readlines()
        for line in text[1:]:
            if line[0] == '<':
                for keyword in init_keywords:
                    #Price
                    if keyword == '"list_price":':
                        init_start_pos = line.find(keyword)
                        temp_string = line[init_start_pos:]
                        term_start_pos = temp_string.find(':')
                        end_pos = temp_string.find(',')
                        raw_data.append(temp_string[term_start_pos + 1:end_pos])
                    #BED, BATH, GARAGE, Pool, SQFT, LOT_SQFT, STORIES, YEAR BUILT
                    elif keyword == '":null,"description":{"b':
                        pred_vars = ['"beds"','"baths_consolidated"','"garage"', '"pool"','"sqft"', "lot_sqft", "stories"]
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
                    #Year Built
                    elif keyword == '<span aria-hidden="false">Year built</span>':
                        init_start_pos = line.find(keyword)
                        if init_start_pos == -1:
                            init_start_pos = line.find('Build Complete')
                            if init_start_pos == -1:
                                raw_data.append('Missing')
                            else:
                                temp_string = line[init_start_pos:init_start_pos + 800]
                                temp_start_pos = temp_string.find('bHKrcK"')
                                temp_string2 = temp_string[temp_start_pos:temp_start_pos + 32]
                                term_start_pos = temp_string2.find('>')
                                end_pos = temp_string2.find('<')
                                raw_data.append(temp_string2[term_start_pos + 1:end_pos])
                        else:
                            temp_string = line[init_start_pos:init_start_pos+800]
                            temp_start_pos = temp_string.find('gMZrrg"')
                            temp_string2 = temp_string[temp_start_pos:temp_start_pos+32]
                            term_start_pos = temp_string2.find('>')
                            end_pos = temp_string2.find('<')
                            raw_data.append(temp_string2[term_start_pos + 1:end_pos])
                    else:
                        break
        next
        return (raw_data)
#II) Clean_Data
def Clean_Data(raw_data, column_names):
    data_row = []
    remove_chars = [',', '$', '"', '+', 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    float_columns = ['Price','Beds', 'Baths', 'Garage','Sqft', 'Lot_Sqft', 'Stories','Year Built']
    for i in range(0,len(column_names)):
        t = (column_names[i],raw_data[i])
        t= list(t)
        if t[1] == 'null':
            if t[0] == 'Pool':
                t[1] = 'No'
            else:
                t[1] = 'Missing'
        elif t[1] == '':
            t[1] = 'Missing'
        for char in remove_chars:
             t[1] = t[1].replace(char,"")
        if t[0] in float_columns:
            if t[1] == 'Missing':
                next
            else:
                t[1] = float(t[1])
        else:
            next
        data_row.append(t)
    data_row = list(data_row)
    return(data_row)

import os
column_names = ['Address', 'County', 'Price', 'Beds', 'Baths', 'Garage', 'Pool', 'Sqft', 'Lot_Sqft', 'Stories','Year Built']
textFilePath = "C:/Users/Chris/Desktop//test.txt"
with open(textFilePath, 'w') as f:
    col_row = str(column_names)
    f.write(col_row)
    f.write('\n')
    f.close()
directory = 'C:/Users/Chris/Desktop/HTML_DATA/'
for folder in os.listdir(directory):
    temp_directory = [directory,folder,'/']
    temp_directory = ''.join(temp_directory)
    for html_file in os.listdir(temp_directory):
        file_location = [temp_directory, html_file]
        file_location = ''.join(file_location)
        geo_location = html_file
        geo_location = geo_location.split(',')
        address = geo_location[0]
        county = geo_location[1]
        init_keywords = ['"list_price":', '":null,"description":{"b', '<span aria-hidden="false">Year built</span>']
        raw_data = INIT_HTML_EXTRACT(file_location, init_keywords)
        data_row = Clean_Data(raw_data, column_names)
        #print(data_row)
        with open(textFilePath, 'a') as f:
            temp_string = ''
            for data in data_row:
                temp_string = temp_string + (str(data[1])) + ','
            temp_string = temp_string.rstrip(',')
            print(temp_string)
            f.write(temp_string)
            f.write('\n')
            f.close()


