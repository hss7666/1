import requests, json, time, threading
import pyfiglet
from colorama import Fore, init
# warna
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE
bl = Fore.BLACK
print(f"{yellow}--------------------------------------------------------------------------------")
print(f"{red}███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█ ")
print(f"{red}████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█ ")
print(f"{red}███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ ")
print(f"{red}████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█  ")
print(f"{red}███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█ ")
print(f"{red}████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█ ")
print(f"███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ ")
print(f"████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ ")
print(f"███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ ")
print(f"█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ ")
print(f"█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ ")
print(f"████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██ ")
print(f"█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██ ")
print(f"█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███ ")
print(f"██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███ ")
print(f"███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████ ")
print(f"███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████ ")
print(f"████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████ ")
print(f"█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████ ")
print(f"██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████ ")
print(f"███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████ ")
print(f"██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████ ")
print(f"███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████")
print(f"{yellow}Tools Created By dT17Corp")
print(f"{green}Credit : @ig : Donitata1717")
print(f"{red}Script Premium {green}Silakan dm ig@donitata1717 atau wa 085156776974")
print(f"{yellow}200k/detik {red}300Rb")
print(f"{yellow}500k/detik {red}350Rb")
print(f"{yellow}1jt/detik {red}450rb")
print(f"{yellow}1,7jt/detik {red}500rb")
print(f"{yellow}5jt/detik {red}650rb")
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '157','Host': '4ae9.playfabapi.com'}

def create_mission():
	try:
		data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["MLG","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
		response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
		js = json.loads(response)
		csession = js['data']['FunctionResult']['careerSession']
		return csession
	except Exception as e:
		pass
	

def skip_mission(token, rec):
		try:
			data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":rec,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
			response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
				
			js = json.loads(response)
			logs = js['data']['Logs']
			cash = logs[len(logs)-1]['Message'].split()[5]
			print(f'{green}[✅]SUCCESS|Your Money Now -> {cash}')
		except Exception as e:
			pass
			
def pass_mission():
	try:
		csession = create_mission()
		token = csession['token']
		kota = ["MLG","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]
		rec = []
		for i in range(0, len(kota)):
			passenger = csession['passenger'][i]
			source = passenger['source']
			dest = passenger['destination']
			max_passenger = passenger['amount']
			rec.append({"Key":{"sourceCity":source,"destinationCity":dest,"routePassed":[dest,source],"activityRewards":None},"Value":int(max_passenger)})
		skip_mission(token, rec)
	except Exception as e:
		pass

auth = input(f'{red}[{white}#{red}] {red}Silakan Masukkan Auth Token : {blue} ')
headers['X-Authorization'] = auth	
while True:
	pass_mission()
	time.sleep(0)
