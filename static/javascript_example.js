// Create an sse emiter client

function connect_sse_emitter() {
    let sse;
    try {
        let prefix = 'https://';
        if (window.location.port !== '443') {
            prefix = 'http://';
        }
        sse = new EventSource(prefix + window.location.hostname + ":" + window.location.port + "/api/sse");
    } catch (e) {
    }

    sse.onmessage = function(msg_event) {
        let msg = msg_event.data;
        if (typeof msg === 'string') {
            if (msg !== '') {
                try {
                    document.getElementById("messages").innerHTML = '<b>sse message:</b><small>&nbsp;&nbsp;' + msg + '</small>';
                } catch (e) {
                }
            }
        }
    };

    sse.onerror = function() {
        sse.close();
        sse = null;
        setTimeout(function() {
            connect_sse_emitter();
        }, 500);
    };
}

// Start the SSE emitter client 1 second after page loading

setTimeout(function() {
    connect_sse_emitter();
}, 1000);

// Load the body of a page (single page application) into the current page
// prevent reloading of javascript and loosing scope

let current_page;
get_page_body = function (url, evaluate) {
    let prefix = 'https://';
    if (window.location.port !== '443') {
        prefix = 'http://';
    }

    current_page = prefix + window.location.hostname + ":" + window.location.port  + url;

    $.ajax({
        type: "GET",
        url: current_page,
        success: function (result) {
            document.getElementById("page_body").innerHTML = result;
        }
    });
    current_page = url;
};

// Load the landing page only once on first load
function Once(){
    console.log("Initializing with /home");
    get_page_body('/home');
    Once = function(){};
}
Once();
