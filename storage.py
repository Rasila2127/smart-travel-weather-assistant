import json 


def save_destination(dest_dict):
    with open('data/destinations.json','r',encoding='utf-8') as file:
        json_data=json.load(file)

        for saved_destination in json_data:
            if saved_destination["country"]==dest_dict["country"]:
                return False
            
    json_data.append(dest_dict)

    with open('data/destinations.json','w',encoding='utf-8') as file:
        json.dump(json_data,file,indent=4,ensure_ascii=False)
        return True

def saved_destinations():
    with open('data/destinations.json','r',encoding='utf-8') as file:
        json_data=json.load(file)

    return json_data

def updated_json(saved):
    with open('data/destinations.json','w',encoding='utf-8') as file:
        json.dump(saved,file,indent=4,ensure_ascii=False)