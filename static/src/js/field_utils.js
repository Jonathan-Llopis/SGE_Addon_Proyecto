odoo.define('gestion.zoo.field_utils', function (require) {
    "use strict";

    var fieldUtils = require('web.field_utils');

    fieldUtils.format.badge = function (value, field) {
        var color_map = {
            'macho': 'background-color: blue; color: white;',
            'hembra': 'background-color: pink; color: white;',
        };
        return {
            className: 'badge',
            style: color_map[value] || 'background-color: gray; color: white;',
            text: fieldUtils.format.char(value, field),
        };
    };
});