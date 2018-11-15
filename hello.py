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
	# combined_list = []
	movie_dict = {}

	print('SNO','-','TITLE')
	if 'results' in data:
		for i,element in enumerate(data['results']):
			# print(i+1, '-', element['title'])
			id_list.append(element['id'])
			title_list.append(element['title'])

			# combined_list.append(element['id'])
			# combined_list.append(element['title'])

		movie_dict = dict(zip(id_list, title_list))
		# DICTIONARY WITH KEY AS MOVIE ID AND NAME AS VALUE

		# print(movie_dict)



	# choice = int(input("choose serial number:"))
	# id_chosen = id_list[choice-1]
	#RETURN TO LANDING PAGE ITSELF. 
	
	return render_template('index.html',combined_list=movie_dict)
	# search_by_id(id_chosen)

@app.route('/moreDetails',methods=['POST'])
def search_by_id():
	API_KEY = 'c85b9d37d442d740f448c23fc53cc90f'
	user_query = request.form['id_search']
	print(user_query)
	param_dict = {'api_key':API_KEY,'append_to_response':"credits,reviews,videos,change_keys"}
	response = requests.get('https://api.themoviedb.org/3/movie/'+user_query,params = param_dict)
	data = response.json()
	print(data)

	for i in data:
		print(i)

	print("\nTITLE:",data['title'],"\nORIGINAL TITLE",data['original_title'],
		"\noriginal language:",data['original_language'],"\nRELEASE INFO:",data['release_date'],
		"\nOVERVIEW:",data['overview'],'\nREVENUE:',data['revenue'], "\nRUNTIME:",data['runtime'],
		"\nTrailers:",data['videos']
		)

	detail_list = []

	detail_dict = {}

	title = data['title']


	detail_list.append('TITLE:')
	detail_list.append(data['title'])
	detail_list.append('ORIGINAL TITLE:')
	detail_list.append(data['original_title'])
	detail_list.append('RELEASE INFO:')
	detail_list.append(data['release_date'])
	detail_list.append('OVERVIEW:')
	detail_list.append(data['overview'])
	detail_list.append('REVENUE:')
	detail_list.append(data['revenue'])
	detail_list.append('RUNTIME:')
	detail_list.append(data['runtime'])
	




	# print("\nTITLE:",data['title'],"\nORIGINAL TITLE",data['original_title'],
	# 		"\noriginal language:",data['original_language'],"\nRELEASE INFO:",data['release_date'],
	# 		"\nOVERVIEW:",data['overview'],"\nGENRES:",data['genres'], '\nREVENUE:',data['revenue'], "\nRUNTIME:",data['runtime'],
	# 		"\nREVIEWS:",data["reviews"],"\nCredits:",data['credits'])
	genre_list = []
	print('\nGenres =>')
	detail_list.append('Genres:')
	for i in data['genres']:
		print(i['name'])
		detail_list.append(i['name'])
		genre_list.append(i['name'])



	detail_dict['ORIGINAL TITLE'] = data['original_title']
	detail_dict['RELEASE DATE'] = data['release_date']
	detail_dict['GENRE'] = ", ".join(genre_list)
	detail_dict['OVERVIEW'] = data['overview']
	detail_dict['RUNTIME'] = str(data['runtime'])+' Min'
	detail_dict['REVENUE'] = '$'+str(data['revenue'])

	cast_list = []
	

	detail_list.append('Cast:')	
	print('\nCast =>')
	for i in data['credits']['cast']:
		print(i['name'])
		detail_list.append(i['name'])
		cast_list.append(i['name'])
	# cast_dict = {}
	# cast_dict['CAST'] = ", ".join(genre_list)
	# crew_list = []
	crew_list = []
	detail_list.append('crew:')	
	print('\nCrew =>')
	for i in data['credits']['crew']:
		print(i['name'])
		detail_list.append(i['name'])
		crew_list.append(i['name'])

	review_list = []
	detail_list.append('reviews:')
	print('\nREVIEWS =>')
	for i in data['reviews']['results']:
		print('\n',i['content'],'\nReviewed by', i['author'])
		detail_list.append(i['content'])
		detail_list.append('Reviewed By')
		detail_list.append(i['author'])

		review_list.append(i['content'] + ' <= || reviewed by || =>' + i['author'])
		# review_list.append()
		# review_list.append()

	trailer_dict = {}
	detail_list.append('TRAILER LINKS')
	print("\nTRAILER LINKS =>")
	for i in data['videos']['results']:
		print(i['name'],':',"https://www.youtube.com/watch?v="+i['key'])
		detail_list.append(i['name'])
		link = "https://www.youtube.com/embed/"+i['key'] # ?v=
		detail_list.append(link)
		trailer_dict[i['name']] = link
		# detail_list()
	if data['backdrop_path'] == None:
		backdrop_img = '/static/img/backdrop_not_found.jpg'
	else:
		backdrop_img = 'https://image.tmdb.org/t/p/w1280/'+data['backdrop_path']
	
	poster_img = 'https://image.tmdb.org/t/p/original/'+data['poster_path']
	print("\nImage Links")
	print("BACKDROP PATH:",data['backdrop_path'])
	# print('Backdrop Image Link:','https://image.tmdb.org/t/p/w300/'+data['backdrop_path'])
	print("POSTER PATH:",data['poster_path'])
	print('Poster Image Link:','https://image.tmdb.org/t/p/w92/'+data['poster_path'])

	return render_template('moreDetails.html',title = title, detail_list=detail_dict, 
		backdrop_img=backdrop_img, poster_img=poster_img, cast_list = cast_list,
		crew_list = crew_list, review_list = review_list, trailer_dict = trailer_dict
		)
if __name__ == "__main__":
	app.run(debug=True)