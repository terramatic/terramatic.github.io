import os
import csv

clist = r'C:\xampp\htdocs\data\countries_desc.csv'
articlesFile = r'C:\xampp\htdocs\data\countries_articles.html'
linksFile = r'C:\xampp\htdocs\data\countries_links.html'

## Read list into dictionary
articles=''
links=''

with open(clist, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=';', quotechar='#')
	for row in reader:
		
		# Articles for the main block
		articles += '''						
		<article>
			<span class="image"><img src="{image}" alt="" /></span>
			<header class="major">
			  <h3><a href="{url}" class="link">{country}</a></h3>
			  <p>{desc}</p>
			</header>
		</article>'''.format(
			country=row[0], 
			desc=row[1],
			image='./images/fulls/{}/{}'.format(row[0].lower(), row[2]), 
			url='./countries/{}.html'.format(row[0].lower())
		)
		
		# Links for the menu section
		links+='''<li><a href="{url}">{country}</a></li>\n'''.format(country=row[0], url='./countries/{}.html'.format(row[0].lower()))

# Save to files HTML
with open(articlesFile, "w") as tf1:
    tf1.write(articles)

with open(linksFile, "w") as tf2:
    tf2.write(links)    