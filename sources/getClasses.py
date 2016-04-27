from lxml import html
import requests

page = requests.get('http://ucsd.edu/catalog/front/courses.html')
tree = html.fromstring(page.content)

urls = tree.xpath( '//a[stars-with( @href, "../courses" )]' )

print urls