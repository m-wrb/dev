import yaml
import json
with open('network_config.yml','r') as file:
    network_config = yaml.safe_load(file)
print(network_config)

###
network_data={
    'switch':'Switch1',
    'ports':[
        {'name':'FastEth0/1','vlan':'10'},
        {'name':'FastEth0/2','vlan':'20'}
    ]
}
with open('new_network_config.json','w') as file:
    json.dump(network_data,file,indent=4)

###
def read_and_modify_router_config(file_path):
    with open(file_path,'r') as file:
        try:
            data=yaml.safe_load(file)
            if data['interfaces']:
                data['interfaces'][1]['ip']='500.10.10.1'
            return data
        except yaml.YAMLError as exc:
            print(f'blad {exc}')
def write_yaml(file_path,data):
    with open(file_path,'w') as file:
        yaml.dump(data,file,sort_keys=False)

modified_config=read_and_modify_router_config('network_config.yml')
write_yaml('modified_router_config.yml',modified_config)