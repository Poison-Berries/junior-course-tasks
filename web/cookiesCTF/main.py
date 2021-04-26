from bottle import route, run, request, response, static_file, get


@route('/')
def hello():
    return '''
	<body>
		<h1 class=".header1">Select a task or check flag:</h1>
		<b><a href="/1" class="link">Task №1(Update page)</a>
		<br></br>
		<a href="/2" class="link">Task №2</a>
		<br></br>
		<a href="/3" class="link">Task №3</a>
		<br></br>
		<a href="/4" class="link">Task №4</a>
		<br></br>
		<a href="/5" class="link">Task №5</a>
		<br></br>
		<p></p>
		<div class="form_design">
			<p><b>Check flag:</b></p>
			<form action="/" method="post" class="form">
				<b>Flag:</b> <input name="flag" type="text" />
				<br></br>
				<input value="Check!" type="submit" />
			</form>
		</div>
		<link rel="stylesheet" type="text/css" href="/styles.css">
		<link rel="preconnect" href="https://fonts.gstatic.com">
		<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
	</body>
    '''


@get('/styles.css')
def retCss():
    return static_file('styles.css', root='./')


@route('/', method='POST')
def checkFlag():
    flag = request.forms.get('flag')
    if flag == "PB{eat_my_cookies}" or flag == "PB{I'm_a_cookiebot}" or flag == "PB{Jake_don't_mind}" or flag == "PB{Jake_isn't_lonely}" or flag == 'PB{Y0tub3_v1d30s_ar3_fun}':
        return '''
		<body>
			<h1 class="correct">Correct!</h1>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''
    else:
        return '''
		<body>
			<h1 class="try_again">Try again!</h1>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''


@route('/1')
def task1():
    response.set_cookie("is_admin", "no", path="/")
    if request.get_cookie("is_admin") == "no":
        return '''
		<body>
			<h1>Hello, Guest!</h1>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''
    elif request.get_cookie("is_admin") == "yes":
        return '''
		<body>
			<h1>Hello, Admin!</h1>
			<p>Flag: PB{eat_my_cookies}</p>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''


@route('/2')
def task2():
    response.set_cookie("is_robot", "99e9bae675b12967251c175696f00a70", path="/")
    if request.get_cookie("is_robot") == "87b7cb79481f317bde90c116cf36084b":
        return '''
		<body>
			<h1>Hello, Robot!</h1>
			<p>Flag: PB{I'm_a_cookiebot}</p>
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''
    else:
        return '''
		<body>
			<h1>Hello, Human!</h1>
			<p>You're not a robot! To get a flag, you must be a robot!</p>
			<p>Hint: Cookies are protected by HASH, /usr/share/dict/words</p>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''


@route('/3')
def task3():
    response.set_cookie("Jake_Surname", "Jake-None", path="/")
    if request.get_cookie("Jake_Surname") == "Jake-Cake":
        return '''
		<body>
			<h1>Congratulations!</h1>
			<p>Jake is give you a present:</p>
			<p>Flag: PB{Jake_don't_mind}</p>
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''
    else:
        return '''
		<body>
			<h1>Oh No!</h1>
			<p>Jake forgot his surname! He went to a government and got a cipher with his surname!</p>
			<p>Please, decode it and write a decoded string to a cookie "Jake_Surname"!</p>
			<a href='/3_file1' class="link">Encoded string</a>
			<p></p>
			<a href='/3_file2' class="link">Ciphers. Guess the cipher by it alphabet!</a>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''


@route('/3_file1')
def task3_file1():
    return static_file('encoded_string.txt', root='./')


@route('/3_file2')
def task3_file2():
    return static_file('ciphers.png', root='./', mimetype='image/png')


@route('/4')
def task4():
    response.set_cookie("Jake_is_fun",
                        "35eae3ea7fe1598f7f8ffa2806229068074bac921b2d235ed02660c6009eba9d40b09e2f5bfa099c8e66235d89d2bd3771941741a02a181aba9dcb027acca465",
                        path='/')
    if request.get_cookie(
            "Jake_is_fun") == "7d357b285f1744c3af09312e2c2e3c577fec5d0a091cb26e3089624890a31aad4d78165cb696d796f10eb81a568bcfa165a2e54771ad5bfb8f6451e48d3c1159":
        return '''
		<body>
			<h1>Jake is fun!</h1>
			<p>Yeah! Flag: PB{Jake_isn't_lonely}</p>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''
    else:
        return '''
		<body>
			<h1>Jake is so lonely!</h1>
			<p>To get the password, send the letter to Jake by POST.</p1>
			<br></br>
			<p>Text in letter:</p>
			<p>letter=Hello, Jake!</p>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>'''


@route('/4', method='POST')
def check_letter():
    letter = request.body.read()
    letter = bytes.decode(letter, encoding='utf-8')
    d = 0
    s = ''
    for i in letter:
        if i == 'H':
            d = 1
            s += i
        elif i == '!':
            d = 0
            s += i
            break

        elif d == 1:
            s += i

    if s == 'Hello, Jake!':
        return '''
		<body>
			<h1>Oh! Thank you!</h1>
			<p>Your present: Jake_is_fun=7d357b285f1744c3af09312e2c2e3c577fec5d0a091cb26e3089624890a31aad4d78165cb696d796f10eb81a568bcfa165a2e54771ad5bfb8f6451e48d3c1159</p>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>
		'''
    else:
        return '''
		<body>
			<h1 class="try_again">Not today!</h1>
			<link rel="stylesheet" type="text/css" href="/styles.css">
			<link rel="preconnect" href="https://fonts.gstatic.com">
			<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
			<link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
		</body>
		'''

@route('/5')
def task5():
    response.set_cookie('u_re_dog', '5ac8ed2a7cc7038692785af9a958b46d')
    if request.get_cookie('u_re_dog') == 'df7e2ff08f3c98c59764f28c3bcfa5c3':
        return '''
            <body>
                <iframe width="560" height="315" src="https://www.youtube.com/embed/Qwe3CJinFSQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <h3>PB{Y0tub3_v1d30s_ar3_fun}</h3>
                <link rel="stylesheet" type="text/css" href="/styles.css">
                <link rel="preconnect" href="https://fonts.gstatic.com">
                <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
            </body>
        '''
    else:
        return '''
        <body>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/O-qLCajT3Y8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            <!-- Matilda says "Patch my files!" --> 
            <p>u_re_dog!</p>
            <link rel="stylesheet" type="text/css" href="/styles.css">
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
        </body>'''

@route('/5', method='PATCH')
def tash5patch():
    return '''
    <body>
        <h1>df7e2ff08f3c98c59764f28c3bcfa5c3</h1>
        <link rel="stylesheet" type="text/css" href="/styles.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:ital@1&display=swap" rel="stylesheet">
    </body>
    '''

run(host='localhost', port=8080, debug=True)
