
var testJob = {{value}};

alert(testJob);

//var testJob = {'': 10, 'WA': 35, 'DE': 3, 'DC': 25, 'WI': 8, 'WV': 1, 'HI': 2, 'FL': 2625, 'NH': 5, 'NJ': 2615, 'NM': 3, 'TX': 7843, 'LA': 2593, 'NC': 5195, 
	//			'ND': 4, 'NE': 2, 'TN': 9, 'NY': 2673, 'PA': 2616, 'CA': 13123, 'NV': 1, 'VA': 50, 'CO': 2612, 'AK': 1, 'AL': 3, 'AR': 2594, 'VT': 2592, 
		//		'IL': 2644, 'GA': 34, 'IN': 13, 'IA': 5, 'MA': 5230, 'AZ': 20, 'ID': 2, 'CT': 13, 'MD': 2608, 'OK': 4, 'OH': 2622, 'UT': 7, 'MO': 26, 
			//	'MN': 28, 'MI': 5206, 'RI': 7, 'KS': 4, 'MT': 1, 'MS': 1, 'SC': 13, 'KY': 5, 'OR': 14};

var all_states = ["HI", "AK", "FL", "NH", "AHO", "MI1", "MI2", "VT", "ME", "RI", "NY", "PA", "NJ", "DE", "MD", "VA", "WV", "OH", "IN", "IL", 
"CT", "WI", "NC", "DC", "MA", "TN", "AR", "MO", "GA", "SC", "KY", "AL", "LA", "MS", "IA", "MN", "OK", "TX", "NM", "KS", "NE", "SD", "ND", 
"WY", "MT", "CO", "ID", "UT", "AZ", "NV", "OR", "CA", "WA"];

var job_numbers = Object.keys(testJob).map(function (state) {return testJob[state];});
var min = Math.min.apply(null, job_numbers);
var max = Math.max.apply(null, job_numbers);

var color = d3.scale.linear()
			.domain([min, max])
			.range(["red","green"]);
			
for (i = 0; i < all_states.length; i++){
	if (testJob[all_states[i]] >= 0) {
		console.log(all_states[i]);
		d3.select("Path#" + all_states[i] + ".state")
			.style("fill", color(testJob[all_states[i]]));
	}
}