# Alzheimer_web
## gitignore 
```env/*```
```media/*```
## goal 
* upload page(preview and upload success)
* predict page(predict success and show on html)
* list_all page(can filter and search )
* login & logout & sign up 
* connecting with nginx
* GCP server and domain name
## pip install 
* pillow
* tensorflow
* django-allauth
# sign up
* password need eng+num and total >8

## 4/12
* 改註冊與登入頁面抱錯:主要更改位置view.py(sign_in)register.html&login.html 參考資料:https://www.796t.com/post/YWRhOXM=.html
* 新增icon(google&github)
* form 增加'placeholder'屬性


Alzheimer_web/
    manage.py
    Alzheimer_web/
    login/
    upload/
    predict/
    media/
    static/
        css/
        js/
        img/
    templates/
        base.html
        index.html
        listall.html
        login.html
        predict.html
        register.html
        signup_success_email.html
        upload.html

## 5/27
* 路徑:D:\python\Lib\site-packages\allauth\templates\account\base.html
```
<!DOCTYPE html>
<html>
  <head>
    <title>{% block head_title %}{% endblock %}</title>
    {% block extra_head %}
    {% endblock %}
    <style>
      .block {
        height: 500px;
        width: 700px;
        position: absolute;     /*絕對位置*/
        top: 50%;               /*從上面開始算，下推 50% (一半) 的位置*/
        left: 50%;              /*從左邊開始算，右推 50% (一半) 的位置*/
        margin-top: -250px;     /*高度的一半*/
        margin-left: -350px;    /*寬度的一半*/
     
    }
    *,
*:before,
*:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  min-height: 100vh;
  display: grid;
  grid-template-rows: 1;
  align-content: center;
  justify-content: center;
  padding: 4rem;
}
a {
  position: absolute;
  transform: translate(-50%, -50%);
  color: #cecd24;
  text-decoration: none;
  font-size: 2em;
  display: inline-block;
  font-family: Montserrat;
  text-transform: uppercase;
  padding: 0.5em 2em;
  border: 2px solid #cecd24;
  transition: 0.02s 0.2s cubic-bezier(0.1, 0, 0.1, 1);
}
a::before {
  content: "";
  display: inline-block;
  position: absolute;
  top: 0;
  left: 0;
  right: 100%;
  bottom: 0;
  background: #cecd24;
  transition: 0.3s 0.2s cubic-bezier(0.1, 0, 0.1, 1), left 0.3s cubic-bezier(0.1, 0, 0.1, 1);
  z-index: -1;
}
a::after {
  content: "";
  display: inline-block;
  background-image: url("https://cdn-icons-png.flaticon.com/128/109/109617.png");
  position: absolute;
  top: 0;
  left: calc(100% - 3em);
  right: 3em;
  bottom: 0;
  background-size: 1.5em;
  background-repeat: no-repeat;
  background-position: center;
  transition: right 0.3s cubic-bezier(0.1, 0, 0.1, 1);
}
a:hover {
  padding: 0.5em 3.5em 0.5em 0.5em;
}
a:hover::before {
  left: calc(100% - 3em);
  right: 0;
  transition: 0.3s cubic-bezier(0.1, 0, 0.1, 1), left 0.3s 0.2s cubic-bezier(0.1, 0, 0.1, 1);
}
a:hover::after {
  right: 0;
  transition: right 0.3s 0.2s cubic-bezier(0.1, 0, 0.1, 1);
}

figure {
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-width: 100%;
  width:  800px;
  height: 500px;
  position: relative;
  padding: calc(1vw + 3rem);
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 378 373' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3.452 2.821l-3.171 367.05c125.311 2.569 250.666 2.673 376.055.905l.84-370.289c-124.617-.622-249.191.172-373.724 2.334z' fill='url(%23a)' /%3E%3Cdefs%3E%3ClinearGradient id='a' x2='1' gradientUnits='userSpaceOnUse' gradientTransform='matrix(377.176 -.281 .281 377.176 .281 .281)'%3E%3Cstop offset='0' stop-color='%23efeef3' /%3E%3Cstop offset='1' stop-color='%23E5E8ED' /%3E%3C/linearGradient%3E%3C/defs%3E%3C/svg%3E%0A") center / cover no-repeat;
}

figure:before, 
figure:after {
  content: '';
  position: absolute;
  z-index: -1;
  right: 0;
  bottom: 0;
}

figure:before {
  filter: blur(12px);
  width: calc(100% - 40px);
  height: calc(100% - 40px);
  background: radial-gradient(ellipse at center, rgba(0, 0, 0, .25) 75%, rgba(0, 0, 0, .1) 80%);
  transform: skew(-7deg, -6deg) translate(0);
}

figure:after {
  filter: blur(2px);
  width: calc(100% - 20px);
  height: calc(100% - 20px);
  background: rgba(0, 0, 0, .25);
  transform: skew(.75deg, 1deg) translate(-1px, -8px);
}

figure img {
  width: 100%;
  height: auto;
  border-radius: 3px;
  vertical-align: middle;
}

figure figcaption {
  font-family: 'Courier', sans-serif;
  font-size: 12px;
  padding: 1rem 0;
}

@media (max-width: 36rem) {
  
  body {
    padding: 9vw;
  }
  
  figure {
    width: calc(100vw - 8rem);
    height: calc(100vw - 8rem);
    padding: 9vw;
  }
  
  figure figcaption {
    padding: 2.5vw 0;
  }
}

    </style>
  </head>
  <body>
    {% block body %}

    {% if messages %}
    <div>
      <strong>Messages:</strong>
      <ul>
        {% for message in messages %}
        <li>{{message}}</li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}

    {% block content %}
    {% endblock %}
    {% endblock %}
    {% block extra_body %}
    {% endblock %}
  </body>
</html>
```
* 路徑:D:\python\Lib\site-packages\allauth\templates\socialaccount\login.html
```
{% extends "socialaccount/base.html" %}
{% load i18n %}
{% block content %}
<figure>
    {% if process == "connect" %}
    <font size=6 >{% blocktrans with provider.name as provider %}Connect {{ provider }}{% endblocktrans %}</font>

    <p>{% blocktrans with provider.name as provider %}You are about to connect a new third party account from {{ provider }}.{% endblocktrans %}</p>
    {% else %}
    <p style=" font-size: 5em;text-align:center;">{% blocktrans with provider.name as provider %}登入 {{ provider }}{% endblocktrans %}</p>

    <p style=" font-size: 2em;text-align:center;">{% blocktrans with provider.name as provider %}You are about to sign in using a third party account from {{ provider }}.{% endblocktrans %}</p>
    {% endif %}
    </br>
    </br>
    <form method="post">
      {% csrf_token %}
      <button type="submit" id="foot"><a>BUTTON</a></button>
    </form>
</figure>
{% endblock %}

```
