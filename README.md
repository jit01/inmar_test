# inmar
Location, department, Category, subcategory based sorting the stuff 

Location: The Location where the user can 
Departmet : if you chooose location it will sort out the department based on location, 
Category and subcategory : same as department functionality


api/v1/location  => To add new location 
api/v1/department => To add new department 
api/v1/category => To add new category
api/v1/store => To add new store info with the above foreign key


api/v1/location/<int:location>/department 
api/v1/location/<int:location>/department/<int:department>/category
api/v1/location/<int:location>/department/<int:department>/category/<int:category>/subcategory
api/v1/location/<int:location>/department/<int:department>/category/<int:category>/subcategory/<int:subcategory>


above 4 API to retrive the data based on values provided... 
