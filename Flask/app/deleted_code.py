
@app.route('/data_science_map')
def data_science_map():
    return render_template("data_science_map.html")

@app.route('/search')
def search():
    return render_template("practice_search.html")

@app.route('/form', methods=['POST'])
def form():
    search = request.form['search']
    return render_template("test_form.html", value = search)
    
@app.route('/query', methods=['POST'])
def query():
    term = request.form['search']
    #job_values = job_info(search_term)
    return render_template("query.html", search_term = term)
    
    
        #all_states = ['HI', "AK", "FL", "NH", "AHO", "MI1", "MI2", "VT", "ME", "RI", 
    #    "NY", "PA", "NJ", "DE", "MD", "VA", "WV", "OH", "IN", "IL", "CT", "WI", "NC", 
    #    "DC", "MA", "TN", "AR", "MO", "GA", "SC", "KY", "AL", "LA", "MS", "IA", "MN", 
    #    "OK", "TX", "NM", "KS", "NE", "SD", "ND", "WY", "MT", "CO", "ID", "UT", "AZ", 
    #    "NV", "OR", "CA", "WA"]
                ##[54, 76, 48, 23, 0, 45, 45, 38, 298, 386, 23, 59, 763, 96, 21, 12, 69, 47, 36, 6, 
                ##8, 4, 23, 34, 45, 76, 5, 237, 5, 43, 67, 78, 98, 292, 347, 65, 332, 5, 34, 34, 23, 893, 98, 
                ##73, 378, 59, 12, 65, 34, 89, 23, 843, 87];
    #numbers = []
    #for each in range(len(all_states)):
    #    if all_states[each] in job_values[1]:
    #        numbers.append(job_values[1][all_states[each]])
    #    else:
    #        numbers.append(0)
                
    #value = 18 #query()