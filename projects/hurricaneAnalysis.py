#This project aimed to use the basics of Python programming (dictionaries, loops, conditionals, etc.) to analyze data and put it into context.




# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

damages_conv=[]
# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert (list):
  for elem in list:
    if elem=="Damages not recorded":
      damages_conv.append(elem)
    elif "M" in elem:
      newStr=elem.replace("M","")
      damages_conv.append(float(newStr)*conversion["M"])
    elif "B" in elem: 
      NewStr=elem.replace("B","")
      damages_conv.append(float(NewStr)*conversion["B"])
      

convert(damages)


def create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_conv, deaths):
  """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
  hurricanes = {}
  num_hurricanes = len(names)
  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": damages_conv[i],
                          "Deaths": deaths[i]}
  return hurricanes

# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_conv, deaths)

print(hurricanes)

# 3
# Organizing by Year
def create_year_dictionary(hurricanes):
  """Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""
  hurricanes_by_year= {}
  for cane in hurricanes:
   #cane is the name (key) of every hurricane
      current_year = hurricanes[cane]['Year']
      current_cane = hurricanes[cane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year


# create a new dictionary of hurricanes with year and key
hurricanes_by_year=create_year_dictionary(hurricanes)
#print(hurricanes)

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

#using the List 
lenlist=len(areas_affected)
flatList=[]
ares={}
def areas_from_comlex_list(list):
    for i in list:
        for j in i:
            flatList.append(j)
    for elem in flatList:
        test=flatList.count(elem)
        if elem not in ares:
            ares[elem]=flatList.count(elem)
    return ares
#test=areas_from_comlex_list(areas_affected)
#print(test)

areas=[]
#using dict. 
def value_in_dic(dic):
    for canes in dic.keys():
        areas.append(dic[canes]["Areas Affected"])
    return areas_from_comlex_list(areas)

print(value_in_dic(hurricanes))

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def most_affected_region(dicti):
    worst_value=0
    worst_key=""    
    my_values=value_in_dic(dicti)
    for item in my_values.items():
        if item[1]>worst_value:
            worst_value=item[1]
            worst_key=item[0]
            print(worst_key,worst_value)
        
most_affected_region(hurricanes)



#6
# Rating Hurricanes by Mortality
# Calculating the Deadliest Hurricane

def killer_hurricane(dic):
    values={}
    deaths=0
    deaths_key=""

    for cane in dic:
        values[cane]=dic[cane]['Deaths']
    for item in values.items():
        if item[1]>deaths:
            deaths=item[1]
            deaths_key=item[0]
    #print(deaths,deaths_key)
#killer_hurricane(hurricanes)
