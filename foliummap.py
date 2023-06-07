import folium
import matplotlib.pyplot as plt
import webbrowser

# Criar um mapa mundi
mapa_america = folium.Map(location=[10, 10], zoom_start=4)

# Adicionar marcadores para cada país e sua capital

paises_capitais_america = {
    #América do Sul
    'Argentina': {'capital': 'Buenos Aires', 'coordenadas': [-34.61, -58.38]},
    'Bolívia': {'capital': 'La Paz', 'coordenadas': [-16.49, -68.12]},
    'Brasil': {'capital': 'Brasília', 'coordenadas': [-15.78, -47.92]},
    'Chile': {'capital': 'Santiago', 'coordenadas': [-33.45, -70.66]},
    'Colômbia': {'capital': 'Bogotá', 'coordenadas': [4.60, -74.08]},
    'Equador': {'capital': 'Quito', 'coordenadas': [-0.20, -78.50]},
    'Guiana': {'capital': 'Georgetown', 'coordenadas': [6.80, -58.16]},
    'Paraguai': {'capital': 'Assunção', 'coordenadas': [-25.27, -57.64]},
    'Peru': {'capital': 'Lima', 'coordenadas': [-12.04, -77.03]},
    'Suriname': {'capital': 'Paramaribo', 'coordenadas': [5.83, -55.17]},
    'Uruguai': {'capital': 'Montevidéu', 'coordenadas': [-34.86, -56.17]},
    'Venezuela': {'capital': 'Caracas', 'coordenadas': [10.48, -66.90]},

    #América do Norte    
    'Canadá': {'capital': 'Ottawa', 'coordenadas': [45.42, -75.69]},
    'Estados Unidos': {'capital': 'Washington D.C.', 'coordenadas': [38.91, -77.04]},
    'México': {'capital': 'Cidade do México', 'coordenadas': [19.43, -99.13]},
    'Antígua e Barbuda': {'capital': 'Saint John\'s', 'coordenadas': [17.12, -61.85]},
    'Bahamas': {'capital': 'Nassau', 'coordenadas': [25.05, -77.35]},
    'Barbados': {'capital': 'Bridgetown', 'coordenadas': [13.10, -59.62]},
    'Belize': {'capital': 'Belmopan', 'coordenadas': [17.25, -88.77]},
    'Costa Rica': {'capital': 'San José', 'coordenadas': [9.93, -84.08]},
    'Cuba': {'capital': 'Havana', 'coordenadas': [23.13, -82.38]},
    'Dominica': {'capital': 'Roseau', 'coordenadas': [15.30, -61.39]},
    'República Dominicana': {'capital': 'Santo Domingo', 'coordenadas': [18.48, -69.90]},
    'El Salvador': {'capital': 'San Salvador', 'coordenadas': [13.70, -89.20]},
    'Granada': {'capital': 'Saint George\'s', 'coordenadas': [12.06, -61.75]},
    'Guatemala': {'capital': 'Cidade da Guatemala', 'coordenadas': [14.63, -90.55]},
    'Haiti': {'capital': 'Port-au-Prince', 'coordenadas': [18.54, -72.34]},
    'Honduras': {'capital': 'Tegucigalpa', 'coordenadas': [14.09, -87.22]},
    'Jamaica': {'capital': 'Kingston', 'coordenadas': [17.97, -76.79]},
    'Nicarágua': {'capital': 'Manágua', 'coordenadas': [12.13, -86.25]},
    'Panamá': {'capital': 'Cidade do Panamá', 'coordenadas': [8.97, -79.53]},
    'São Cristóvão e Neves': {'capital': 'Basseterre', 'coordenadas': [17.30, -62.72]},
    'Santa Lúcia': {'capital': 'Castries', 'coordenadas': [14.01, -60.99]},
    'São Vicente e Granadinas': {'capital': 'Kingstown', 'coordenadas': [13.16, -61.23]},
    'Trinidad e Tobago': {'capital': 'Port of Spain', 'coordenadas': [10.67, -61.51]},

    #América Central

    'Belize': {'capital': 'Belmopan', 'coordenadas': [17.25, -88.77]},
    'Costa Rica': {'capital': 'San José', 'coordenadas': [9.93, -84.08]},
    'El Salvador': {'capital': 'San Salvador', 'coordenadas': [13.70, -89.20]},
    'Guatemala': {'capital': 'Cidade da Guatemala', 'coordenadas': [14.63, -90.55]},
    'Honduras': {'capital': 'Tegucigalpa', 'coordenadas': [14.09, -87.22]},
    'Nicarágua': {'capital': 'Manágua', 'coordenadas': [12.13, -86.25]},
    'Panamá': {'capital': 'Cidade do Panamá', 'coordenadas': [8.97, -79.53]}

   
}

for pais, info in paises_capitais_america.items():
    capital = info['capital']
    coordenadas = info['coordenadas']
    folium.Marker(location=coordenadas, popup=capital).add_to(mapa_america)
    folium.Marker(location=coordenadas, icon=folium.Icon(color='green')).add_to(mapa_america)

# Mostrar o mapa
mapa_america.save('america.html')
mapa_america

# Criar um mapa mundi
mapa_asia = folium.Map(location=[10, 10], zoom_start=4)

paises_capitais_asia = {  
    
    #Ásia Setentrional (Norte)
    'Cazaquistão': {'capital': 'Nursultan', 'coordenadas': [51.17, 71.43]},
    'China': {'capital': 'Pequim', 'coordenadas': [39.91, 116.40]},
    'Coreia do Norte': {'capital': 'Pyongyang', 'coordenadas': [39.03, 125.75]},
    'Coreia do Sul': {'capital': 'Seul', 'coordenadas': [37.56, 126.97]},
    'Mongólia': {'capital': 'Ulã Bator', 'coordenadas': [47.92, 106.92]},
    'Rússia': {'capital': 'Moscou', 'coordenadas': [55.75, 37.62]},

    #Ásia Central
    'Cazaquistão': {'capital': 'Nursultan', 'coordenadas': [51.17, 71.43]},
    'Quirguistão': {'capital': 'Bisqueque', 'coordenadas': [42.87, 74.59]},
    'Tajiquistão': {'capital': 'Duxambé', 'coordenadas': [38.56, 68.77]},
    'Turcomenistão': {'capital': 'Asgabate', 'coordenadas': [37.95, 58.38]},
    'Uzbequistão': {'capital': 'Tashkent', 'coordenadas': [41.31, 69.24]}, 

    #Ásia Meridional (Sul)
    'Afeganistão': {'capital': 'Cabul', 'coordenadas': [34.53, 69.17]},
    'Bangladesh': {'capital': 'Daca', 'coordenadas': [23.81, 90.41]},
    'Bhutan': {'capital': 'Timbu', 'coordenadas': [27.47, 89.63]},
    'Índia': {'capital': 'Nova Delhi', 'coordenadas': [28.61, 77.20]},
    'Maldivas': {'capital': 'Malé', 'coordenadas': [4.18, 73.51]},
    'Nepal': {'capital': 'Catmandu', 'coordenadas': [27.70, 85.32]},
    'Paquistão': {'capital': 'Islamabad', 'coordenadas': [33.68, 73.05]},
    'Sri Lanka': {'capital': 'Colombo', 'coordenadas': [6.92, 79.86]},

    #Oriente Médio    
    'Afeganistão': {'capital': 'Cabul', 'coordenadas': [34.53, 69.17]},
    'Arábia Saudita': {'capital': 'Riade', 'coordenadas': [24.71, 46.67]},
    'Bahrain': {'capital': 'Manama', 'coordenadas': [26.23, 50.57]},
    'Chipre': {'capital': 'Nicósia', 'coordenadas': [35.17, 33.37]},
    'Emirados Árabes Unidos': {'capital': 'Abu Dhabi', 'coordenadas': [24.47, 54.37]},
    'Iêmen': {'capital': 'Sana', 'coordenadas': [15.35, 44.21]},
    'Irã': {'capital': 'Teerã', 'coordenadas': [35.70, 51.41]},
    'Iraque': {'capital': 'Bagdá', 'coordenadas': [33.33, 44.44]},
    'Israel': {'capital': 'Jerusalém', 'coordenadas': [31.78, 35.22]},
    'Jordânia': {'capital': 'Amã', 'coordenadas': [31.95, 35.93]},
    'Kuwait': {'capital': 'Cidade do Kuwait', 'coordenadas': [29.38, 47.97]},
    'Líbano': {'capital': 'Beirute', 'coordenadas': [33.89, 35.50]},
    'Omã': {'capital': 'Mascate', 'coordenadas': [23.61, 58.59]},
    'Palestina': {'capital': 'Jerusalém Oriental', 'coordenadas': [31.78, 35.22]},
    'Qatar': {'capital': 'Doha', 'coordenadas': [25.28, 51.53]},
    'Síria': {'capital': 'Damasco', 'coordenadas': [33.51, 36.29]},
    'Turquia': {'capital': 'Ancara', 'coordenadas': [39.93, 32.86]},

    #Extremo Oriente    
    'China': {'capital': 'Pequim', 'coordenadas': [39.90, 116.40]},
    'Coreia do Norte': {'capital': 'Pyongyang', 'coordenadas': [39.02, 125.75]},
    'Coreia do Sul': {'capital': 'Seul', 'coordenadas': [37.57, 126.98]},
    'Japão': {'capital': 'Tóquio', 'coordenadas': [35.68, 139.77]},
    'Mongólia': {'capital': 'Ulã Bator', 'coordenadas': [47.91, 106.92]},
    'Taiwan': {'capital': 'Taipé', 'coordenadas': [25.03, 121.56]},
    'Hong Kong': {'capital': 'Hong Kong', 'coordenadas': [22.31, 114.16]},
    'Macau': {'capital': 'Macau', 'coordenadas': [22.20, 113.55]},


    #Sudeste Asiático
    'Brunei': {'capital': 'Bandar Seri Begawan', 'coordenadas': [4.89, 114.94]},
    'Camboja': {'capital': 'Phnom Penh', 'coordenadas': [11.55, 104.92]},
    'Filipinas': {'capital': 'Manila', 'coordenadas': [14.60, 120.98]},
    'Indonésia': {'capital': 'Jacarta', 'coordenadas': [-6.21, 106.85]},
    'Laos': {'capital': 'Vientiane', 'coordenadas': [17.97, 102.60]},
    'Malásia': {'capital': 'Kuala Lumpur', 'coordenadas': [3.14, 101.69]},
    'Myanmar': {'capital': 'Naypyidaw', 'coordenadas': [19.76, 96.07]},
    'Singapura': {'capital': 'Singapura', 'coordenadas': [1.29, 103.85]},
    'Tailândia': {'capital': 'Bangkok', 'coordenadas': [13.75, 100.50]},
    'Timor-Leste': {'capital': 'Díli', 'coordenadas': [-8.56, 125.57]},
    'Vietnã': {'capital': 'Hanói', 'coordenadas': [21.03, 105.85]}

    
}

for pais, info in paises_capitais_asia.items():
    capital = info['capital']
    coordenadas = info['coordenadas']
    folium.Marker(location=coordenadas, popup=capital).add_to(mapa_asia)
    folium.Marker(location=coordenadas, icon=folium.Icon(color='orange')).add_to(mapa_asia)

mapa_asia.save('asia.html')
mapa_asia

# Criar um mapa mundi
mapa_europa = folium.Map(location=[10, 10], zoom_start=4)

paises_capitais_europa = {
    
   #Europa Oriental  
    'Albânia': {'capital': 'Tirana', 'coordenadas': [41.33, 19.82]},
    'Bielorrússia': {'capital': 'Minsk', 'coordenadas': [53.90, 27.57]},
    'Bósnia e Herzegovina': {'capital': 'Sarajevo', 'coordenadas': [43.85, 18.38]},
    'Bulgária': {'capital': 'Sófia', 'coordenadas': [42.70, 23.32]},
    'Croácia': {'capital': 'Zagreb', 'coordenadas': [45.81, 15.97]},
    'Eslováquia': {'capital': 'Bratislava', 'coordenadas': [48.15, 17.11]},
    'Eslovênia': {'capital': 'Liubliana', 'coordenadas': [46.06, 14.51]},
    'Estônia': {'capital': 'Tallinn', 'coordenadas': [59.44, 24.75]},
    'Hungria': {'capital': 'Budapeste', 'coordenadas': [47.50, 19.04]},
    'Letônia': {'capital': 'Riga', 'coordenadas': [56.95, 24.10]},
    'Lituânia': {'capital': 'Vilnius', 'coordenadas': [54.69, 25.28]},
    'Moldávia': {'capital': 'Chisinau', 'coordenadas': [47.02, 28.83]},
    'Polônia': {'capital': 'Varsóvia', 'coordenadas': [52.23, 21.01]},
    'República Checa': {'capital': 'Praga', 'coordenadas': [50.08, 14.44]},
    'Romênia': {'capital': 'Bucareste', 'coordenadas': [44.44, 26.10]},
    'Rússia': {'capital': 'Moscou', 'coordenadas': [55.75, 37.62]},
    'Sérvia': {'capital': 'Belgrado', 'coordenadas': [44.82, 20.46]},
    'Ucrânia': {'capital': 'Kiev', 'coordenadas': [50.45, 30.52]},

   #Europa Ocidental   
    'Alemanha': {'capital': 'Berlim', 'coordenadas': [52.52, 13.40]},
    'Áustria': {'capital': 'Viena', 'coordenadas': [48.21, 16.37]},
    'Bélgica': {'capital': 'Bruxelas', 'coordenadas': [50.85, 4.35]},
    'Dinamarca': {'capital': 'Copenhague', 'coordenadas': [55.68, 12.57]},
    'Espanha': {'capital': 'Madri', 'coordenadas': [40.42, -3.70]},
    'Finlândia': {'capital': 'Helsinque', 'coordenadas': [60.17, 24.94]},
    'França': {'capital': 'Paris', 'coordenadas': [48.85, 2.35]},
    'Grécia': {'capital': 'Atenas', 'coordenadas': [37.98, 23.73]},
    'Irlanda': {'capital': 'Dublin', 'coordenadas': [53.35, -6.26]},
    'Itália': {'capital': 'Roma', 'coordenadas': [41.90, 12.49]},
    'Luxemburgo': {'capital': 'Luxemburgo', 'coordenadas': [49.61, 6.13]},
    'Noruega': {'capital': 'Oslo', 'coordenadas': [59.91, 10.74]},
    'Países Baixos': {'capital': 'Amsterdã', 'coordenadas': [52.37, 4.90]},
    'Portugal': {'capital': 'Lisboa', 'coordenadas': [38.72, -9.14]},
    'Reino Unido': {'capital': 'Londres', 'coordenadas': [51.51, -0.13]},
    'Suécia': {'capital': 'Estocolmo', 'coordenadas': [59.33, 18.07]},
    'Suíça': {'capital': 'Berna', 'coordenadas': [46.95, 7.44]},

   #Europa Setentrional(Norte)
    'Dinamarca': {'capital': 'Copenhague', 'coordenadas': [55.68, 12.57]},
    'Finlândia': {'capital': 'Helsinque', 'coordenadas': [60.17, 24.94]},
    'Islândia': {'capital': 'Reykjavik', 'coordenadas': [64.14, -21.94]},
    'Noruega': {'capital': 'Oslo', 'coordenadas': [59.91, 10.74]},
    'Suécia': {'capital': 'Estocolmo', 'coordenadas': [59.33, 18.07]},

   #Europa Meridional (Sul)
    'Albânia': {'capital': 'Tirana', 'coordenadas': [41.33, 19.82]},
    'Bósnia e Herzegovina': {'capital': 'Sarajevo', 'coordenadas': [43.85, 18.38]},
    'Croácia': {'capital': 'Zagreb', 'coordenadas': [45.81, 15.98]},
    'Chipre': {'capital': 'Nicósia', 'coordenadas': [35.17, 33.37]},
    'Grécia': {'capital': 'Atenas', 'coordenadas': [37.98, 23.73]},
    'Itália': {'capital': 'Roma', 'coordenadas': [41.90, 12.49]},
    'Kosovo': {'capital': 'Pristina', 'coordenadas': [42.67, 21.17]},
    'Malta': {'capital': 'Valeta', 'coordenadas': [35.90, 14.51]},
    'Montenegro': {'capital': 'Podgorica', 'coordenadas': [42.43, 19.26]},
    'Portugal': {'capital': 'Lisboa', 'coordenadas': [38.72, -9.14]},
    'San Marino': {'capital': 'San Marino', 'coordenadas': [43.94, 12.45]},
    'Sérvia': {'capital': 'Belgrado', 'coordenadas': [44.82, 20.46]},
    'Eslovênia': {'capital': 'Liubliana', 'coordenadas': [46.05, 14.51]},
    'Espanha': {'capital': 'Madri', 'coordenadas': [40.42, -3.70]}    
}

for pais, info in paises_capitais_europa.items():
    capital = info['capital']
    coordenadas = info['coordenadas']
    folium.Marker(location=coordenadas, popup=capital).add_to(mapa_europa)
    folium.Marker(location=coordenadas, icon=folium.Icon(color='pink')).add_to(mapa_europa)

mapa_europa.save('europa.html')
mapa_europa

# Criar um mapa mundi
mapa_africa = folium.Map(location=[10, 10], zoom_start=4)

paises_capitais_africa = {
    #África Mediterrânea
    'Argélia': {'capital': 'Argel', 'coordenadas': [36.75, 3.04]},
    'Líbia': {'capital': 'Trípoli', 'coordenadas': [32.89, 13.19]},
    'Marrocos': {'capital': 'Rabat', 'coordenadas': [34.02, -6.83]},
    'Tunísia': {'capital': 'Túnis', 'coordenadas': [36.80, 10.18]},

    #África Subsaariana
    'África do Sul': {'capital': 'Cidade do Cabo (legislativa)', 'coordenadas': [-33.93, 18.42]},
    'Angola': {'capital': 'Luanda', 'coordenadas': [-8.83, 13.23]},
    'Benin': {'capital': 'Porto-Novo', 'coordenadas': [6.49, 2.63]},
    'Botsuana': {'capital': 'Gaborone', 'coordenadas': [-24.66, 25.91]},
    'Burkina Faso': {'capital': 'Ouagadougou', 'coordenadas': [12.37, -1.54]},
    'Burundi': {'capital': 'Bujumbura', 'coordenadas': [-3.38, 29.36]},
    'Cabo Verde': {'capital': 'Praia', 'coordenadas': [14.92, -23.51]},
    'Camarões': {'capital': 'Yaoundé', 'coordenadas': [3.87, 11.52]},
    'Chade': {'capital': "N'Djamena", 'coordenadas': [12.12, 15.05]},
    'Comores': {'capital': 'Moroni', 'coordenadas': [-11.70, 43.24]},
    'Congo-Brazzaville': {'capital': 'Brazzaville', 'coordenadas': [-4.26, 15.27]},
    'Congo-Kinshasa': {'capital': 'Quinxassa', 'coordenadas': [-4.31, 15.31]},
    'Costa do Marfim': {'capital': 'Yamoussoukro', 'coordenadas': [6.81, -5.28]},
    'Djibuti': {'capital': 'Djibuti', 'coordenadas': [11.57, 43.14]},
    'Eritreia': {'capital': 'Asmara', 'coordenadas': [15.33, 38.94]},
    'Eswatini': {'capital': 'Mbabane (administrativa)', 'coordenadas': [-26.31, 31.14]},
    'Etiópia': {'capital': 'Adis Abeba', 'coordenadas': [9.02, 38.75]},
    'Gabão': {'capital': 'Libreville', 'coordenadas': [0.39, 9.45]},
    'Gâmbia': {'capital': 'Banjul', 'coordenadas': [13.45, -16.57]},
    'Gana': {'capital': 'Acra', 'coordenadas': [5.56, -0.20]},
    'Guiné': {'capital': 'Conacri', 'coordenadas': [9.54, -13.68]},
    'Guiné-Bissau': {'capital': 'Bissau', 'coordenadas': [11.86, -15.60]},
    'Guiné Equatorial': {'capital': 'Malabo', 'coordenadas': [3.75, 8.78]},
    'Kenya': {'capital': 'Nairóbi', 'coordenadas': [-1.28, 36.82]},
    'Lesoto': {'capital': 'Maseru', 'coordenadas': [-29.31, 27.48]},
    'Libéria': {'capital': 'Monróvia', 'coordenadas': [6.31, -10.80]},
    'Líbia': {'capital': 'Trípoli', 'coordenadas': [32.89, 13.19]},
    'Madagascar': {'capital': 'Antananarivo', 'coordenadas': [-18.88, 47.53]},
    'Malawi': {'capital': 'Lilongwe', 'coordenadas': [-13.97, 33.79]},
    'Mali': {'capital': 'Bamaco', 'coordenadas': [12.65, -8.00]},
    'Mauritânia': {'capital': 'Nouakchott', 'coordenadas': [18.08, -15.98]},
    'Maurícia': {'capital': 'Port Louis', 'coordenadas': [-20.16, 57.50]},
    'Moçambique': {'capital': 'Maputo', 'coordenadas': [-25.97, 32.57]},
    'Namíbia': {'capital': 'Windhoek', 'coordenadas': [-22.56, 17.08]},
    'Níger': {'capital': 'Niamey', 'coordenadas': [13.51, 2.11]},
    'Nigéria': {'capital': 'Abuja', 'coordenadas': [9.08, 7.41]},
    'Quênia': {'capital': 'Nairóbi', 'coordenadas': [-1.28, 36.82]},
    'República Centro-Africana': {'capital': 'Bangui', 'coordenadas': [4.39, 18.55]},
    'República Democrática do Congo': {'capital': 'Kinshasa', 'coordenadas': [-4.32, 15.32]},
    'República do Congo': {'capital': 'Brazzaville', 'coordenadas': [-4.27, 15.27]},
    'Ruanda': {'capital': 'Kigali', 'coordenadas': [-1.96, 30.06]},
    'São Tomé e Príncipe': {'capital': 'São Tomé', 'coordenadas': [0.33, 6.73]},
    'Senegal': {'capital': 'Dacar', 'coordenadas': [14.69, -17.44]},
    'Serra Leoa': {'capital': 'Freetown', 'coordenadas': [8.49, -13.24]},
    'Seychelles': {'capital': 'Victoria', 'coordenadas': [-4.68, 55.49]},
    'Somália': {'capital': 'Mogadíscio', 'coordenadas': [2.04, 45.34]},
    'Suazilândia': {'capital': 'Lobamba', 'coordenadas': [-26.47, 31.19]},
    'São Tomé e Príncipe': {'capital': 'São Tomé', 'coordenadas': [0.19, 6.61]},
    'Senegal':{'capital': 'Dacar', 'coordenadas': [14.71, -17.45]},
    'Serra Leoa':{'capital': 'Freetown', 'coordenadas': [8.49, -13.24]},
    'Seychelles': {'capital': 'Victoria', 'coordenadas': [-4.62, 55.45]},
    'Somália': {'capital': 'Mogadíscio', 'coordenadas': [2.05, 45.34]},
    'Sudão':{'capital': 'Cartum', 'coordenadas': [15.59, 32.53]},
    'Sudão do Sul': {'capital': 'Juba', 'coordenadas': [4.86, 31.58]}
 
}

for pais, info in paises_capitais_africa.items():
    capital = info['capital']
    coordenadas = info['coordenadas']
    folium.Marker(location=coordenadas, popup=capital).add_to(mapa_africa)
    folium.Marker(location=coordenadas, icon=folium.Icon(color='gray')).add_to(mapa_africa)
    
mapa_africa.save('africa.html')
mapa_africa


# Abre o arquivo HTML no navegador padrão
webbrowser.open('asia.html')
webbrowser.open('africa.html')
webbrowser.open('europa.html')
webbrowser.open('america.html')

