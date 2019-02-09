odoo.define('group_js.costume', function (require) {
"use strict";
    var Model = require('web.Model');
    var model=new Model("js.injector");
    model.call("get_current_user_js").done(function(result){
      var group_js_functions = function () {
        eval(result);
      };
      group_js_functions();
    });
});
