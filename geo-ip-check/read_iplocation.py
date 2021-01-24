import json
from sys import argv
import os
import connect_iplocation as con_iploc
import iphelp
import time

start_time = time.time()

def display(ip_address, apiKey) :
    net_ip = iphelp.find_net(ip_address)
    try:
        directory = './cache/'
        filename = 'iplocation_'+str(net_ip)+'.json'
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as f:
            ip_json=f.read()

        ip_addr = json.loads(ip_json)
#        print(json.dumps(ip_addr,indent=2))
        geo_info = {'database':'ip2location.com', 'code': ip_addr["country_code"], 'country': ip_addr["country_name"], 'region' : ip_addr["region_name"],
                   'city': ip_addr["city_name"], 'company': '', 'isp': ip_addr["isp"], 'latitude' : ip_addr["latitude"], 'longitude' : ip_addr["longitude"]}

        return (geo_info)

    except IOError:
        ip_addr = con_iploc.connect_api(ip_address, apiKey)
        geo_info = {'database':'ip2location.com', 'code': ip_addr["country_code"], 'country': ip_addr["country_name"], 'region' : ip_addr["region_name"],
                   'city': ip_addr["city_name"], 'company': '', 'isp': ip_addr["isp"], 'latitude' : ip_addr["latitude"], 'longitude' : ip_addr["longitude"]}
        #        print(json.dumps(ip_addr, indent=2))

        return (geo_info)

if __name__ == "__main__" :
    arg_ip = argv[1]
    apiKey= argv[2]
    my_ip = iphelp.ip_check(arg_ip)
    ip_addr = display(my_ip, apiKey)

    print(f'''IP address :  {my_ip}
Database : {ip_addr["database"]}
Code : {ip_addr["code"]}
Country :  {ip_addr["country"]}
Region : {ip_addr["region"]}
City : {ip_addr["city"]}
ISP: {ip_addr["isp"]}
Geolocation: {ip_addr["latitude"]}, {ip_addr["longitude"]}
    '''
    )

    print("--- %s seconds ---" % (time.time() - start_time))