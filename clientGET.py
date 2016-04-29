#Build a client that prints the 5 first 
#elements of each available resource
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



if __name__ == "__main__":

	get_elements()
