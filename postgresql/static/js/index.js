

$(".btn_alert").click(function(){
    text = document.getElementById('input_text').value;
    socket.emit( 'test_alert', {in_text:text, date:'15/5/2015' });
});

socket.on('back_test_alert', function(msg){
    $('#back_msg').text(msg);
});