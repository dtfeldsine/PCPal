// This is the js for the default/index.html view.

var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            cpu_list: [${CPU_1}, ${CPU_2}, ${CPU_3}, ${CPU_4}, ${CPU_5}],
            gpu_list: [],
            mem_list: [],
            mobo_list: [],
            hdd_list: [],
            case_list: [],
            psu_list: [],
            logged_in: false,
            user_email: null,
        },
        methods: {
        }

    });


    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
