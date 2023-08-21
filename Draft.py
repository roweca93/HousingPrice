#File_Director
"""
import os

directory = 'C:/Users/Chris/Desktop/VirginiaHousingRawDataHTML/'
directory_list = []
for filename in os.listdir(directory):
    directory_list.append(filename)
    #with open(os.path.join(directory, filename)) as f:
    #print(f.read())
print(directory_list)
"""
##arrays are faster than lists so maybe convert to arrays in initial search and move from there
#Raw_HTML_Extractor
def Raw_HTML_Extractor(file, init_keywords):
    main_extract = []
    with open(file) as f:
        text = f.readlines()
        num_lines = len(text)
        for keyword in init_keywords:
            pat_len = len(keyword)
            line_num = 0
            for line in text:
                line_len = len(line)
                if line[0] == '<':
                    for i1 in range(0, line_len - pat_len + 1):
                        match_count = 0
                        while match_count < pat_len:
                            if line[i1 + match_count] == keyword[match_count]:
                                match_count += 1
                            else:
                                break
                        else: #match_count !< pat_len
                            if keyword == 'Price__Component':
                                temp_string = line[i1:i1+60]
                                start1 = temp_string.find('$')
                                end1 = temp_string.find('<')
                                main_extract.append(temp_string[0:end1])
                            else:
                                end2 = 0
                                for i2 in range(i1, line_len):
                                    while (end2 < 1):
                                        if line[i2] == '}':
                                            end2 += 1
                                            main_extract.append(line[i1:i2 + 1])
                                        else:
                                            break
                line_num +=1
    main_extract = main_extract[1:] #this gets rid of the repeat (x2) for 'address":{"line":'
    return(main_extract)
init_keywords = ['address":{"line":', 'Price__Component','"description":{','"category":']
raw_data = Raw_HTML_Extractor('C:/Users/Chris/Desktop/VirginiaHousingRawDataHTML/6420 Orchard Rd, New Kent, VA 23124 _ realtor.com®.html', init_keywords)
print(raw_data)


#Main_Extract_Processor
def Main_Extract_Processor(main_extract, features):
    file_data_list = []
    main_extract_str=''.join(main_extract)
    for feature in features:
        loc = main_extract_str.find(feature)
        main_extract_str_temp = main_extract_str[loc + len(feature) + 1:loc + len(feature) + 100]
        main_extract_str_temp = main_extract_str_temp.replace('"', "")
        if feature == 'Price__Component':
            start_pos = main_extract_str_temp.find('$')
            end_pos = (main_extract_str_temp.find('descript'))
            data_point = (feature, main_extract_str_temp[start_pos:end_pos])
            file_data_list.append(data_point)
        else:
            end_pos = main_extract_str_temp.find(',')
            data_point = (feature, main_extract_str_temp[0:end_pos])
            file_data_list.append(data_point)
    return(file_data_list)
feature_keywords = ['address":{"line":', 'Price__Component', '"baths_consolidated"', '"beds"', '"garage"', '"pool"', '"sqft"', '"lot_sqft"','"stories"', '"year_built"', "Cooling Features", "Heating Features", '"County']
results = Main_Extract_Processor(raw_data, feature_keywords)
print(results)

#Clean_Export
def Clean_Export(results):
    var_name_list = ['Address','Price','Baths', 'Beds', 'Garage','Pool','Sqft','Lot_Sqft', 'Stories','Year Built',
                         'Cooling','Heating', 'County']
    clean_dat_list = []
    for i in range(0, len(var_name_list)):
        t = (var_name_list[i], results[i][1])
        clean_dat_list.append(t)
    textFilePath = "C:/Users/Chris/Desktop//test.txt"
    # create new text file code
    # with open(textFilePath, 'w') as f:
    # for result in results:
    # f.write(result)
    #eventually, text file will have lines = # samples taken and each line will be the clean_dat_list. for storage of data
    return(clean_dat_list)
clean_results = Clean_Export(results)
print(clean_results)


#def Create Pandas dataset for Housing Price Model because it performs faster than lists
    #after saving as text for data. use either the txt file or clean_results lines to generate pandas frame for calcula.

#def run calculations on pandas dataset and optimize

#def create visualization of model
















"""
 streetAddress_find = 0 
                            elif keyword == 'streetAddress':
                                while (streetAddress_find <1):
                                    
                                #temp_string =
"""
