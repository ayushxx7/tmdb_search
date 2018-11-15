# MAIN APP THAT USES FLASK FOR BACKEND
# CLEAN, SIMPLE FRAMEWORK TO DO ALL THAT IS REQUIRED.
# NOTHING MORE, NOTHING LESS.

from flask import Flask, render_template, request # FLASK FILES
import requests # FOR API CALLS

# APP NAME = app
app = Flask(__name__)


# ROOT URL THAT RETURNS INDEX HTML
@app.route('/')
def index():
    return render_template('index.html')

# FUNCTION TO MAKE FIRST API CALL TO FETCH MOVIE NAMES MATCHING KEYWORD. 

@app.route('/script',methods=['POST'])
def search_by_name():

	API_KEY = 'c85b9d37d442d740f448c23fc53cc90f'
	user_query = request.form['user_search'] # TAKES IN USER INPUT FOR MOVIE NAME
	param_dict = {'api_key':API_KEY,'query':user_query} #DICTIONARY TO PASS AS PARAMETER
	response2 = requests.get('https://api.themoviedb.org/3/search/movie',params=param_dict)
	# API CALL

	data = response2.json() #CONVERT RESPONSE TO JSON

	id_list = []
	title_list = []
	movie_dict = {}

	print('SNO','-','TITLE')
	if 'results' in data:
		for i,element in enumerate(data['results']):
			id_list.append(element['id'])
			title_list.append(element['title'])


		movie_dict = dict(zip(id_list, title_list))
		# DICTIONARY WITH KEY AS MOVIE ID AND NAME AS VALUE

	#RETURN TO LANDING PAGE ITSELF. MOVIE DICT PASSED TO HTML.

	return render_template('index.html',combined_list=movie_dict)

# FUNCTION TO MAKE 2ND API CALL. TO FETCH MORE DETAILS ABOUT A MOVIE. 

@app.route('/moreDetails',methods=['POST'])
def search_by_id():
	API_KEY = 'c85b9d37d442d740f448c23fc53cc90f'
	user_query = request.form['id_search'] # TAKES FROM THE HIDDEN INPUT BOX IN TABLE IN INDEX PAGE
	param_dict = {'api_key':API_KEY,'append_to_response':"credits,reviews,videos,change_keys"}
	# APPEND TO RESPONSE IS USED TO GET EXTRA DETAILS USING MOVIE ID.
	# CREDITS HAS CAST AND CREW
	# VIDEOS HAS TRAILERS

	response = requests.get('https://api.themoviedb.org/3/movie/'+user_query,params = param_dict)
	data = response.json() # RESPONSE CONVERTED TO JSON 

	detail_dict = {}

	title = data['title']
	# GENRE LIST TO DISPLAY IN BASIC INFO TABLE
	genre_list = []
	for i in data['genres']:
		genre_list.append(i['name'])



	detail_dict['ORIGINAL TITLE'] = data['original_title']
	detail_dict['RELEASE DATE'] = data['release_date']
	detail_dict['GENRE'] = ", ".join(genre_list)
	detail_dict['OVERVIEW'] = data['overview']
	detail_dict['RUNTIME'] = str(data['runtime'])+' Min'
	detail_dict['REVENUE'] = '$'+str(data['revenue'])

	# DETAIL DICTIONARY WITH KEY AS LEFT COLUMN NAMES TO BE SHOWN IN TABLE
	# AND VALUES TO BE PASSED VIA API TO HTML

	# PUSH DATA IN CAST SECTION 

	cast_list = []
	for i in data['credits']['cast']:
		cast_list.append(i['name'])

	# PUSH DATA IN CREW SECTION 

	crew_list = []
	for i in data['credits']['crew']:
		crew_list.append(i['name'])

	# PUSH DATA TO REVIEW SECTION
	review_list = []
	for i in data['reviews']['results']:

		review_list.append(i['content'] + ' <= || reviewed by || =>' + i['author'])

	# PUSH TRAILER DICTIONARY WHICH HAS TRAILER NAME AND LINK TO EMBED VIDEOS IN HTML

	trailer_dict = {}
	for i in data['videos']['results']:
		link = "https://www.youtube.com/embed/"+i['key'] 
		trailer_dict[i['name']] = link

	# SOME OBSCURE MOVIES HAVE NO BACK DROPS

	if data['backdrop_path'] == None:
		backdrop_img = '/static/img/backdrop_not_found.jpg'
	else:
		backdrop_img = 'https://image.tmdb.org/t/p/w1280/'+data['backdrop_path']
	
	poster_img = 'https://image.tmdb.org/t/p/original/'+data['poster_path']

	# PAGE RENDERED IS MOREDETAILS.HTML
	# PASSED VALUES ARE TITLE, DETAIL DICTIONARY, BACKDROP IMAGE, POSTER IMAGE, 
	# CAST LIST, CREW LIST, REVIEW LIST AND TRAILER DICTIONARY
	# FOR JINJA RENDERING ON WEBPAGE

	return render_template('moreDetails.html',title = title, detail_list=detail_dict, 
		backdrop_img=backdrop_img, poster_img=poster_img, cast_list = cast_list,
		crew_list = crew_list, review_list = review_list, trailer_dict = trailer_dict
		)

# CALL IN COMMAND PROMPT VIA COMMAND: py hello.py
# server starts running on localhost:5000

if __name__ == "__main__":
	app.run(debug=True)