import os
from flask import Flask, render_template, request, send_from_directory

from gmail import Gmail

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/contact.php', methods=['GET'])
@app.route('/contact', methods=['GET'])
def contact():
    if is_spam(request):
        return 'Spamming is a sin. You will not enjoy your dirty money.'
    else:
        return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def submit_contact():
    variables = ["%s: %s" % (k,v,) for k, v in os.environ.items()]
    variables.sort()
    body = """
Planet Terasi Feedback

About: %s
From: %s <%s>
Blog URL: %s
Feed URL: %s
Comments:

%s

--------

%s
    """ % (request.form['about'], request.form['name'], request.form['email'], request.form['blogurl'],
        request.form['feedurl'], request.form['comments'], "\n".join(variables))
    Gmail().send(body=body)
    return "Message sent."

@app.route('/<path:filename>')
def send_static(filename):
     return send_from_directory('static', filename)

def is_spam(request):
    return False
    # if (isset($_SERVER['force_no_vary']) &&
    #     isset($_SERVER['nokeepalive']) &&
    #     isset($_SERVER['ssl_unclean_shutdown']))
    # {
    #     die("You think I'm stupid, bitch?\n");
    # }
    # $shitlist = array(
    #     '203.247.145.10',
    #     '220.226.63.254',
    #     '198.133.178.133',
    #     '206.204.190.33',
    #     '72.232.228.106',
    #     '72.237.17.120',
    #     '93.157.169.18',
    # );
    # if ((array_key_exists('REMOTE_ADDR', $_SERVER) && in_array($_SERVER['REMOTE_ADDR'], $shitlist)) ||
    #     (array_key_exists('HTTP_X_FORWARDED_FOR', $_SERVER) && in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $shitlist)) ||
    #     (array_key_exists('blogurl', $_POST) && preg_match('/(casino|adult|viagra|cialis|valium|lorazepam|tramadol|phentermine|ringtone)/i',$_POST['blogurl'])) ||
    #     (array_key_exists('email', $_POST) && preg_match('/goldfish?ka/i',$_POST['email'])) ||
    #     (array_key_exists('comments', $_POST) && preg_match('/(<a href=\\\?["\']?\s*https?:|goldfishka)/i', $_POST['comments'])) ||
    #     (!empty($_POST['blogurl']) && ($_POST['blogurl'] === $_POST['feedurl'])))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 3000.
    port = int(os.environ.get('PORT', 3000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
