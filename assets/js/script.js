function submit(page) {
var xhr = new XMLHttpRequest();
xhr.open('get', 'http://0.0.0.0:8080/' + page, true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
xhr.send();
}
