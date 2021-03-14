# webscraping for component-hk

[component-hk](https://component-hk.net) has nice low prices on components but its website search is terrible. These couple of programs are made with the aim of making the search easier.

`get_data.py` gathers info on every component the website has to offer for a search and `find&display.py` can then take all that gathered information and perform a proper search on it

## Usage

1. Both `get_data.py` and `find&display.py` have an `url` variable. Set that variable to the link you get after performing a search on the website.

2. Run `get_data.py`, it will create a json file with the info on all the components from the website search you performed. (it might take a little while to gather all the information)

3. `find&display.py` has a list variable called `searchTerms`, remove all the search terms/keywords in there and put in your own. The program can search for a range of numerical values for a specific property. The syntax demonstrated on an example is: `1-5V`. 1 being the minimum numerical value, 5 the maximum one, and V for volts being the property.
