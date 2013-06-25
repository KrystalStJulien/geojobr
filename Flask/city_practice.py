# -*- coding: utf-8 -*-
import urllib2
import simplejson as json

def fifteen_per_state(state):
    cities_15 = {
    'AL': ['Birmingham', 'Montgomery', 'Mobile', 'Huntsville', 'Tuscaloosa', 'Hoover', 'Dothan', 'Decatur',
        'Auburn', 'Madison', 'Florence', 'Gadsden', 'Vestavia Hills', 'Prattville', 'Phenix City'],
    'AK': ['Anchorage', 'Fairbanks', 'Juneau', 'Sitka', 'Ketchikan', 'Wasilla', 'Kenai', 'Kodiak', 'Bethel',
            'Palmer', 'Homer', 'Unalaska', 'Barrow', 'Soldotna', 'Valdez'],
    'AZ': ['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Glendale', 'Scottsdale', 'Gilbert', 'Tempe', 'Peoria',
            'Surprise', 'Yuma', 'Avondale', 'Flagstaff', 'Goodyear', 'Lake Havasu City'], 
    'AR': ['Little Rock', 'Fort Smith', 'Fayetteville', 'Springdale', 'Jonesboro', 'North Little Rock', 'Conway',
            'Rogers', 'Pine Bluff', 'Bentonville', 'Hot Springs', 'Benton', 'Texarkana', 'Sherwood', 'Jacksonville'],
    'CA': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno', 'Sacramento', 'Long Beach', 'Oakland',
            'Bakersfield', 'Anaheim', 'Santa Ana', 'Riverside', 'Stockton', 'Chula Vista', 'Fremont'],
    'CO': ['Denver', 'Colorado Springs', 'Aurora', 'Fort Collins', 'Lakewood', 'Thornton', 'Arvada', 'Westminster',
            'Pueblo', 'Centennial', 'Boulder', 'Greeley', 'Longmont', 'Loveland', 'Grand Junction'],
    'CT': ['Bridgeport', 'New Haven', 'Hartford', 'Stamford', 'Waterbury', 'Norwalk', 'Danbury', 'New Britain',
            'Bristol', 'Meriden', 'Milford', 'West Haven', 'Middletown', 'Norwich'],
    'DE': ['Wilmington', 'Dover', 'Newark', 'Middletown', 'Smyrna', 'Milford', 'Seaford', 'Georgetown', 'Elsmere',
            'New Castle', 'Millsboro', 'Laurel', 'Harrington', 'Camden', 'Clayton'],
    'DC': ['Washington'],
    'FL': ['Jacksonville', 'Miami', 'Tampa', 'St. Petersburg', 'Orlando', 'Hialeah', 'Tallahassee', 'Fort Lauderdale',
            'Port St. Lucie', 'Pembroke Pines', 'Cape Coral', 'Hollywood', 'Gainesville', 'Miramar', 'Coral Springs'],
    'GA': ['Atlanta', 'Augusta', 'Columbus', 'Savannah', 'Athens', 'Sandy Springs', 'Macon', 'Roswell', 'Albany', 'Johns Creek',
            'Warner Robins', 'Alpharetta', 'Marietta', 'Valdosta', 'Smyrna'],
    'HI': ['Honolulu', 'Pearl City', 'Hilo', 'Kailua', 'Waipahu', 'Kāne‘ohe', 'Mililani Town', 'Kahului', '‘Ewa Gentry',
            'Kīhei'],
    'ID': ['Boise', 'Nampa', 'Meridian', 'Idaho Falls', 'Pocatello', 'Caldwell', "Coeur d'Alene", 'Twin Falls', 'Lewiston',
            'Post Falls', 'Rexburg', 'Moscow', 'Eagle', 'Kuna', 'Mountain Home'],
    'IL': ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville', 'Springfield', 'Peoria', 'North Peoria', 'Elgin', 'Waukegan'],
    'IN': ['Indianapolis', 'Fort Wayne', 'Evansville', 'South Bend', 'Carmel', 'Bloomington', 'Fishers', 'Hammond', 'Gary',
            'Muncie', 'Lafayette', 'Terre Haute', 'Kokomo', 'Anderson', 'Noblesville'],
    'IA': ['Des Moines', 'Cedar Rapids', 'Davenport', 'Sioux City', 'Iowa City', 'Waterloo', 'Council Bluffs', 'Ames',
            'West Des Moines', 'Dubuque', 'Ankeny', 'Urbandale', 'Cedar Falls', 'Marion', 'Bettendorf'],
    'KS': ['Wichita', 'Overland Park', 'Kansas City', 'Topeka', 'Olathe', 'Lawrence', 'Shawnee', 'Manhattan', 'Lenexa',
            'Salina', 'Hutchinson', 'Leavenworth', 'Leawood', 'Dodge City', 'Garden City'],
    'KY': ['Louisville', 'Lexington', 'Bowling Green', 'Owensboro', 'Covington', 'Hopkinsville', 'Richmond', 'Florence',
            'Georgetown', 'Elizabethtown', 'Nicholasville', 'Henderson', 'Jeffersontown', 'Frankfort', 'Paducah'],
    'LA': ['New Orleans', 'Baton Rouge', 'Shreveport', 'Metairie', 'Lafayette', 'Lake Charles', 'Kenner', 'Bossier City',
            'Monroe', 'Alexandria', 'Houma', 'Marrero', 'New Iberia', 'Laplace', 'Slidell'], 
    'ME': ['Portland', 'Lewiston', 'Bangor', 'South Portland', 'Auburn', 'Biddeford', 'Sanford', 'Augusta', 'Saco',
            'Westbrook', 'Waterville', 'Presque Isle', 'Brewer', 'Bath', 'Caribou'],
    'MD': ['Baltimore', 'Frederick', 'Rockville', 'Gaithersburg', 'Bowie', 'Hagerstown', 'Annapolis', 'College Park',
            'Salisbury', 'Laurel', 'Greenbelt', 'Cumberland', 'Westminster', 'Hyattsville', 'Takoma Park'],
    'MA': ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford', 'Brockton', 'Quincy', 'Lynn',
            'Fall River', 'Newton', 'Lawrence', 'Somerville', 'Framingham', 'Haverhill'],
    'MI': ['Detroit', 'Grand Rapids', 'Warren', 'Sterling Heights', 'Lansing', 'Ann Arbor', 'Flint', 'Dearborn',
            'Livonia', 'Clinton', 'Canton', 'Westland', 'Troy', 'Farmington Hills', 'Macomb'],
    'MN': ['Minneapolis', 'Saint Paul', 'Rochester', 'Duluth', 'Bloomington', 'Brooklyn Park', 'Plymouth', 'St. Cloud',
            'Eagan', 'Woodbury', 'Maple Grove', 'Eden Prairie', 'Coon Rapids', 'Burnsville', 'Blaine'],
    'MS': ['Jackson', 'West Gulfport', 'Gulfport', 'Southaven', 'Hattiesburg', 'Biloxi', 'Meridian', 'Tupelo',
            'Greenville', 'Olive Branch'],
    'MO': ['Kansas City', 'St. Louis', 'Springfield', 'Independence', 'Columbia', "Lee's Summit", "O'Fallon", 'St. Joseph',
            'St. Charles', 'St. Peters', 'Blue Springs', 'Florissant', 'Joplin', 'Chesterfield', 'Jefferson City'],
    'MT': ['Billings', 'Missoula', 'Great Falls', 'Bozeman', 'Butte', 'Helena', 'Kalispell', 'Havre', 'Anaconda',
            'Miles City', 'Belgrade', 'Livingston', 'Laurel', 'Whitefish', 'Lewistown'],
    'NE': ['Omaha', 'Lincoln', 'Bellevue', 'Grand Island', 'Kearney', 'Fremont', 'Hastings', 'North Platte', 'Norfolk',
            'Columbus', 'Papillion', 'La Vista', 'Scottsbluff', 'South Sioux City', 'Beatrice'],
    'NV': ['Las Vegas', 'Henderson', 'Reno', 'North Las Vegas', 'Sparks', 'Carson City', 'Fernley', 'Elko', 'Mesquite',
            'Boulder City', 'Fallon', 'Winnemucca', 'West Wendover', 'Ely', 'Yerington'],
    'NH': ['Manchester', 'Nashua', 'Concord', 'Derry', 'Dover', 'Rochester', 'Salem', 'Merrimack', 'Hudson', 'Londonderry',
            'Keene', 'Bedford', 'Portsmouth', 'Goffstown', 'Laconia'],
    'NJ': ['Newark', 'Jersey City', 'Paterson', 'Elizabeth', 'Edison', 'Woodbridge Township', 'Lakewood Township', 'Toms River',
            'Hamilton', 'Trenton', 'Clifton', 'Camden', 'Brick Township', 'Cherry Hill', 'Passaic'],
    'NM': ['Albuquerque', 'Las Cruces', 'Rio Rancho', 'Santa Fe', 'Roswell', 'Farmington', 'South Valley', 'Clovis', 'Hobbs', 
            'Alamogordo', 'Carlsbad', 'Gallup', 'Los Alamos', 'Deming', 'Los Lunas'],
    'NY': ['New York', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse', 'Albany', 'New Rochelle', 'Mount Vernon', 'Schenectady',
            'Utica', 'White Plains', 'Troy', 'Niagara Falls', 'Binghamton', 'Rome'],
    'NC': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem', 'Fayetteville', 'Cary', 'Wilmington',
            'High Point', 'Greenville', 'Asheville', 'Concord', 'Gastonia', 'Jacksonville', 'Chapel Hill'],
    'ND': ['Fargo', 'Bismarck', 'Grand Forks', 'Minot', 'West Fargo', 'Dickinson', 'Mandan', 'Williston', 'Jamestown',
            'Wahpeton', 'Devils Lake', 'Valley City', 'Grafton', 'Beulah', 'Rugby'],
    'OH': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron', 'Dayton', 'Parma', 'Canton', 'Youngstown', 'Lorain',
            'Hamilton', 'Springfield', 'Kettering', 'Elyria', 'Lakewood'],
    'OK': ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow', 'Lawton', 'Edmond', 'Moore', 'Midwest City', 'Enid',
            'Stillwater', 'Muskogee', 'Bartlesville', 'Owasso', 'Shawnee', 'Ponca City'],
    'OR': ['Portland', 'Eugene', 'Salem', 'Gresham', 'Hillsboro', 'Beaverton', 'Bend', 'Medford', 'Springfield', 'Corvallis',
            'Albany', 'Tigard', 'Lake Oswego', 'Keizer', 'Grants Pass'],
    'PA': ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading', 'Scranton', 'Bethlehem', 'Lancaster', 'Harrisburg',
            'Altoona', 'York', 'State College', 'Wilkes-Barre', 'Chester', 'Williamsport'],
    'RI': ['Providence', 'Warwick', 'Cranston', 'Pawtucket', 'East Providence', 'Woonsocket', 'North Providence', 'West Warwick',
            'Newport', 'Bristol'],
    'SC': ['Columbia', 'Charleston', 'North Charleston', 'Mount Pleasant', 'Rock Hill', 'Greenville', 'Summerville', 'Sumter',
            'Hilton Head Island', 'Florence'],
    'SD': ['Sioux Falls', 'Rapid City', 'Aberdeen', 'Brookings', 'Watertown', 'Mitchell', 'Yankton', 'Pierre', 'Huron',
            'Vermillion', 'Spearfish', 'Brandon', 'Box Elder', 'Sturgis', 'Madison'],
    'TN': ['Memphis', 'Nashville', 'Knoxville', 'Chattanooga', 'Clarksville', 'Murfreesboro', 'Jackson', 'Johnson City',
            'Franklin', 'Bartlett', 'Hendersonville', 'Kingsport', 'Collierville', 'Cleveland', 'Smyrna'],
    'TX': ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth', 'El Paso', 'Arlington', 'Corpus Christi', 'Plano',
            'Laredo', 'Lubbock', 'Garland', 'Irving', 'Amarillo', 'Grand Prairie'],
    'UT': ['Salt Lake City', 'West Valley City', 'Provo', 'West Jordan', 'Orem', 'Sandy', 'Ogden', 'St. George', 'Layton',
            'Taylorsville', 'South Jordan', 'Logan', 'Lehi', 'Murray', 'Bountiful'],
    'VT': ['Burlington', 'South Burlington', 'Rutland', 'Barre', 'Montpelier', 'Winooski', 'St. Albans', 'Newport',
            'Vergennes'],
    'VA': ['Virginia Beach', 'Norfolk', 'Chesapeake', 'Richmond', 'Newport News', 'Alexandria', 'Hampton', 'Roanoke',
            'Portsmouth', 'Suffolk', 'Lynchburg', 'Harrisonburg', 'Charlottesville', 'Danville', 'Manassas'],
    'WA': ['Seattle', 'Spokane', 'Tacoma', 'Vancouver', 'Bellevue', 'Kent', 'Everett', 'Renton', 'Yakima', 'Federal Way', 
            'Spokane Valley', 'Bellingham', 'Kennewick', 'Auburn', 'Pasco'],
    'WV': ['Charleston', 'Huntington', 'Parkersburg', 'Morgantown', 'Wheeling', 'Weirton', 'Fairmont', 'Beckley', 'Martinsburg',
            'Clarksburg', 'South Charleston', 'St. Albans', 'Vienna', 'Bluefield', 'Moundsville'],
    'WI': ['Milwaukee', 'Madison', 'Green Bay', 'Kenosha', 'Racine', 'Appleton', 'Waukesha', 'Oshkosh', 'Eau Claire',
            'Janesville', 'West Allis', 'La Crosse', 'Sheboygan', 'Wauwatosa', 'Fond du Lac'],
    'WY': ['Cheyenne', 'Casper', 'Laramie', 'Gillette', 'Rock Springs', 'Sheridan', 'Green River', 'Evanston', 'Riverton',
            'Jackson', 'Cody', 'Rawlins', 'Lander', 'Torrington', 'Powell']
    }
    return cities_15[state]
    
def job_search(job_name):
    #job_title = raw_input('Please list job title: ')
    ##for now: hard coding a job title
    job_title = job_name

    if len(job_title.split()) == 0:
        print 'No job entry detected, please try again.'
        job_search()
    elif len(job_title.split()) > 1:
        query_name = ""
        for word in range(len(job_title.split())):
            query_name += job_title.split()[word] + "+"   
        query_name = query_name[:-1]
        return query_name
    else:
        query_name = job_title
        return query_name  


def city_numbers(query_name, cities, state):
    
    job_numbers = []
    for each in cities:
        city = job_search(each)

        url = 'http://api.indeed.com/ads/apisearch?publisher=3962451415712761&format=json&q=title:"' + query_name + '"&l=' + city + '+' + state + '&sort=&radius=&st=&jt=&start=&limit=&fromage=&filter=&latlong=1&co=us&chnl=&userip=&useragent=Mozilla/%2F4.0%28Firefox%29&v=2'
    
        ## Grab the indeed query based on the job title input by the user
        file = urllib2.urlopen(url)

        ## Concatenate the API output data into a string of JSON
        json_string = ""

        for line in file.readlines():
            # remove the whitespace (newlines) while grabbing lines of file
            line = line.rstrip()
            if line:
                json_string += line
                
        ## Parse JSON API output string into a dictionary of dictionaries
        j = json.loads(json_string)
    
        ## Get a count of the total number of relevant jobs found
        job_numbers.append(j['totalResults'])
        
    return job_numbers
    