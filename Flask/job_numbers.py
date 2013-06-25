
from python_testing import job_search, extract_data, num_pages

def job_info(job_name):
## Initialize global variables
    date_list, state_list, expired_list, city_list, lat_list, long_list = [], [], [], [], [], []

    query_name = job_search(job_name)  

## Get a count of the total number of relevant jobs found
    job_total = num_pages(query_name)
    page_total = job_total/25        
    count = 1    
    for pages in range(page_total):
    #    #for now, the extract_data will only extract state_list
        state_list += extract_data(query_name, str(count), str(count * 25), date_list, state_list, expired_list, city_list, lat_list, long_list)
        count += 25
    
    ## Separate the states by uniqueness and count the number of each state with a job post        
    unique_states = list(set(state_list))
    state_counts = {i: state_list.count(i) for i in unique_states}
    state_info = [unique_states, state_counts]
    
    return state_info
    
    ## Produce a dictionary of States with any "True" values and the # of values ex: {TX:22}
    
    #expired_counts = []
    
    #if True in expired_list:
        #find the true one and add it to a dictionary for that state   
        
 

 