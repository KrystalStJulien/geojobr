#from job_numbers import job_info
from python_testing import norm_vals, job_search, abs_numbers
from flask import render_template, request, jsonify
from app import app
import simplejson as json
from city_practice import city_numbers, fifteen_per_state

total = 0
search_term = ''

@app.route('/') 
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about_me')
def about_me():
    return render_template("about_me.html")
    
@app.route('/about_geojobr')
def about_geojobr():
    return render_template("about_geojobr.html")
      
@app.route('/top_cities', methods=['POST'])
def top_cities():
    global total, search_term    
    state = request.form['state_name']
    
    if state == 'MI1' or state == 'MI2':
        cities = fifteen_per_state("MI")
        state = "MI"
    else:
        cities = fifteen_per_state(state)
        
    search_string = job_search(search_term)    
    number_jobs = city_numbers(search_string, cities, state) 
    
    sorted_city_indices = sorted(range(len(number_jobs)), key=lambda k: number_jobs[k])
    job_list, city_list = [], []
    for indices in sorted_city_indices:
        job_list.append(number_jobs[indices])
        city_list.append(cities[indices])
    
    return render_template("top_cities.html", state = state, total = total, 
    jobnum_list = job_list, list_of_cities = city_list, query = search_term, search_string = search_string)
    
@app.route('/cost_of_living')
def col():
    return render_template("cost_of_living.html")        

@app.route('/map', methods=['POST'])
def map():
    global total, search_term
    search_term = request.form['search']
    
    numbers = norm_vals(job_search(search_term))
    total = numbers.pop()
    
    return render_template("demand_map.html", job_totals = numbers[0], date_avgs = numbers[1], numbers_list = numbers[2], total = total, query = search_term)

