import os

# desktopFile = os.path.expanduser("~/Desktop/myfile.txt")

os.makedirs(os.path.expanduser('~/Desktop/newProject'))
os.chdir(os.path.expanduser('~/Desktop/newProject'))
index = open('index.html', 'w+')
index.write( """ <!DOCTYPE html>
<html>
    \t<head>
        \t\t<title>Test</title>
        \t\t<meta name="viewport" content="width=device-width, initial-scale=1">
        \t\t<link rel="stylesheet" href="css/main.css">
    \t</head>
    \t<body>
        \t\t\t<h1>This is a H1<h1>
    \t</body>
\t</html> """)
