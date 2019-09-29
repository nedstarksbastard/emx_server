# EMX Server

### Tech Stack
* Python 3.7.4 (local), 3.6.9 (hosted)
### Services
* Github for version control
* Heroku for web-hosting (auto build integration with github repo)
* Flask, gunicorn for web-service
####Setup
* clone repository
* pip install requirements
* run emx_server.py

### Rundown
#### Starting local web server
There are many options that provide rapid prototyping capabilities. The ones I was familiar with being Node.js,
Flask and Django. I ruled out Django since all I needed was a simple web-server and not a full-stack web framework.
Node is extremely easy to set up for simple web service and is also very performant. But considering the fact that
I was not writing client side code and I am much more proficient in python than javascript, I went with Flask. 
#### Hosting on the web
Now I had the flask service running locally on a windows machine and the code was histed in a git repository. 
For deploying it online I chose Heroku which is a cloud platform as a service. There are other alternatives but 
this was fairly easy to understand and set up with continuous build integration with my git repo. So I could push
code to my repo and the changes would  be reflected on the hosted service seamlessly

#### All requests save puzzle
Build a map that contains the request argument as key and the answer string to be sent back as value. Parse the request
argument (`q` in this case) and send back the associated value in the map

#### The Puzzle!!!
This was the most complex part of the project. The GET request was a string containing the character set followed 
by the codec to be filled in for each of the character in the set separated by newline. The codec is a clue 
to the sort order of the characters in the set and based on the clues we need to first figure out the correct ordering
and then fill in the missing values in the codec.

#####Assumptions
* There can be any number of characters in the set but the number should equal the codec provided i.e. each 
  character should have an associated codec. My code validates this assumption
* Each character in the set is distinct
* No two characters in the character set can be equal to each other

#####Algorithm
Each character in the set can be thought of as a node. For each character we are provided a clue:
* Either the character is equal to itself. Or,
* It is greater or less than another character in the set

###### Build DAG and sort it
We ignore the equality since that is an automatic assumption. For the second case
* Split and strip the string to get the characters and their associated codec  
* Add each character in the set as nodes in a graph
* Process the codec and create an edge between the nodes, the direction of which is from the lesser of the two
 nodes to the greater.As an example, for our puzzle we will have 4 nodes `A,B,C,D` and a codec like `A-->-` will 
 result in an edge going from `C -> A` denoting the fact that A is greater than C.  
* After processing each node and edge we get a Directed Acyclic Graph which is then be topologically sorted to get
 the right order.

###### Construct string from the sorted graph
Now that we have the right ordering, we need to build the string to be sent back. We build the string for each character
in the topologically started array starting from the lowest. Since this is the lowest node, all the characters in the
string will be `<` for all other nodes. 
* Initialize the string as `[<,<,<,<,<]` (node+codec)
* Let's say the first character in the topologically sorted array is `C` (lowest).  
    * Insert character `C` at index 0 and
    * Insert `=` at index of `C` (current node). 
* Now the list becomes `[C,<,<,=,<]`. We join the list into a string and insert it into the main list that will in turn be converted into a list before 
being sent back to client ( This is done because strings are immutable in Python and as such it is less expensive to 
perform modifications on a list and then convert it into a string when we are done)
* The next node in the array will be greater than the current one. Lets say the character is `A` (next lowest).
    * Insert `A` at the beginning of the list, index 0.
    * Insert `>` at index with value `=` (index of the last popped item in the sorted array since the new item 
    is greater than the previous item)
    * Insert `=` at the index of `A` (current node)
* Now the list becomes `[A,=,<,>,<]`. We convert this into a string and store it. 
* We process all the elements in the array till its empty and construct the final resultant string to be sent back.



    
   
        
    
