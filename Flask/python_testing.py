import urllib2
import simplejson as json
#from testing_again import extract_date
from test_date_time import calculate_date
import decimal

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

## Extract date, state, expired, city, latitude, and longitude information for job_title user selects
def extract_data(query_name, start, end, date_list, state_list, expired_list, city_list, lat_list, long_list):
    #global date_list, state_list, expired_list, city_list, lat_list, long_list
    url = "http://api.indeed.com/ads/apisearch?publisher=3962451415712761&format=json&q=" + query_name + "&l=&sort=&radius=&st=&jt=&start=" + start + "&limit=" + end + "&fromage=&filter=&latlong=1&co=us&chnl=&userip=&useragent=Mozilla/%2F4.0%28Firefox%29&v=2"
    
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

    ## Produce complete list of dates, states, cities, and expired_post data for specific job query 
    for keys in range(len(j['results'])):
        if 'date' in j['results'][keys].keys():
            date_list.append(j['results'][keys]['date'])
        elif 'date' not in j['results'][keys].keys():
            date_list.append("NA")
            
        if 'state' in j['results'][keys].keys():
            state_list.append(j['results'][keys]['state'])
        elif 'state' not in j['results'][keys].keys():
            state_list.append("NA")
            
        if 'expired' in j['results'][keys].keys(): 
            expired_list.append(j['results'][keys]['expired'])
        elif 'expired' not in j['results'][keys].keys():
            expired_list.append("NA")
            
        if 'city' in j['results'][keys].keys():
            city_list.append(j['results'][keys]['city'])
        elif 'city' not in j['results'][keys].keys():
            city_list.append("NA")
            
        if 'latitude' in j['results'][keys].keys():
            lat_list.append(j['results'][keys]['latitude'])
        elif 'latitude' not in j['results'][keys].keys():
            lat_list.append(0)
               
        if 'longitude' in j['results'][keys].keys():
            long_list.append(j['results'][keys]['longitude'])
        elif 'longitude' not in j['results'][keys].keys():
            long_list.append(0)
            
    return state_list
        
    
def norm_numbers(query_name):
    all_states = ["HI", "AK", "FL", "NH", "MI", "VT", "ME", "RI", 
        "NY", "PA", "NJ", "DE", "MD", "VA", "WV", "OH", "IN", "IL", "CT", "WI", "NC", 
        "DC", "MA", "TN", "AR", "MO", "GA", "SC", "KY", "AL", "LA", "MS", "IA", "MN", 
        "OK", "TX", "NM", "KS", "NE", "SD", "ND", "WY", "MT", "CO", "ID", "UT", "AZ", 
        "NV", "OR", "CA", "WA"]
    
    state_pop = [139, 73, 1932, 1321, 988, 63, 133, 105,
        1957, 1276, 886, 92, 588, 819, 186, 1154, 654, 1288, 359, 573, 975,
        63, 665, 646, 295, 602, 992, 472, 438, 482, 460, 298, 307, 538,
        381, 2606, 209, 289, 189, 83, 70, 186, 101, 519, 160, 286, 655,
        276, 390, 3805, 690]
    
    dates_list = []
    job_numbers = []
    for each in all_states:
        url = "http://api.indeed.com/ads/apisearch?publisher=3962451415712761&format=json&q=" + query_name + "&l=" + each + "&sort=&radius=&st=&jt=&start=0&limit=0&fromage=&filter=&latlong=1&co=us&chnl=&userip=&useragent=Mozilla/%2F4.0%28Firefox%29&v=2"
    
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
        date_list = []
        dates_list.append(extract_date(query_name, date_list))
    
    total_jobs = sum(job_numbers)
    norm_numbers = []
    for every_state in range(len(all_states)):
        normalized = float(job_numbers[every_state]) / float(state_pop[every_state])       
        norm_numbers.append(normalized)
        
    norm_numbers.append(total_jobs)
    return norm_numbers

def abs_numbers(query_name):
    all_states = ["HI", "AK", "FL", "NH", "MI", "VT", "ME", "RI", 
        "NY", "PA", "NJ", "DE", "MD", "VA", "WV", "OH", "IN", "IL", "CT", "WI", "NC", 
        "DC", "MA", "TN", "AR", "MO", "GA", "SC", "KY", "AL", "LA", "MS", "IA", "MN", 
        "OK", "TX", "NM", "KS", "NE", "SD", "ND", "WY", "MT", "CO", "ID", "UT", "AZ", 
        "NV", "OR", "CA", "WA"]
    
    state_pop = [139, 73, 1932, 1321, 988, 63, 133, 105,
        1957, 1276, 886, 92, 588, 819, 186, 1154, 654, 1288, 359, 573, 975,
        63, 665, 646, 295, 602, 992, 472, 438, 482, 460, 298, 307, 538,
        381, 2606, 209, 289, 189, 83, 70, 186, 101, 519, 160, 286, 655,
        276, 390, 3805, 690]
    
    job_numbers = []
    for each in all_states:
        url = "http://api.indeed.com/ads/apisearch?publisher=3962451415712761&format=json&q=" + query_name + "&l=" + each + "&sort=&radius=0&st=&jt=&start=&limit=25&fromage=&filter=&latlong=1&co=us&chnl=&userip=&useragent=Mozilla/%2F4.0%28Firefox%29&v=2"
    
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

def norm_vals(query_name):
    all_states = ["HI", "AK", "FL", "NH", "MI", "VT", "ME", "RI", 
        "NY", "PA", "NJ", "DE", "MD", "VA", "WV", "OH", "IN", "IL", "CT", "WI", "NC", 
        "DC", "MA", "TN", "AR", "MO", "GA", "SC", "KY", "AL", "LA", "MS", "IA", "MN", 
        "OK", "TX", "NM", "KS", "NE", "SD", "ND", "WY", "MT", "CO", "ID", "UT", "AZ", 
        "NV", "OR", "CA", "WA"]
    
#    state_pop = [139, 73, 1932, 1321, 988, 63, 133, 105,
#        1957, 1276, 886, 92, 588, 819, 186, 1154, 654, 1288, 359, 573, 975,
#        63, 665, 646, 295, 602, 992, 472, 438, 482, 460, 298, 307, 538,
#        381, 2606, 209, 289, 189, 83, 70, 186, 101, 519, 160, 286, 655,
#        276, 390, 3805, 690]

    populations = {"HI": 139, "AK": 73, "FL": 1932, "NH": 1321, "MI": 988, "VT": 63, "ME": 133, "RI": 105, "NY": 1957, "PA": 1276, 
	   "NJ": 886, "DE": 92, "MD": 588, "VA": 819, "WV": 186, "OH": 1154, "IN": 654, "IL": 1288, "CT": 359, "WI": 573, "NC": 975, 
	   "DC": 63, "MA": 665, "TN": 646, "AR": 295, "MO": 602, "GA": 992, "SC": 472, "KY": 438, "AL": 482, "LA": 460, "MS": 298, 
	   "IA": 307, "MN": 538, "OK": 381, "TX": 2606, "NM": 209, "KS": 289, "NE": 189, "SD": 83, "ND": 70, "WY": 186, "MT": 101, 
	   "CO": 519, "ID": 160, "UT": 286, "AZ": 655, "NV": 276, "OR": 390, "CA": 3805, "WA": 690};
    
    norm_numbers = []
    job_numbers = []
    dates_list = []
    for each in all_states:
        url = 'http://api.indeed.com/ads/apisearch?publisher=3962451415712761&format=json&q=title:+"' + query_name + '"&l=' + each + '&sort=&radius=0&st=&jt=&start=&limit=50&fromage=&filter=&latlong=1&co=us&chnl=&userip=&useragent=Mozilla/%2F4.0%28Firefox%29&v=2'

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
        #job_numbers.append(j['totalResults'])
        jobs = j['totalResults']
    
        date_list = []
        for keys in range(len(j['results'])):
            if 'date' in j['results'][keys].keys():
                date = calculate_date(j['results'][keys]['date'])
                date_list.append(date)
            elif 'date' not in j['results'][keys].keys():
                date_list.append("NA")
        
        if sum(date_list):        
            date_avg = sum(date_list)/len(date_list) + 1
        else:
            date_avg = 1
            
        #normalized = float(jobs) / float(populations[each]) * date_avg   
        job_numbers.append(jobs)    
        norm_numbers.append(jobs*date_avg)
        dates_list.append(date_avg)
    
    all_list = [job_numbers, dates_list]
    total_norm = sum(norm_numbers)
    score_list = []
    for values in norm_numbers:
        if total_norm == 0:
            score_list.append(0)
        else:
            score = round(float(values)/float(total_norm)*100, 1)
            score_list.append(score)
    
    total_jobs = sum(job_numbers)
    all_list.append(score_list)
    all_list.append(total_jobs)
    #score_list.append(total_jobs)
    return all_list
