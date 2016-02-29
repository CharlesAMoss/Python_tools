import os
import webbrowser

project_name = raw_input("Project Name: ")

if not os.path.exists(os.path.expanduser('~/Desktop/' + project_name)):
    os.makedirs(os.path.expanduser('~/Desktop/' + project_name))
    print('Project folder ' + project_name + ' created')
os.chdir(os.path.expanduser('~/Desktop/' + project_name))
if not os.path.isfile('index.html'):
    index = open('index.html', 'w+')
    index.write("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>""" + project_name + """</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="css/main.css">
        </head>
        <body>
            <div class="wrapper">
                <h1>This is the """ + project_name.title() + """ page<h1>
            </div>
            <script type="text/javascript" src="js/main.js"></script>
        </body>
    </html> """)
    index.close
    print('index.html created')
if not os.path.exists(os.path.expanduser('~/Desktop/' + project_name + '/css')):
    os.makedirs(os.path.expanduser('~/Desktop/' + project_name + '/css'))
os.chdir(os.path.expanduser('~/Desktop/' + project_name + '/css'))
if not os.path.isfile('main.css'):
    style = open('main.css', 'w+')
    style.write("""
    *, *:before, *:after {
        box-sizing: border-box;
    }
    html {
        font-size: 100%;
        height: 100%;
        line-height: 1.3;
    }
    body {
        width: 98%;
    }
    /* type ===================== */
    h1, h2, h3, h4, h5, h6 {
        font-family: sans-serif;
        font-weight: 200;
    }
    h1 {
        font-size: 3.5082em;
        line-height: 1.1972;
        margin: 1.45rem 0;
    }
    h2 {
        font-size: 2.3125em;
    }
    h3 {
        font-size: 1.75em;
    }
    /* type ============== media */
    @media (min-width: 1200px) {
        html {
            font-size: 125%;
            line-height: 1.4;
        }
        h1 {
            line-height: 1.24;
            margin:: 1.45rem 0;
        }
        h2 {
          font-size: 1.769em;
        }
        h3 {
          font-size: 1.33em;
        }
    }
    /* layout ================= */
    .wrapper {
        width: 55%;
        margin: 4em auto 0 auto;
    }
    /* interface ================ */
    .form__btn {
        background: #f5f2f0;
        border-radius: 4px;
        border: 1px solid #d6cac2;
        color: #b7a294;
        padding: 20px;
        font-size: 1em;
        width: 100%;
    }
    .form__btn:hover {
        background: #f0f5f5;
        color: #94b7b4;
    }
    /* clear fix ================ */
    .pull-left {
        float: left;
    }
    .pull-right {
        float: right;
    }
    .group:after {
        content: "";
        display: table;
        clear: both;
    }
    """)
    style.close
    print('main.css created')
if not os.path.exists(os.path.expanduser('~/Desktop/' + project_name + '/js')):
    os.makedirs(os.path.expanduser('~/Desktop/' + project_name + '/js'))
os.chdir(os.path.expanduser('~/Desktop/' + project_name + '/js'))
if not os.path.isfile('main.js'):
    script = open('main.js', 'w+')
    script.write("// write some javascript")
    script.close
    print('main.js created')
os.chdir(os.path.expanduser('~/Desktop/' + project_name))
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open('file://' + os.path.realpath('index.html'))
