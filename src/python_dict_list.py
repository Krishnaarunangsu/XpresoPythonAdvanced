import pprint
import json

json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

json_object = json.loads(json_data)

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)
dict1 ={}
dict1.append({"ID":10,"Name":"Pankaj","Role":"CEO"})
dict1.append({"ID":20,"Name":"David Lee","Role":"Editor"})


json_formatted_str = json.dumps(dict1, indent=2)
print('***************************************************')
print(json_formatted_str)

