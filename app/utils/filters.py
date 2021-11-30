# date formatting to dd/mm/yyyy
def format_date(date):
  return date.strftime('%m/%d/%Y')

# url formatting to clean up the hyperlinks
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# plural word formatting
def format_plural(amount, word):
  if amount != 1:
    return word + 's'
  
  return word
