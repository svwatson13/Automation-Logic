var express = require('express');
var app = express();

app.set('view engine' , 'ejs');

app.set('views','/vagrant/app/views');

app.set('index','/vagrant/app/views');

app.use(express.static('/vagrant/app/public'));

app.get('/' , function(req , res){

  res.render("index");

});

app.listen(3000);
