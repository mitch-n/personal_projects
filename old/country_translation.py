
countries = "United States, Australia, Estados Unidos de América, New Zealand, Deutschland, Chile, Argentina, Finland, Guatemala, Philippines, Polynesie Française, Tahiti, República Dominicana, Canada, 日本, Samoa, 한국, Nouvelle Zélande, Indonesia, Tonga, 香港, Fiji, 中國, 일본, Guam, ประเทศไทย, 台灣, Perú, India, South Africa, France, Ukraine, 미합중국, ｱﾒﾘｶ合衆国, United Kingdom, Czech Republic, Hong Kong, España, Germany, Nederland, Kenya, Ghana, Nigeria, Suisse, Italia, Brasil, Uruguay, México, Reino Unido, Peru, Venezuela, Ecuador, Cabo Verde, Bolivia, Honduras, Japan, Jordan, Alemanha, Puerto Rico, Colombia, Costa Rica, Nicaragua, Paraguay, Armenia, 斯里蘭卡, Niue, Portugal, Hungary, Italy, Denmark, Cote d'Ivoire, Haití, El Salvador, Saint Kitts and Nevis, Trinidad and Tobago, Papua New Guinea, Brazil, Dominican Republic, Panamá, កម្ពុជា, Bulgaria, Lithuania, Kiribati, Россия, សហរដ្ឋ​អាមេរិក, Vietnam, Mexico, French Polynesia, Austria, США, Allemagne, Jamaica, Virgin Islands, République Démocratique Congo, Alemania, Switzerland, Democratic Republic of Congo, Marshall Islands, Sierra Leone, Aruba, Estonia, Vanuatu, Беларусь, Uganda, South Korea, Монгол, Latvia, Sweden, Micronesia, Ireland, Guyana, Haïti, Etats-Unis, Romania, Slovenia, Mozambique, Tanzanie, Estados Unidos, Albania, Poland, Norway, Serbia, Croatia, Zimbabwe, Rwanda, Russia, Liberia, Macedonia, 印尼, Belgium, République du Congo, Ethiopia, Malta, Bosnia and Herzegovina, Belize, Singapore, United Arab Emirates, Israel, Thailand, ហុងកុង, China, 韓国, ไต้หวัน, Madagascar, Cambodia, Malaysia, Canadá, Northern Mariana Islands, Netherlands, Turks and Caicos Islands, Slovakia, Belgique, American Samoa, Spain, Barbados, Iceland, Qatar, Egypt, Cyprus, Bermuda, Panama, Cameroon, Saint Lucia, Taiwan, Ελλάς, Cook Islands, Mauritius, Republic of Congo, Grenada, Eswatini, Bahamas, Kuwait, Tuvalu, Montenegro, Senegal, Kosovo, Bahrain, Angola, België, Zambia, Georgia, Dominica, Turkey, Tanzania, Cape Verde, Verenigde Staten, 美國, Belice, Benin, ドイツ, Botswana, Luxembourg, Cayman Islands, Suriname, Moçambique, Afrique du Sud, Việt Nam, Solomon Islands, Казахстан, Cuba, Togo, Pakistan, Malawi, 澳門, Saint Vincent and Grenadines, Guinée Française, Jersey, Nouvelle Calédonie, Guadeloupe, Αλβανία, Guadeloupe, Namibia, АНУ, Maurice, Oman, Uruguai, Sint Maarten, ﾐｸﾛﾈｼｱ, Antigua and Barbuda, Moldova, Réunion, Haiti, Sudáfrica, Lebanon, Republique Dominicaine, Isle of Man, Cameroun, Sierra Léone, Trinidad y Tobago, ฮ่องกง, Macau, Lesotho, 越南, Morocco, Campuchia, Duitsland, Guernsey, Burundi, Martinique, Sri Lanka, Mongolia, Mali, Virgin Islands, British, Curacao, Holanda, Gabon, Falkland Islands, The Gambia, Palau, 菲律賓, Greece, Japão, Nauru, Guinea, Sénégal, République Afrique Centrale, Bosnia Hercegovina, Ouganda".encode("utf-16").decode("utf-16").split(", ")
#countries=["ฮ่องกง"]
#countries = "Samoa, 한국, Nouvelle Zélande, Indonesia, Tonga, 香港, Fiji, 中國, 일본, Guam, ประเทศไทย, 台灣, Perú, កម្ពុជា, Bulgaria, Lithuania, Kiribati, Россия, République Démocratique Congo, Alemania, Ouganda".encode("utf-16").decode("utf-16").split(", ")

import requests, time

s = requests.Session()
s.headers = {"Authorization":"DeepL-Auth-Key 22e5c907-31ec-75d3-163b-97990d898cdd:fx"}

url = "https://api-free.deepl.com/v2/translate"

for country in countries:
	#print(country)
	data = {"text": country, "target_lang":"EN"}
	response = s.post(url, data=data)
	#print(response,response.text)
	translation = response.json()["translations"][0]["text"]
	language = response.json()["translations"][0]["detected_source_language"]
	if  not (country.lower() == translation.lower() and language == "EN"):
		print(country, ":", translation)
	#input()
	time.sleep(.5)
