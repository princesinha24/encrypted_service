# -*- coding: utf-8 -*-
"""
Created on Sat May  8 07:31:15 2021

@author: PRINCE SINHA
"""
############################ Import Libraries ############################ 
from flask import Flask, render_template, session, request, redirect, url_for, flash
import sys
from hashlib import sha256
import cv2
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired,length, EqualTo
import hashlib
import random
############################ END ############################ END

############################ hashing function ############################ 
def hashing(pwd):
    hash_pwd = hashlib.sha256(pwd.encode('utf-8'))
    return hash_pwd.hexdigest()
############################ END ############################ END

############################ Image resize function ############################
def resize(path):
    img = cv2.imread(path)
    width = 128
    height = 128
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized
############################ END ############################ END

############################ Password Encryption function ############################ 
def encrypte_img(img,pwd):
    j=0
    hexadecimal = pwd
    end_length = len(hexadecimal) * 4
    
    hex_as_int = int(hexadecimal, 16)
    hex_as_binary = bin(hex_as_int)
    b_pwd = hex_as_binary[2:].zfill(end_length)
    for i in range (img.shape[0]):
        if(b_pwd[j]=='1' and (img[i][0][j%3])%2==0):
            img[i][0][j%3]=img[i][0][j%3]^1
        elif(b_pwd[j]=='0' and (img[i][0][j%3])%2==1):
            img[i][0][j%3]=img[i][0][j%3]^1
        j+=1
        if(b_pwd[j]=='1' and (img[i][127][j%3])%2==0):
            img[i][127][j%3]=img[i][127][j%3]^1
        elif(b_pwd[j]=='0' and (img[i][127][j%3])%2==1):
            img[i][127][j%3]=img[i][127][j%3]^1
        j+=1
    return img
############################ END ############################ END

############################ Key Encryption function ############################ 
def encrypte_key(img,key):
    a=list()
    p=key
    while(p):
        a.append(p%2)
        p=p//2
    for i in range (len(a)):
        if(a[i]==1 and (img[3*i][63][i%3])%2==0):
            img[3*i][63][i%3]=img[3*i][63][i%3]^1
        elif(a[i]==0 and (img[3*i][63][i%3])%2==1):
            img[3*i][63][i%3]=img[3*i][63][i%3]^1
    return img
############################ END ############################ END

############################ Password Decryption function ############################  
def decrypte_img(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    ans=''
    j=0
    s = ""
    for i in range (img.shape[0]):
        ans+=str((img[i][0][j%3])%2)
        j+=1
        ans+=str((img[i][127][j%3])%2)
        j+=1
    return ans
############################ END ############################ END

############################ Key Encryption function ############################ 
def decrypte_key(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    p=1
    key=0
    for i in range (40):
        key = key+(p*(img[3*i][63][i%3]%2))
        p=p*2 
    return key
############################ END ############################ END

############################ binary to string for encrypted mssg############################ 
def bin_str_enc(res):
    mp = {0:'0',
           1:'1',
           2:'2',
           3:'3',
           4:'4',
           5:'5',
           6:'6',
           7:'7',
           8:'8',
           9:'9',
           10:'a',
           11:'b',
           12:'c',
           13:'d',
           14:'e',
           15:'f' }
    ans=list()
    i=0
    while(i<len(res)):
        p=0
        q=8
        j=0
        while(j<4):
            if(res[i]=='1'):
                p+=q
            q=q//2
            i+=1
            j+=1
        ans.append(mp[p])
    return ans;
############################ END ############################ END

############################ binary to string for decrypted mssg ############################ 
def bin_str_dec(res):
    ans=list()
    i=0
    while(i<len(res)):
        p=0
        q=128
        j=0
        while(j<8):
            if(res[i]=='1'):
                p+=q
            q=q//2
            i+=1
            j+=1
        if p==0:
            break
        else:
            ans.append(chr(p))
    return ans;
############################ END ############################ END

############################ hexa to binary ############################ 
def hex_bin(d):
    mp = {'0' : "0000", 
              '1' : "0001",
              '2' : "0010", 
              '3' : "0011",
              '4' : "0100",
              '5' : "0101", 
              '6' : "0110",
              '7' : "0111", 
              '8' : "1000",
              '9' : "1001", 
              'a' : "1010",
              'b' : "1011", 
              'c' : "1100",
              'd' : "1101", 
              'e' : "1110",
              'f' : "1111" }
    b=''
    for i in range (len(d)):
        b+=mp[d[i]]
    return b
############################ Msseage Encryption ############################
def encryption_mssg(key,word):
    lt=[]
    rt=[]
    for i in range (256):
        lt.append(word[i])
        rt.append(word[i+256])
    j=0
    while(j<16):
        if j%2==0:
            for i in range (len(rt)):
                if (lt[i]=='0' and key[i]=='1') or (lt[i]=='1' and key[i]=='0'):
                    if(rt[i]=='0'):
                        rt[i]='1'
                    else:
                        rt[i]='0'
        else:
            for i in range (len(lt)):
                if (rt[i]=='0' and key[i]=='1') or (rt[i]=='1' and key[i]=='0'):
                    if(lt[i]=='0'):
                        lt[i]='1'
                    else:
                        lt[i]='0'
        for i in range (16):
            k=(i-16+256)%256
            p=key[i]
            while(1):
                key[k],p=p,key[k]
                k=(k-16+256)%256
                if(k==i):
                    break
            key[i]=p
        j+=1
    for i in range (len(rt)):
        lt.append(rt[i])
    return lt
############################ END ############################ END

############################ Msseage Decryption ############################
def decryption_mssg(key,word):
    lt=[]
    rt=[]
    for i in range (256):
        lt.append(word[i])
        rt.append(word[i+256])
    j=0
    
    while(j<16):
        for i in range (16):
            k=i+16
            p=key[i]
            while(1):
                key[k],p=p,key[k]
                k=(k+16)%256
                if(k==i):
                    break
            key[i]=p
        if j%2==1:
            for i in range (len(rt)):
                if (lt[i]=='0' and key[i]=='1') or (lt[i]=='1' and key[i]=='0'):
                    if(rt[i]=='0'):
                        rt[i]='1'
                    else:
                        rt[i]='0'
        else:
            for i in range (len(lt)):
                if (rt[i]=='0' and key[i]=='1') or (rt[i]=='1' and key[i]=='0'):
                    if(lt[i]=='0'):
                        lt[i]='1'
                    else:
                        lt[i]='0'
        
        j+=1
    for i in range (len(rt)):
        lt.append(rt[i])
    return lt
############################ END ############################ END

app = Flask(__name__)

############################ Database Connection ############################
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="crypt"
mysql=MySQL(app)
prime_no=9999999967
add_no=549755813888
alpha=56711
############################ END ############################ END

############################ Some Forms ############################ 
class LoginForm(FlaskForm):
    username = StringField(label='User Id',validators=[length(min=1,max=255), DataRequired()] )
    password = PasswordField(label='Password',validators=[length(min=1,max=255), DataRequired()])
    submit = SubmitField(label='SignIn')
    
class SigninForm(FlaskForm):
    userid = StringField(label='User Id',validators=[length(min=1,max=255), DataRequired()])
    emailid = StringField(label='Email Id',validators=[length(min=1,max=255), DataRequired()])
    username = StringField(label='Username',validators=[length(min=1,max=255), DataRequired()])
    image=FileField(label='Upload Your image (size must be greater than 128x128)', validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[length(min=1,max=255), DataRequired()])
    confirm = PasswordField(label='Confirm Password',validators=[length(min=1,max=255), DataRequired()])
    submit = SubmitField(label='SignIn')
    
class mssgForm(FlaskForm):
    reply1=StringField(label='reply',validators=[length(min=1,max=1000), DataRequired()])
    submit = SubmitField(label='Send')
############################ END ############################ END
 
############################ Public key ############################ 
def public_key(p,key1,prime_no):
    p_key=1
    q=p
    m=key1
    while(m):
        if(m%2==1):
            p_key=(p_key*q)%prime_no
        m=m//2
        q=(q*p)%prime_no   
    c=str(p_key)
    return c
############################ END ############################ END   
     
############################ Encrypt Message ############################ 
def encrypt_mssg(mssg,key):
    r=str(key)
    enc_key=hashing(r)
    print(enc_key)
    return 1
############################ END ############################ END   
    

############################ for login ############################ 
@app.route("/")
def fun(mssg=0):
    form=LoginForm()
    return render_template('login.html', form=form,a=mssg) 
############################ END ############################ END

############################ for new user ############################ 
@app.route("/new")
def new_user(mssg=0):
    form=SigninForm()
    return render_template('new_user.html',form=form,a=mssg)
############################ END ############################ END

############################ user ############################
@app.route("/user/<name>")
def profile(name):
    if(session['id']!=None):
        img=cv2.imread('C:/Users/PRINCE SINHA/cryptography/static/Images/'+name+'.jpg')
        n=decrypte_key(session['path'])
        session['pr_key']=str(n-add_no)
        width=int((256*img.shape[1])/img.shape[0])
        cur=mysql.connection.cursor()
        sql=cur.execute("select friend from friend_list where user_id='"+session['id']+"'  ")
        items=[]
        if sql:
            detail=cur.fetchall()
            for i in range (len(detail)):
                img=cv2.imread('C:/Users/PRINCE SINHA/cryptography/static/Images/'+detail[i][0]+'.jpg')
                width1=int((50*img.shape[1])/img.shape[0])
                items.append({'id':detail[i][0],'wt':width1})
        cur.close()
        session['key']=None
        return render_template('user.html', name=session['name'],image=name, ht=width,ids=session['id'],items=items)
        
    else:
        flash ("You are not logged in Please login again")
        return redirect(url_for('fun'))
############################ END ############################ END
 
############################ Login form ############################
@app.route('/', methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        if form.errors =={}:
            userid=request.form['username']
            pwd = request.form['password']
            mssg=1
            cur=mysql.connection.cursor()
            com='select path,user_name from user where user_id="'+userid+'"'
            sql=cur.execute(com)
            if(sql==0):
                return fun(2)
            else:
                path=cur.fetchone()
                ans=hashing(pwd)
                hexadecimal = ans
                end_length = len(hexadecimal) * 4
                
                hex_as_int = int(hexadecimal, 16)
                hex_as_binary = bin(hex_as_int)
                b_pwd = hex_as_binary[2:].zfill(end_length)
                ans=decrypte_img(path[0])
                if(ans!=b_pwd):
                    return fun(2)
                else:
                    session['path']=path[0]
                    session['name']=path[1]
                    session['id']=userid
                    return redirect(url_for('profile',name=session['id']))
        else:
            return render_template('login.html', form=form,a=1)
############################ END ############################ END

############################ For register Form ############################         
@app.route("/new",methods=['GET','POST'])
def register():
    form=SigninForm()
    if form.validate_on_submit():
        userid=request.form['userid']
        emailid=request.form['emailid']
        username=request.form['username']
        image=request.form['image']
        password=request.form['password']
        confirm=request.form['confirm']
        if form.errors =={}:
            if password!=confirm:
                return new_user(1)
            else:
                cur=mysql.connection.cursor()
                sql=cur.execute("select user_id from user where email_id='"+emailid+"'")
                cur.close()
                if(sql):
                    return new_user(2)
                else:
                    cur=mysql.connection.cursor()
                    sql=cur.execute("select email_id from user where user_id='"+userid+"'")
                    cur.close()
                    if(sql):
                        return new_user(3)
                    else:
                        while(1):
                            n = (random.random())*prime_no
                            n=round(n)
                            if n>7 or n<=prime_no-8:
                                break
                        p_key=public_key(alpha, n, prime_no)
                        n=n+add_no
                        key=n
                        pwd=hashing(password)
                        img = cv2.imread('C:/Users/PRINCE SINHA/cryptography/Images/'+image)
                        path1='C:/Users/PRINCE SINHA/cryptography/static/Images/'+userid+'.jpg'
                        cv2.imwrite(path1,img)
                        output=resize(path1)
                        output=encrypte_img(output, pwd)
                        output=encrypte_key(output, key)
                        path='C:/Users/PRINCE SINHA/cryptography/static/hidden_image/'+userid+'.png'
                        cv2.imwrite(path,output) 
                        cur=mysql.connection.cursor()
                        sql=cur.execute("insert into user (user_id,email_id,path,user_name,public_key) values('"+userid+"','"+emailid+"','"+path+"','"+username+"','"+p_key+"')")
                        if(sql):
                            mysql.connection.commit()
                            cur.close()
                            flash('Registration Complete')
                            return redirect(url_for('fun'))
                        else:
                            return new_user(4)

        else:
            return new_user(4)
                
    return render_template('new_user.html', form=form)
############################ END ############################ END  
  
############################ Log out ############################
@app.route("/logout")
def log_out():
    session['id']=None
    session['pr_key']=None
    session.pop('path',default=None)
    session.pop('name',default=None)
    return redirect(url_for('fun'))
############################ END ############################ END   

############################ Friend Request ############################
@app.route("/friend_request")
def f_req():
    cur=mysql.connection.cursor()
    sql=cur.execute("select user_id from request where request_to = '"+session['id']+"'")
    
    if sql==0:
        cur.close()
        cur=mysql.connection.cursor()
        sql=cur.execute("select user_id from user where not (user_id='"+session['id']+"' OR user_id in (select user_id from request where request_to='"+session['id']+"') OR user_id in (select request_to from request where user_id='"+session['id']+"') OR user_id in (select user_id from friend_list where friend='"+session['id']+"')) ")
        detail=cur.fetchall()
        items=[]
        for i in range (len(detail)):
            img=cv2.imread('C:/Users/PRINCE SINHA/cryptography/static/Images/'+detail[i][0]+'.jpg')
            width1=int((50*img.shape[1])/img.shape[0])
            items.append({'id':detail[i][0],'wt':width1})
        return render_template('request.html',a=1,name=session['name'],items=items, ids=session['id'] )
    else:
        res=cur.fetchall()
        req_get=[]
        for i in range (len(res)):
            req_get.append(res[i][0])
        cur.close()
        cur=mysql.connection.cursor()
        sql=cur.execute("select user_id from user where not (user_id='"+session['id']+"' OR user_id in (select user_id from request where request_to='"+session['id']+"') OR user_id in (select request_to from request where user_id='"+session['id']+"') OR user_id in (select user_id from friend_list where friend='"+session['id']+"')) ")
        detail=cur.fetchall()
        items=[]
        for i in range (len(detail)):
            img=cv2.imread('C:/Users/PRINCE SINHA/cryptography/static/Images/'+detail[i][0]+'.jpg')
            width1=int((50*img.shape[1])/img.shape[0])
            items.append({'id':detail[i][0],'wt':width1})
        return render_template('request.html',a=2,name=session['name'],items=items, req_get=req_get, ids=session['id'] )
############################ END ############################ END  

############################ Friend Request ############################
@app.route("/friend_request",methods=['GET','POST'])
def respond():
    if request.method=="POST":
        print("no")
        user=request.form['req_id']
        cur=mysql.connection.cursor()
        sql=cur.execute("Insert into friend_list (user_id,friend) values('"+session['id']+"','"+user+"')")
        if sql:
            mysql.connection.commit()
            cur.close()
            cur=mysql.connection.cursor()
            sql=cur.execute("Insert into friend_list (user_id,friend) values('"+user+"','"+session['id']+"')")
            mysql.connection.commit()
            cur.close()
            cur=mysql.connection.cursor()
            sql=cur.execute("Delete from request where request_to='"+session['id']+"' and user_id = '"+user+"'")
            mysql.connection.commit()
            cur.close()
            flash('request accepted')
        else:
            cur.close()
            flash('some error occured')
        return redirect(url_for('f_req'))
############################ END ############################ END  
 
############################ Add Friend ############################
@app.route("/friend_request1",methods=['GET','POST'])
def frd_request():
    if request.method=="POST" :
        print('Yes')
        user=request.form['add_id']
        cur=mysql.connection.cursor()
        sql=cur.execute("Insert into request (user_id,request_to) values('"+session['id']+"','"+user+"')")
        if sql:
            mysql.connection.commit()
            cur.close()
            flash('request sent')
        else:
            cur.close()
            flash('some error occured')
        return redirect(url_for('f_req'))
############################ END ############################ END  
 

############################ user ############################
@app.route("/user",methods=['GET','POST'])
def send_mssg():
    if request.method=="POST":
        frd_id=request.form['id_frd']
        session['friend']=frd_id
        cur=mysql.connection.cursor()
        sql=cur.execute("select public_key from user where user_id = '"+session['friend']+"'")
        detail=cur.fetchone()
        pb_key=int(detail[0])
        cur.close()
        pr_key=int(session['pr_key'])
        key=public_key(pb_key, pr_key, prime_no)
        d=hashing(key)
        session['key']=hex_bin(d)
        print(session['key'])
        return redirect(url_for('print_mssg'))
############################ END ############################ END

############################ user ############################
@app.route("/message")
def print_mssg():
    form=mssgForm()
    cur=mysql.connection.cursor()
    sql=cur.execute("select mssg,sender from message where (sender='"+session['id']+"' and receiver='"+session['friend']+"') OR(sender='"+session['friend']+"' and receiver='"+session['id']+"')")
    items=[]
    if sql!=0:
        details=cur.fetchall()
        for i in range (len(details)):
            check= hex_bin(details[i][0])
            check=list(check)
            b=list(session['key'])
            mssg1=''
            for k in range (len(check)//512):
                word=check[k*512:(k+1)*512]
                ans=decryption_mssg(b, word)
                ans=bin_str_dec(ans)
                for j in range (len(ans)):
                    mssg1+=ans[j] 
            if(details[i][1]==session['id']):
                items.append({'id':'1','message':mssg1})
            else:
                items.append({'id':'2','message':mssg1})
    cur.close()
    return render_template('message.html', friend=session['friend'],name=session['name'],ids=session['id'],items=items,form=form)
############################ END ############################ END
  

############################ write message ############################
@app.route("/message",methods=['GET','POST'])
def reply():
    form=mssgForm()
    if form.validate_on_submit():
        message1=request.form['reply1']
        res = ''.join(format(ord(i), '08b') for i in message1)
        md=(len(res))%(512)
        md=(512-md)%512
        b=list(session['key'])
        for i in range(md):
            res=res+'0'
        res=list(res)
        check=""
        for i in range (len(res)//512):
            word=res[i*512:(i+1)*512]
            ans=encryption_mssg(b, word)
            ans=bin_str_enc(ans)
            for j in range (len(ans)):
                check+=ans[j]
        cur=mysql.connection.cursor()
        sql=cur.execute("insert into message (sender,receiver,mssg) value('"+session['id']+"','"+session['friend']+"','"+check+"')")
        if(sql):
            mysql.connection.commit()
        cur.close()
    return redirect(url_for('print_mssg'))
############################ END ############################ END
 
@app.route("/content/"+"<username>")
def home(username):
    return f'<h1>hola {username}</h1>'





if __name__ == '__main__':
   app.run(debug = True)