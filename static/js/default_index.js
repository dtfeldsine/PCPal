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
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};
    
    self.cpu_list_func = function () {
       console.log("in cpu_list");
       $.getJSON(cpu_list_url, function (data) {
           self.vue.cpu_list = data.cpu_list;
           enumerate(self.vue.search_list);
       })
    };
    self.gpu_list_func = function () {
       console.log("in gpu_list");
       $.getJSON(gpu_list_url, function (data) {
           self.vue.gpu_list = data.gpu_list;
       })
    };
    self.mem_list_func = function () {
       console.log("in mem_list");
       $.getJSON(mem_list_url, function (data) {
           self.vue.mem_list = data.mem_list;
       })
    };
    self.mobo_list_func = function () {
       console.log("in mobo_list");
       $.getJSON(mobo_list_url, function (data) {
           self.vue.mobo_list = data.mobo_list;
       })
    };
    self.hdd_list_func = function () {
       console.log("in hdd_list");
       $.getJSON(hdd_list_url, function (data) {
           self.vue.hdd_list = data.hdd_list;
       })
    };
    self.psu_list_func = function () {
       console.log("in psu_list");
       $.getJSON(psu_list_url, function (data) {
           self.vue.psu_list = data.psu_list;
       })
    };
    self.case_list_func = function () {
       console.log("in case_list");
       $.getJSON(case_list_url, function (data) {
           self.vue.case_list = data.case_list;
       })
    };
    
    
    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            cpu_list: [],
            gpu_list: [],
            mem_list: [],
            mobo_list: [],
            hdd_list: [],
            psu_list: [],
            case_list: [],
            logged_in: false,
            user_email: null,
        },
        methods: {
            cpu_list_func: self.cpu_list_func,
            gpu_list_func: self.gpu_list_func,
            mem_list_func: self.mem_list_func,
            mobo_list_func: self.mobo_list_func,
            hdd_list_func: self.hdd_list_func,
            psu_list_func: self.psu_list_func,
            case_list_func: self.case_list_func,
        }

    });

    self.cpu_list();
    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
