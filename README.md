#MERCYS_RESTAURANT's 

##SUMMARY
The project is a website which is about the system on how Mercys_Restaurant works.

##FEATURES
It is created using Django and it follows the MVT design pattern (MVT - Model View Template).

##FUNCTIONS
 The model contains the data that needs to be presented which is from the database. In this particular database, each data is the order of a unique customer. In each order, it is the food ordered, the cost of the meal, the waiter name, the tip cost to the waiter and the tip percentage which is the tip cost out of meal cost. After the model is the view. It is a request handler that returns the contents. For this website, the main methods used is the GET, POST, PUT and DELETE. Generally, these methods are used standardly to create any website. GET is used to display all the results. Additionally, in the GET method, the serializers.py is called in which complex data is converted to Python data types. The other method which is POST. This is used to add new data into the database. Then is PUT which updates one of the old data and the last one is DELETE which deletes one of the old data. There was one more method called Retreive which works from a new GET method that will display a particular order. 