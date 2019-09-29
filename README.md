# emx_server

#### Tech Stack
* Python 3.7.4, 3.6.9
#### Services
* Github for version control
* Heroku for web-hosting (auto build integration with github repo)
* Flask, gunicorn for web-service
####Setup
* clone repository
* pip install requirements
* run emx_server.py

####Thoughts
##### Starting local web server
    There are many options that provide rapid prototyping capabilities. The ones I was familiar with being Node.js,
    Flask and Django. I ruled out Django since all I needed was a simple web-server and not a full-stack web framework.
    Node is extremely easy to set up for simple web service and is also very performant. But considering the fact that
    I wasn't writing client side code and I am much more proficient in python than javascript, I went with Flask. 
##### Hosting on the web
    Now I had the flask service running locally on a windows machine and the code was histed in a git repository. 
    For deploying it online I chose Heroku which is a cloud platform as a service. There are other alternatives but 
    this was failry easy to understand and set up with continuous build intergration with my git repo. So I could push
    code to my repo and the chnages would  be reflected on the hosted service seamlessly

#### The Puzzle!
This was the most complex part of the project.The string contains the character set followed by the codec to be filled 
in for each of the character in the setseperated by newline. The codec is a clue to the sort order of the characters in
the and based on the clues we need to first figure out the correct ordering and then fill in the missing values in the codec.

    Assumptions
    I have made certain assumptions (but will be happy to provide further explanations if needed)
    * There can be any number of characters in the set but the number should equal the codec provided i.e. each character
      should have an associated codec. The code validates this assumption
    * No two characters in the character set can be equal to each other
    
    Explanation
    
   
        
    
