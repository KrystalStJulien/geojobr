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

    populations = {"HI": 139*0.047, "AK": 73*0.059, "FL": 1932*0.071, "NH": 1321*0.053, "MI": 988*0.084, 
            "VT": 63*0.041, "ME": 133*0.068, "RI": 105*0.089, "NY": 1957*0.076, "PA": 1276*0.075, 
	   "NJ": 886*0.086, "DE": 92*0.072, "MD": 588*0.067, "VA": 819*0.053, "WV": 186*0.062, "OH": 1154*0.07, "IN": 654*0.083, 
	   "IL": 1288*0.091, "CT": 359*0.08, "WI": 573*0.07, "NC": 975*0.088, 
	   "DC": 63*0.085, "MA": 665*0.066, "TN": 646*0.083, "AR": 295*0.073, "MO": 602*0.068, 
	   "GA": 992*0.083, "SC": 472*0.08, "KY": 438*0.081, "AL": 482*0.068, "LA": 460*0.068, "MS": 298*0.091, 
	   "IA": 307*0.046, "MN": 538*0.053, "OK": 381*0.05, "TX": 2606*0.065, "NM": 209*0.067, "KS": 289*0.057, 
	   "NE": 189*0.038, "SD": 83*0.04, "ND": 70*0.032, "WY": 186*0.046, "MT": 101*0.054, 
	   "CO": 519*0.069, "ID": 160*0.062, "UT": 286*0.046, "AZ": 655*0.078, "NV": 276*0.095, "OR": 390*0.078, 
	   "CA": 3805*0.086, "WA": 690*0.068};
    
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
        norm_numbers.append(float(jobs)/float(date_avg)/float(populations[each]))
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
