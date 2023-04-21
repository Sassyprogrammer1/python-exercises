import json

# Load JSON data from file

uni_name = ''
new_file_name = 'c_'+uni_name
with open(f'{uni_name}.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# print(data)
# Access the "minor" array inside the "courses" object


for value in data:
    uni_name = value
    
minor_array = data[uni_name]['courses']['minor']

# print(minor_array)
# Loop through the array and access each element


new_objects = []
for element in minor_array:
    # print(element)
    if 'applicationDeadline' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] = 'N/A'
        

    if 'requirements' in element:

        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements']=  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements'] = 'N/A'
   
    # if 'chineseHighSchool' in element['admissionInfo']['internationalHighSchool']:
    
    
    if 'applicationDeadline' in element:

        #applicationDeadline
        element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['applicationDeadline'])

    else:
        element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['applicationDeadline'] = 'N/A'


        #requirements
    if 'requirements' in element:

        element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['requirements'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['requirements'])
    else:
        element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['requirements'] = 'N/A'
        
    
    #requirements


    # Create a new object and add key-value pairs from "courses" and "courses.minor"
    new_obj = {}

    new_obj['university_name'] = data[uni_name]['name']
    new_obj['acronym'] = data[uni_name]['acronym']
    new_obj['world_ranking'] = data[uni_name]['worldRanking']
    new_obj['address'] = data[uni_name]['address']
    new_obj['province'] = data[uni_name]['province']
    new_obj['country_code'] = data[uni_name]['countryCode']
    new_obj['geotag'] = data[uni_name]['geotag']
    new_obj['google_map_url'] = data[uni_name]['googleMapURL']
    new_obj['admission_email'] = data[uni_name]['admissionEmail']
    new_obj['phone_number'] = data[uni_name]['phoneNumber']
    new_obj['website_url'] = data[uni_name]['websiteURL']
    new_obj['lang_req'] = json.dumps(data[uni_name]['langRequirement'])
    new_obj['course_name'] = element['courseName']
    new_obj['faculty'] = element['faculty']
    new_obj['program_length'] = element['programLength']
    new_obj['education_level'] = element['educationLevel']
    new_obj['introduction'] = element['introduction']
    new_obj['url'] = element['url']
    new_obj['work_experience'] = element['workExperience']
    new_obj['ib_high_school_admission_info'] = element['admissionInfo']['internationalHighSchool']['chineseHighSchool']
    new_obj['chinese_high_school_admission_info'] = element['admissionInfo']['internationalHighSchool']['chineseHighSchool']

    
    if 'importantTag' in element:
      new_obj['importantTag'] = element['importantTag']
    else:
    #   new_obj['importantTag'] = 'n/a'
      continue 

    # new_obj['important_tag'] = element['importantTag']
    # print(element['importantTag'])

    # new_obj['ib_high_school_admission_info']
    # Add the new object to the list
    new_objects.append(new_obj)
    

# Print the list of new objects
print(new_objects)



with open(f'{new_file_name}.json', 'w') as f:
    json.dump(new_objects, f)
