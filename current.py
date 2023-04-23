import json

# Load JSON data from file

uni_name = 'uni_of_western_aus'
new_file_name = 'c_'+uni_name
with open(f'F:\\PythonProjects\\map_chart\\z_converted_unis\\aus\\aus_json\\{uni_name}.json', 'r', encoding='utf-8') as f:
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
    if 'admissionInfo' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo'] = {}

    if 'internationalHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool'] = {}

    if 'IBHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool'] = {}


    if 'applicationDeadline' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] = 'N/A' 
        

    if 'internationalHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool'] = {}

    if 'IBHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements']=  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool'] = {}

    if 'requirements' in element:

        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements']=  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['requirements'] = 'N/A'

    



   
    # if 'chineseHighSchool' in element['admissionInfo']['internationalHighSchool']:

    
    if 'chineseHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['chineseHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool']['chineseHighSchool'] = {}


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
      new_obj['important_tags'] = element['importantTag']
    else:
    #   new_obj['importantTag'] = 'n/a'
      continue 

    # new_obj['important_tag'] = element['importantTag']
    # print(element['importantTag'])

    # new_obj['ib_high_school_admission_info']
    # Add the new object to the list
    new_objects.append(new_obj)


# Print the list of new objects
# print(new_objects)

# new_obj2 = []
# for element in new_objects:
#     # print(type(element))
#     # print(element['importantTag'])
#     if isinstance(element['importantTags'], list):
#         # print(element)
        
#         for x in element['importantTags']:
#             # print(element['importantTag'][x])
#             # print(x)
       
#             new_obj = {}

#             new_obj['university_name'] = element['university_name']
#             new_obj['acronym'] = element['acronym']
#             new_obj['world_ranking'] = element['world_ranking']
#             new_obj['address'] = element['address']
#             new_obj['province'] = element['province']
#             new_obj['country_code'] = element['country_code']
#             new_obj['geotag'] = element['geotag']
#             new_obj['google_map_url'] = element['google_map_url']
#             new_obj['admission_email'] = element['admission_email']
#             new_obj['phone_number'] = element['phone_number']
#             new_obj['website_url'] = element['website_url']
#             new_obj['lang_req'] = json.dumps(element['lang_req'])
#             new_obj['course_name'] = element['course_name']
#             new_obj['faculty'] = element['faculty']
#             new_obj['program_length'] = element['program_length']
#             new_obj['education_level'] = element['education_level']
#             new_obj['important_tag'] = x
#             new_obj['introduction'] = element['introduction']
#             new_obj['important_tags'] = element['important_tags']
#             new_obj['url'] = element['url']
#             new_obj['work_experience'] = element['work_experience']
#             new_obj['ib_high_school_admission_info'] = element['ib_high_school_admission_info']
#             new_obj['chinese_high_school_admission_info'] = element['chinese_high_school_admission_info']
#             new_obj2.append(new_obj)
#     else:
#         element['importantTag'] = element['important_tags']
#         new_obj2.append(element)
        
        

# print(new_obj2)
    








with open(f'F:\\PythonProjects\\map_chart\\z_converted_unis\\aus\\converted_json\\{new_file_name}.json', 'w') as f:
    json.dump(new_objects, f)
