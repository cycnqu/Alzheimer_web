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