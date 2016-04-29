#Build a client that creates a post with 
#the data passed by argument
import requests

def get_elements():
 for resource in ["posts", "comments", "albums", "photos", "todos", "users"]:
	print resource, ":"
	resp = []
	resp = requests.get("http://jsonplaceholder.typicode.com/posts/")
	if resp.status_code != 200:
    		# This means something went wrong.
    		raise Exception('GET /tasks/ %s' % (resp.status_code))
	elements=resp.json()
	for element in range(0,5):
		print elements[element],"\n"


def post_elements():
	data = {
		"userId": 29,
		"id": 333,
		"title": "OSCAR's POST",
		"body": "Texteeeeeeeeeeeeeeeeeeeee el Barca fara doblet"}

	resp = requests.post("http://jsonplaceholder.typicode.com/posts/",data=data)
	if resp.status_code != 201:
    		raise Exception('POST /posts/ %s' % (resp.status_code))
	print 'Created task. ID: %s' % (resp.json()["id"])

if __name__ == "__main__":

	post_elements()
