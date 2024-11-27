# With this module we can type the keyword and get the google search for whatever we input in the webbrowser.open() method
# It opens the browser with that search term 

import webbrowser

user_input = input("Enter the term to search: ").replace(" ", "+" )

webbrowser.open("https://www.google.com/search?q="+ user_input)