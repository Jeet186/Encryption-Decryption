from flask import Flask, render_template, request
import os

app = Flask(__name__)
# picfolder=os.path.join('static','Images')

# app.config['UPLOAD_FOLDER'] = picfolder


@app.route('/')
def home():
    return render_template('HomePage.html')

@app.route('/Encryption')
def encrypt():
    return render_template('Encryption.html')

@app.route('/Decryption')
def decrypt():
    return render_template('Decryption.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Encryption', methods=['POST'])
def getdata_enc():
    source_name = request.form['source_name']
    import base64
    data = bytes(source_name, 'utf-8')
    encoded_data = base64.b64encode(data)
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    cover_name = request.form['cover_name']
    new_img_name = request.form['new_name']

    from base_enc import base_enc
    base_enc(source_name)
 
    from rsa_enc import call_rsa
    call_rsa(p, q, encoded_data)
 
    import stego_enc
    cover_name = os.path.dirname(os.path.abspath(__file__))+'/static/coverimages/'+cover_name
    stego_enc.encode(cover_name, new_img_name)
    return render_template('ThankYou.html')

@app.route('/Decryption', methods=['POST'])
def getdata_dec():
    cover_name = request.form['cover_name']
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    new_cover_name = request.form['new_cover_name']
 
    import stego_dec
    stego_dec.decode(cover_name)
 
    import rsa_dec
    rsa_dec.rsa_dec(p,q)
 
    import base_dec
    base_dec.base_dec(new_cover_name)
    return render_template('ThankYou.html')

if __name__ == '__main__':
    app.run(debug=True)