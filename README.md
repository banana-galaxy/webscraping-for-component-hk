# webscraping for component-hk

[component-hk](https://component-hk.net) has very attractive prices but its website offers no parametric search. These couple of programs are made with the aim of making the search easier.

`get_data.py` gathers info on every product it can find from a product category and `find&display.py` can then use this information to perform a parametric search on it

## Usage

1. Both `get_data.py` and `find&display.py` files have an `url` variable inside the code. Set that variable to the link you get after going into `products index` in the top menu and selecting a category.

2. Run `get_data.py`, it will create a json file with the info on all the components it can find. (it might take a little while to gather all the information)

3. `find&display.py` has a list variable in the code called `searchTerms`, remove all the search terms/keywords in there and put in your own. The program can search for a range of numerical values for a specific property. The syntax demonstrated on an example is: `1-5V`. 1 being the minimum numerical value, 5 the maximum one, and V for volts being the property.

4. Run `find&display.py`, it will create an html file which you can then open in your browser and look at the search results
