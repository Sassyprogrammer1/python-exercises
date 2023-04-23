import json
import requests
url = 'https://i8um1uxi40.execute-api.us-east-2.amazonaws.com/dev/api/v1/university/create'
# Load JSON data from file

#Input uni name
"""All json files in  'aus,can & nz' folders are named 1.json, 2.json... 
"""

uni_name = '1'
new_file_name = 'c_'+uni_name

# path to read file
"""
path of uni should be uni-json + either aus,can or nz. 
"""
with open(f'/uni-json/aus/{uni_name}.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Access the "minor" array inside the "courses" object
for value in data:
    uni_name = value
    
minor_array = data[uni_name]['courses']['minor']

# Loop through the array and access each element
new_objects = []
for element in minor_array:

    if 'admissionInfo' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo'] = {}


    if 'internationalHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool'] = {}


    if 'IBHighSchool' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo'])
    else:
         element['admissionInfo']['internationalHighSchool']['IBHighSchool'] = {}


    if 'applicationDeadline' in element:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] =  json.dumps(element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'])
    else:
        element['admissionInfo']['internationalHighSchool']['IBHighSchool']['applicationDeadline'] = 'N/A'


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
      
      response = requests.post(url, data=new_obj)
      # Print the response content
      print(response.content)
    else:
      continue 
    # Add the new object to the list
    new_objects.append(new_obj)

#path to save file
    """path should be uni-json/converted
    """
with open(f'/uni-json/converted{new_file_name}.json', 'w') as f:
    json.dump(new_objects, f)

