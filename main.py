#####
# Δ #
#####

import flask, os, cryptocode, bz2, pickle
from replit import db
from flask import render_template, request, redirect, url_for, make_response, session, send_file
from threading import Thread
import requests as rq
import time

############
# RESET DB #
############

# pdb = pickle.load(bz2.BZ2File('pdb.txt', 'r'), encoding='latin1')
# f'{ipj["ip"]} | {ipj["postal"]} {ipj["city"]} {ipj["region"]} {ipj["country_code"]} | {round(float(ipj["latitude"]), 4)} {round(float(ipj["longitude"]), 4)} | {ispj["name"]} {ispj["type"].upper()}'

def spdb():
    pickle.dump(pdb, bz2.BZ2File('pdb.txt', 'w'))


def gssu(user):
    samtused = len(bz2.compress(pickle.dumps(pdb[user], -1)))
    if samtused >= 1048576:
        return f"~{round(samtused / 1048576, 2)}MB / ~{round(pdb[user]['x']['samt'] / 1024, 2)}MB"
    else:
        return f"~{round(samtused / 1024, 2)}KB / {pdb[user]['x']['samt']}KB"


pdb = {}

pdb['x'] = {}
pdb['x']['x'] = {'samt': 1024}  # (KB)

pdb['x']['q'] = [100000, ['test1', 'test2', 'test3', 'test4', 'test5']]
pdb['x']['blog'] = [[
    'First',
    'background:#080808;font-size:5vh;font-family:monospace;color:white',
    'test test\ntest test<br>test test test <i>test</i>'
]]

spdb()

#####

db['q'] = [['? - ?Δ', '? - ?Δ', '? - ?Δ', '? - ?Δ', '? - ?Δ'], 0]
db['o']['nac'] = {}
# db['o']['l']['mods'] = ['https://xmods.repl.co/_', 6]
# db['o']['l'].pop('hacks')
# db['u']['l'] = {'a': ['https://qwkq.repl.co/o/l/_', 0]}
# db['ip'] = {'81.111.183.142': 'DEV'}
# db['api'] = {'lpwd': 0}
# TOTAL V, TODAY V, YESTERDAY V, AVG, LEN AVG DATASET
# db['o']['l'] = {"_": ["https://qwkq.repl.co/_", 319, 0, 0, 3.19, 100], "nogameshere": ["https://nogameshere2.repl.co/home", 1093, 0, 0, 10.93, 100], "ezbux": ["https://ezbux.repl.co/home", 157, 0, 0, 1.57, 100], "mods": ["https://xmods.repl.co/_", 258, 0, 0, 2.58, 100]}

#####

# return redirect(url_for('x', x=x))

app = flask.Flask('QWKQ')
app.secret_key = os.environ['appsecretkey']
ipdata = os.environ['IPDATA']

#####


@app.route('/baldy')
def baldy():
    return send_file('baldy.txt', mimetype='text')


@app.route('/hacks')
def hacks():
    return '<body style="background:#000000"></body><script>window.location.href = "https://qwkq.repl.co/o/l/hacks";</script>'


@app.route('/hacks_')
def hacks_():
    return make_response(render_template('hacks.html'))


@app.route('/hack/<n>')
def hack(n):
    return send_file(f'general/hacks/{n}', mimetype='text/javascript')


#####


def cmd(c='', i1='', i2='', i3=''):
    if c == '':
        print('//ONLINE')
    if c == 'dblu':
        print('//Here are all active links:')
        print(
            f"// | I{' '*((int(len(max(db['u']['l'], key=len))))-1)} | L{' '*((len(max([i[0] for i in list(db['u']['l'].values())], key=len)))-1)} | V{' '*((len(max([str(i[1]) for i in list(db['u']['l'].values())], key=len)))-1)} |"
        )
        for i in db['u']['l']:
            print(
                f"// | {i}{' '*((int(len(max(db['u']['l'], key=len))))-len(i))} | {db['u']['l'][i][0]}{' '*((len(max([i[0] for i in list(db['u']['l'].values())], key=len)))-len(db['u']['l'][i][0]))} | {db['u']['l'][i][1]}{' '*((len(max([str(i[1]) for i in list(db['u']['l'].values())], key=len)))-len(str(db['u']['l'][i][1])))} |"
            )
    if c == 'dblo':
        print('//Here are all active links:')
        print(
            f"// | I{' '*((int(len(max(db['o']['l'], key=len))))-1)} | L{' '*((len(max([i[0] for i in list(db['o']['l'].values())], key=len)))-1)} | V{' '*((len(max([str(i[1]) for i in list(db['o']['l'].values())], key=len)))-1)} |"
        )
        for i in db['o']['l']:
            print(
                f"// | {i}{' '*((int(len(max(db['o']['l'], key=len))))-len(i))} | {db['o']['l'][i][0]}{' '*((len(max([i[0] for i in list(db['o']['l'].values())], key=len)))-len(db['o']['l'][i][0]))} | {db['o']['l'][i][1]}{' '*((len(max([str(i[1]) for i in list(db['o']['l'].values())], key=len)))-len(str(db['o']['l'][i][1])))} |"
            )

@app.route('/api/ping')
def api_p():
    if db['api']['lpwd'] != time.localtime().tm_wday:
        db['api']['lpwd'] = time.localtime().tm_wday
        for i in db['o']['l'].keys():
            db['o']['l'][i][4] = round(db['o']['l'][i][1] / (db['o']['l'][i][5] + 1), 2)
            db['o']['l'][i][5] += 1
            db['o']['l'][i][3] = db['o']['l'][i][2]
            db['o']['l'][i][2] = 0
    return '<body style="background:#000000; color:#ffffff">PING</body>'

@app.route('/api/visits')
def api_v():
    return [{'n': i, 'v': db['o']['l'][i][1], 't': db['o']['l'][i][2], 'y': db['o']['l'][i][3], 'a': db['o']['l'][i][4], 'u': round(db['o']['l'][i][2] - db['o']['l'][i][4], 2)} for i in db['o']['l'].keys()]

@app.route('/')
def rtlp():
    return '<body style="background:#000000"></body><script>window.location.href = "https://qwkq.repl.co/o/l/_";</script>'


@app.route('/_')
def landing_():
    # return '<body style="background:#080808;font-family:monospace;color:white;margin:0;padding:0;box-sizing:border-box;overflow:hidden;font-size:99vh;text-align:center;line-height:1">Δ</body>'
    return make_response(render_template('landing.html'))


@app.errorhandler(404)
def error404(e):
    resp = make_response(render_template('404.html'))
    return resp, 404


@app.errorhandler(500)
def error500(e):
    resp = make_response(render_template('500.html'))
    return resp, 500


# HTML TEMPLATES

plfhtml = '<body style="background:#080808;font-size:10vh;font-family:monospace;color:white">Please login first before accesing this service.</body>'

# /dev/ DEV


@app.route('/games')
def games():
    return '<body style="background:#080808;font-size:10vh;font-family:monospace;color:white">PAGE COMING SOON<br><br>Indie game dev, IGN:<br><b><i>@cheekyrizz</i></b></body>'


@app.route('/dev/footer')
def dev_footer():
    return make_response(render_template('footer.html'))


# /q/ QWK


@app.route('/q')
def q_index():
    if session['lia'] != None:
        return redirect(url_for('q_home'))
    return plfhtml


@app.route('/q/home')
def q_home():
    resp = make_response(
        render_template('q/home.html',
                        username=session['lia'],
                        balance=pdb[session['lia']]['q'][0],
                        his=pdb[session['lia']]['q'][1],
                        d=list(db['q'][0])))
    return resp


# /x/ WHOLE SITE


@app.route('/x')
def x():
    return make_response(render_template('index.html'))


@app.route('/x/acc/ls/<dxu>/<dxp>')
def x_acc_ls(dxu, dxp):
    dxu = dxu.lower()
    session['lia'] = None
    for _ in dxu:
        if _ not in list('abcdefghijklmnopqrstuvwxyz0123456789'):
            return f'<body style="background:#080808;font-size:5vh;font-family:monospace;color:white">The name:<br>{dxu}<br>Contains characters other than a-z and 0-9<br>Please make sure your name is <i><b>five or more characters long</b></i> and only contains characters that are from <i><b>a-z</b></i> and/or <i><b>0-9</b></i>.<br>(Name will be put in <i><b>ALL</b></i> lower case automatically)</body>'
    if len(dxu) < 5 and dxu != 'x':
        return f'<body style="background:#080808;font-size:5vh;font-family:monospace;color:white">The name:<br>{dxu}<br>Has less than five characters.<br>Please make sure your name is <i><b>five or more characters long</b></i> and only contains characters that are from <i><b>a-z</b></i> and/or <i><b>0-9</b></i>.<br>(Name will be put in <i><b>ALL</b></i> lower case automatically)</body>'
    xu, xp = cryptocode.encrypt(dxu, os.environ['key2k']), cryptocode.encrypt(
        dxp, os.environ['key2k'])
    if dxu not in [
            cryptocode.decrypt(_, os.environ['key2k'])
            for _ in list(db['x'].keys())
    ] and dxu:
        db['x'][xu] = xp
        session['lia'] = dxu
        return f'<body style="background:#080808;font-size:5vh;font-family:monospace;color:white">Created new account and logged in as:<br>{dxu}</body>'
    for i in range(len(list(db['x'].keys()))):
        if cryptocode.decrypt(
                list(db['x'].keys())[i],
                os.environ['key2k']) == dxu and cryptocode.decrypt(
                    db['x'][list(db['x'].keys())[i]],
                    os.environ['key2k']) == dxp:
            session['lia'] = dxu
            return f'<body style="background:#080808;font-size:5vh;font-family:monospace;color:white">Logged in as:<br>{dxu}</body>'
    return f'<body style="background:#080808;font-size:5vh;font-family:monospace;color:white">Wrong password for the account named:<br>{dxu}</body>'


# @app.route('/x/signup')
# def x_signup():
#     pass

# /u/ USER CONTENT

# ;;BLOG

# TODO: USERS, BLOGS, SEARCH, LIKE


@app.route('/u/blog')
def u_blog():
    if session['lia'] != None:
        pass
    return plfhtml


@app.route('/u/blog/new')
def u_blog_new():
    return make_response(render_template('u/blog/new.html'))


# ;;L


@app.route('/u/l/<n>')
def u_l(n='_'):
    if n != '_':
        db['u']['l'][n][1] += 1
        return redirect(db['u']['l'][n][0])
    else:
        return '<body style="background:#080808;color:white;font-family:monospace"><h1>ADD YOUR OWN LINK!<br>Remember to include <i>https://</i></h1><form action="/u/l/_/c" method = "POST"><input type="text" id="ul" name="ul" placeholder="Link"><input type="submit" value="Submit"></form><p><small>By clicking "Submit" you agree that your link can be removed for any reason at any time.<br>We will usually remove a link if it contains illegal media/items or is a scam/virus.</small></p>'


@app.route('/u/l/_/v/<n>')
def u_l_v(n):
    return f'<body style="background:#080808;color:white;font-family:monospace"><h1>Link: <a href="https://qwkq.repl.co/u/l/{n}">qwkq.repl.co/u/l/{n}</a><br>URL: <a href="{db["u"]["l"][n][0]}">{db["u"]["l"][n][0]}</a><br>Visits: {db["u"]["l"][n][1]}</h1>'


@app.route('/u/l/_/c', methods=['GET', 'POST'])
def u_l_c():
    if request.method == 'POST':
        ul, nk = request.form['ul'], list(list(db['u']['l'].keys())[-1])
        for i in range(len(nk)):
            if i != len(nk) - 1:
                if nk[-(i + 1)] != '-':
                    nk[-(i +
                         1)] = list('abcdefghijklmnopqrstuvwxyz0123456789-')[
                             list('abcdefghijklmnopqrstuvwxyz0123456789-'
                                  ).index(nk[-(i + 1)]) + 1]
                    break
                else:
                    nk[-(i + 1)] = 'a'
            else:
                if nk[-(i + 1)] != '-':
                    nk[-(i +
                         1)] = list('abcdefghijklmnopqrstuvwxyz0123456789-')[
                             list('abcdefghijklmnopqrstuvwxyz0123456789-'
                                  ).index(nk[-(i + 1)]) + 1]
                    break
                else:
                    nk[-(i + 1)] = 'a'
                    nk.append('a')
                    break
        db['u']['l'][''.join(nk)] = [ul, 0]
    return f'<body style="background:#080808;color:white;font-family:monospace"><h1>Your link is online! Here is the link:<br><a href="https://qwkq.repl.co/u/l/{"".join(nk)}">qwkq.repl.co/u/l/{"".join(nk)}</a><br>Go to: <a href="https://qwkq.repl.co/u/l/_/v/{"".join(nk)}">qwkq.repl.co/u/l/_/v/{"".join(nk)}</a> to see how many visits your link has!</h1>'


# /o/ OFFICIAL CONTENT

# ;L


@app.route('/o/l/<n>', methods=['GET'])
def o_l(n='nogameshere'):
    ip = None
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    if ip != None:
        if ip not in db['ip'].keys():
            ipj = rq.get(
                f'https://api.ipdata.co/{ip}?api-key={ipdata}&fields=ip,city,region,country_code,postal,latitude,longitude'
            ).json()
            ispj = rq.get(
                f'https://api.ipdata.co/{ip}/asn?api-key={ipdata}&fields=name,type'
            ).json()
            ipinfo = f'{ipj["ip"]} | {ipj["postal"]} {ipj["city"]} {ipj["region"]} {ipj["country_code"]} | {round(float(ipj["latitude"]), 4)} {round(float(ipj["longitude"]), 4)} | {ispj["name"]} {ispj["type"].upper()}'
            rq.get(
                'http://xdroid.net/api/message',
                params={
                    'k': os.environ['XDROID'],
                    't': f'{n.upper()}',
                    'c': ipinfo,
                    'u': f'https://qwkq.repl.co/o/l/v/{n}'
                })
            db['ip'][ip] = ipinfo
        else:
            rq.get(
                'http://xdroid.net/api/message',
                params={
                    'k': os.environ['XDROID'],
                    't': f'{n.upper()}',
                    'c': db['ip'][ip],
                    'u': f'https://qwkq.repl.co/o/l/v/{n}'
                })
    db['o']['l'][n][1] += 1
    db['o']['l'][n][2] += 1
    if db['o']['l'][n][1] % 100 == 0:
        return f'<body style="background:#080808;color:white;font-family:monospace;""><h1 style="font-size: 10vh;">{n.upper()} NOW HAS {db["o"]["l"][n][1]} VISITS!<br>REDIRECTING IN 5 SECS...</h1></body><script>function timeFunction() {{ setTimeout(function(){{ window.location.href = "https://qwkq.repl.co/o/l/{n}"; }}, 5000); }};timeFunction();</script>'
    return redirect(db['o']['l'][n][0])


@app.route('/o/l/v/<n>')
def o_l_v(n):
    return f'<body style="background:#080808;color:white;font-family:monospace"><h1>Link: <a href="https://qwkq.repl.co/o/l/{n}">qwkq.repl.co/o/l/{n}</a><br>URL: <a href="{db["o"]["l"][n][0]}">{db["o"]["l"][n][0]}</a><br>Visits: {db["o"]["l"][n][1]}</h1>'


# ;FILE

@app.route('/o/file/<m>/<n>')
def o_file(m, n):
    if m == 'png':
        return send_file(f'general/o/file/{m}/{n.strip(".png")}.{m}',
                         mimetype='image/png')
    return send_file(f'general/o/file/{m}/{n}.{m}')

@app.route('/-/<n>')
def o_f(n):
    p = n.split(".", 1)[-1]
    if p == 'png':
        return send_file(f'general/o/file/{p}/{n}', mimetype='image/png')
    return send_file(f'general/o/file/{p}/{n}')


# ;NAC


@app.route('/o/nac/<n>/<id>', defaults={'x': ''})
@app.route('/o/nac/<n>/<id>/<x>', methods=['GET'])
def o_nac(n, id, x=''):
    if request.method == 'GET':
        if x == '':
            if id not in db['a']['nac']:
                db['a']['kac'][id] = [
                    '.', '.', '.', '.', '.', '.', '.', '.', '.'
                ]
            return flask.Response(db['a']['nac'][id][int(n) - 1],
                                  mimetype='text/plain')
            # return db['a']['kac'][id][int(n) - 1]
        else:
            if id not in db['a']['nac']:
                db['a']['nac'][id] = [
                    '.', '.', '.', '.', '.', '.', '.', '.', '.'
                ]
            if db['a']['nac'][id][int(n) - 1] == '.':
                if x == 'x' or 'o':
                    db['a']['nac'][id][int(n) - 1] = x
            return flask.Response('Done.', mimetype='text/plain')


def run():
    app.run(host='0.0.0.0', port=5050)


def keep_alive():
    keepalivet = Thread(target=run)
    keepalivet.start()


keep_alive()
