from bottle import route, run, request, response, static_file, get, template


@route('/')
def hello():
	f = open('./Pages/index.html')
	return f.read()


@get('/styles.css')
def retCss():
	return static_file('styles.css', root='./Pages')


@get('/', method='POST')
def checkFlag():
	flag = request.forms.get('flag')
	if flag == "PB{eat_my_cookies}" or flag == "PB{I'm_a_cookiebot}" or flag == "PB{Jake_don't_mind}" or flag == "PB{Jake_isn't_lonely}" or flag == 'PB{Y0tub3_v1d30s_ar3_fun}':
		f = open('./Pages/Correct.html')
		return f.read()
	else:
		f = open('./Pages/TryAgain.html')
		return f.read()


@route('/1')
def task1():
	response.set_cookie("is_admin", "no", path="/")
	if request.get_cookie("is_admin") == "no":
		f = open('./Pages/Task1/Task1GUEST.html')
		return f.read()
	elif request.get_cookie("is_admin") == "yes":
		f = open('./Pages/Task1/Task1ADMIN.html')
		return f.read()


@route('/2')
def task2():
	response.set_cookie("is_robot", "99e9bae675b12967251c175696f00a70", path="/")
	if request.get_cookie("is_robot") == "87b7cb79481f317bde90c116cf36084b":
		f = open('./Pages/Task2/Task2ROBOT.html')
		return f.read()
	else:
		f = open('./Pages/Task2/Task2HUMAN.html')
		return f.read()

@route('/3')
def task3():
	response.set_cookie("Jake_Surname", "Jake-None", path="/")
	if request.get_cookie("Jake_Surname") == "Jake-Cake":
		f = open('./Pages/Task3/Task3SOLVED.html')
		return f.read()
	else:
		f = open('./Pages/Task3/Task3notSOLVED.html')
		return f.read()


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
		f = open('./Pages/Task4/Task4SOLVED.html')
		return f.read()
	else:
		f = open('./Pages/Task4/Task4notSOLVED.html')
		return f.read()


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
		f = open('./Pages/Task4/Task4preSOLVED.html')
		return f.read()
	else:
		f = open('./Pages/Task4/Task4preNOTsolved.html')
		return f.read()

@route('/5')
def task5():
	response.set_cookie('u_re_dog', '5ac8ed2a7cc7038692785af9a958b46d')
	if request.get_cookie('u_re_dog') == 'df7e2ff08f3c98c59764f28c3bcfa5c3':
		f = open('./Pages/Task5/Task5SOLVED.html')
		return f.read()
	else:
		f = open('./Pages/Task5/Task5notSOLVED.html')
		return f.read()

@route('/5', method='PATCH')
def tash5patch():
	f = open('./Pages/Task5/Task5preSOLVED.html')
	return f.read()

run(host='localhost', port=8080, debug=True)
