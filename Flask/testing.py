import urllib2
import simplejson as json
from python_testing import job_search, norm_vals
from city_practice import city_numbers, fifteen_per_state

search = "executive chef"
    
number_jobs = norm_vals(job_search(search))
print number_jobs