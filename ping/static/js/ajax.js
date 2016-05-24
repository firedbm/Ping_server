function deleteS(id){
	$.ajax({
type: 'POST',
url: "/ping/ajax/delete/",
dataType: "json",
 data:{
'id':id
},
success: function(data) {

	alert("url was success delete");

},
error:function(){
	
}
});
};
    setInterval(function refresh(){
      $.ajax({
type: 'GET',
url: "/ping/ajax/",
success: function (data) {
$('#datatable tbody').empty();
$.each(data['server'], function (i, item){
$('#datatable').append(
'<tr>' +
'<td>' + item[1] + '</td>' +
'<td>' + item[2] + '</td>' +
'<td>'+'<a  onclick="deleteS(' + "'" + item[0] + "'" + ')" class="btn btn-warning waves-effect waves-light">Delete</a>'+'</td>'+
'</tr>'
);
});
},
error: function () {
alert("error");
}
})
    }, 1000);
    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 
