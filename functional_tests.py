from selenium import webdriver

browser = webdriver.Firefox()

# User visits an online to-do app
browser.get('http://localhost:8000')

# User checks that 'To-Do' is in the title
assert 'To-Do' in browser.title

# User is invited to enter a to-do item

# User types "Buy peacock feathers" into a text box

# When user hits <Enter>, the page updates and lists
# "1: Buy peacock feathers"

# The text box still allows the user to enter more items
# User adds "Use peacock feathers to make a fly"

# The page updates and lists both items

# The site has generated a unique URL to access the to-do list

# User visits that URL and confirms the list

# User is done with the site

browser.quit()
