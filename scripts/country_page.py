import os

#country = 'morroco'
#FULL_DIR = r'C:\xampp\htdocs\images\fulls\morroco'
#THUMBS_DIR = r'C:\xampp\htdocs\images\thumbs\morroco'
#HTML_DIR = r'C:\xampp\htdocs\countries'

## Create articles
articles = ''
for f in os.listdir(FULL_DIR):
	articles += '''
	<article>
		<a class="thumbnail" href="../images/fulls/{country}/{file}" data-position="left center"><img src="../images/thumbs/{country}/{file}" alt="" /></a>
		<h2>{title}</h2>
		<p>{paragraph}</p>
	</article>
	'''.format(file=f, title='Title', paragraph='Insert description here', country=country)

## Write page according to template
TEMPLATE_HTML = '''
<!DOCTYPE HTML>
<!--
	Lens by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<!-- Global site tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=UA-142138420-1"></script>
		<script>
  			window.dataLayer = window.dataLayer || [];
  			function gtag(){dataLayer.push(arguments);}
  				gtag('js', new Date());
  			gtag('config', 'UA-142138420-1');
		</script>
			
		<title>{country_low}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="../assets/css/main_lens.css" />
		<noscript><link rel="stylesheet" href="../assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload-0 is-preload-1 is-preload-2">
		<!-- Main -->
			<div id="main">
				<!-- Back button -->
				<div style="padding: 10px">
					<button  onclick="window.history.back();">BACK TO HOME PAGE</button>
				</div>			
				<!-- Header -->
				<header id="header">
					<h1>{country_high}</h1>
					<p>TEXTHERE</p>
				</header>
				<!-- Thumbnail -->
				<section id="thumbnails">
					{articles}
				</section>
				<!-- Footer -->
				<footer id="footer">
					<ul class="icons">
						<li><a href="https://twitter.com/terramaticspace" class="icon alt fa-twitter"><span class="label">Twitter</span></a></li>
						<li><a href="https://www.instagram.com/terramaticspace" class="icon alt fa-instagram"><span class="label">Instagram</span></a></li>
						<li><a href="https://github.com/jsalcal" class="icon alt fa-github"><span class="label">GitHub</span></a></li>
						<li><a href="https://www.linkedin.com/in/jsalcal" class="icon alt fa-linkedin"><span class="label">LinkedIn</span></a></li>
					</ul>
				</footer>

			</div>
		<!-- Scripts -->
			<script src="../assets/js/jquery.min.js"></script>
			<script src="../assets/js/browser.min.js"></script>
			<script src="../assets/js/breakpoints.min.js"></script>
			<script src="../assets/js/main_lens.js"></script>
	</body>
</html>\n
'''.format(country_low=country, country_high=country.upper(), articles=articles)


## Write file
with open(os.path.join(HTML_DIR, '{}.html'.format(country)), 'w') as f:
	f.write(TEMPLATE_HTML)
