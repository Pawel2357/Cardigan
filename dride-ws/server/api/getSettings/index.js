'use strict';

var express = require('express');
var controller = require('./getSettings.controller');

var router = express.Router();


var config = require('../../config/environment');



router.get('/', function(req, res){

 	controller.index(req, res)


 	
});

module.exports = router;