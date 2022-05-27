# Alzheimer_web
## gitignore 
```env/*```
```media/*```
```images/*```
```models/*```
## goal 
* upload page
* predict page(predict success and show on html)
* list_all page(can filter and search )
* login & logout & sign up 
* connecting with nginx
* GCP server and domain name
## pip install 
* pillow
* tensorflow
* django-allauth
* celery
* django-celery-results
# login & logout & sign up 
## sign up
* password need eng+num and total >8
* can email to user's gmail 4/11 AAA
* add email template.html 4/11 AAA 
## sign in
* can superuser
* github login success (token to 35.197.74.137)
* google login success (token to 35.197.74.137)test 4/11 AAA
## index
* can use contact form (api data-sb-form-api-token) 4/11 AAA =>https://startbootstrap.com/account/forms
## 4/12 request
* predict progress bar
* login logout register response
* ssl nginx
* upload listall predict  美編
* ppt word 
* web testing
* predict tag 
* image post
* account manage
## 4/13 do 
* add upload tag
* fixed login logout register response
## celery
* redis 
* celery -A Alzheimer_web worker -l info
## lazy page
* pip install lazypage
* find the html
``` open module lazypage
/templates/lazepage/loading.html 
```
* edit like this
```
<!DOCTYPE html>
<html>
<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0">
  <title>Lazy Loading</title>
  <style>

    .previous {
        box-sizing: border-box;
        width: 2em;
        height: 2em;
        border: .2em solid #000;
        border-radius: 50%;
        position: fixed;
        left: 10px;
        top: 10px;
    }
    .previous:before {
        box-sizing: border-box;
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-top: auto;
        margin-bottom: auto;
        margin-left: -.65em;
        width: 0;
        height: 0;
        border-top: .45em solid transparent;
        border-bottom: .45em solid transparent;
        border-right: .6em solid #000;
    }
    .previous:after {
        box-sizing: border-box;
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-top: auto;
        margin-bottom: auto;
        margin-left: -.2em;
        width: 0;
        height: 0;
        border-top: .45em solid transparent;
        border-bottom: .45em solid transparent;
        border-right: .6em solid #000;
    }
    .loader{
      position: fixed;
      width: 200px;
      height: 200px;
      left: 50%;
      top: 50%;
      margin-left: -100px;
      margin-top: -100px;
    }
    .error{
      position: relative;
      top: 40px;
      left: 40px;
    }
    .info{
      position: fixed;
      bottom: 30px;
    }
    .info span{
      color: #ffe691;
    }
    a {
      text-decoration: none;
      color: gray;
    }
  </style>
</head>

<body>
  <h1 style="color: black;text-align: center;">Thank you for your patience</h1>
  <a href="#" onclick="history.back(-1);" class="previous">&nbsp;&nbsp;&nbsp;&nbsp;</a>

  {% if url %}

      {% if error_msg %}
        <div class="error">
            {{ error_msg|linebreaksbr }}
        </div>
      {% else %}
        <div class="loader" title="ttl: {{ ttl }}">
          <svg width="200px"  height="200px"  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid" class="lds-cube" style="background: none;"><g transform="translate(25,25)"><rect ng-attr-x="{{config.dp}}" ng-attr-y="{{config.dp}}" ng-attr-width="{{config.blockSize}}" ng-attr-height="{{config.blockSize}}" ng-attr-fill="{{config.c1}}" x="-17.5" y="-17.5" width="35" height="35" fill="#ffb6bb" transform="scale(1.2581 1.2581)"><animateTransform attributeName="transform" type="scale" calcMode="spline" values="1.5;1" keyTimes="0;1" dur="1s" keySplines="0 0.5 0.5 1" begin="-0.3s" repeatCount="indefinite"></animateTransform></rect></g><g transform="translate(75,25)"><rect ng-attr-x="{{config.dp}}" ng-attr-y="{{config.dp}}" ng-attr-width="{{config.blockSize}}" ng-attr-height="{{config.blockSize}}" ng-attr-fill="{{config.c2}}" x="-17.5" y="-17.5" width="35" height="35" fill="#ffe691" transform="scale(1.35895 1.35895)"><animateTransform attributeName="transform" type="scale" calcMode="spline" values="1.5;1" keyTimes="0;1" dur="1s" keySplines="0 0.5 0.5 1" begin="-0.2s" repeatCount="indefinite"></animateTransform></rect></g><g transform="translate(25,75)"><rect ng-attr-x="{{config.dp}}" ng-attr-y="{{config.dp}}" ng-attr-width="{{config.blockSize}}" ng-attr-height="{{config.blockSize}}" ng-attr-fill="{{config.c3}}" x="-17.5" y="-17.5" width="35" height="35" fill="#95d5ee" transform="scale(1.0073 1.0073)"><animateTransform attributeName="transform" type="scale" calcMode="spline" values="1.5;1" keyTimes="0;1" dur="1s" keySplines="0 0.5 0.5 1" begin="0s" repeatCount="indefinite"></animateTransform></rect></g><g transform="translate(75,75)"><rect ng-attr-x="{{config.dp}}" ng-attr-y="{{config.dp}}" ng-attr-width="{{config.blockSize}}" ng-attr-height="{{config.blockSize}}" ng-attr-fill="{{config.c4}}" x="-17.5" y="-17.5" width="35" height="35" fill="#585872" transform="scale(1.00084 1.00084)"><animateTransform attributeName="transform" type="scale" calcMode="spline" values="1.5;1" keyTimes="0;1" dur="1s" keySplines="0 0.5 0.5 1" begin="-0.1s" repeatCount="indefinite"></animateTransform></rect></g></svg>
        </div>

      {% endif %}


      <div class="info">
        <a style="color: black;" href="{{request.scheme}}://{{request.get_host}}{{ url }}">{{request.scheme}}://{{request.get_host}}{{ origin_url }}</a>
        <span style="color: black;">
            {% if error_msg %}
              Load Failed!
            {% else %}
            Is Loading...
            
              <script>
                  setTimeout(function () {
                      top.location.reload()
                  }, '{{ polling_seconds }}' * 1000)
              </script>
              
            {% endif %}
        </span>
       <!-- <div id="counter">00:00:00.000</div>
        <script>
          startTime = Date.now();
          intervalId = setInterval(updateCounter, 15);
          function updateCounter() {
              let currentTime = Date.now();
              let msecond = ("0" + (currentTime - startTime) % 1000).substr(-3, 3);
              let counter = Math.floor((currentTime - startTime)/1000);
              let hour = ("0" + Math.floor(counter / 3600)).substr(-2, 2);
              let minute = ("0" + Math.floor((counter % 3600) / 60)).substr(-2, 2);
              let second = ("0" + Math.floor(counter % 60)).substr(-2, 2);
              document.getElementById('counter').textContent = `${hour}:${minute}:${second}.${msecond}`;
          }
        </script>
      </div>
      -->

      
  {% else %}
      <p>
        Page Not Found Or Expired!
      </p>
  {% endif %}
```
# 20220527 
## allauth html modify
* ```Lib\site-packages\allauth\templates\account\base.html```
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
* Lib\site-packages\allauth\templates\socialaccount\login.html
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
