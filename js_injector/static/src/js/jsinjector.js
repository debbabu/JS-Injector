odoo.define('js_injector.jsinjector', function (require) {
"use strict";
    var rpc = require('web.rpc');
    rpc.query({
            model: 'js.injector',
            method: 'get_current_user_js',
        }).then(function (result) {
          var group_js_functions = function () {
              eval(result);
            };
            group_js_functions();
        });
});
