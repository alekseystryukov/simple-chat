

jQuery(document).ready(function($) {
    var send_button = $('.send-message-btn'),
    send_message = $('.send-message'),
    name_input = $('.name-input'),
    msg_wrap = $('.msg-wrap'),
    msg_template = $('.msg-template'),
    last_message_id = 0,
    load_messages_timeout = 0;

    send_button.on('click', function(){
        $.post('/chat/send_message/',
            {
                'message': send_message.val(),
                'name': name_input.val(),
            },
            function(){
                if(load_messages_timeout){
                    clearTimeout(load_messages_timeout);
                    load_messages();
                }
            }
        );
        send_message.val('');
    });

    function load_messages(){

        $.get('/chat/get_messages/' + last_message_id + '/',
            function(data){
                if(data.last_message_id){
                    last_message_id = data.last_message_id
                }
                if(data.messages.length){
                    var mess_item;
                    for(var i=0;i<data.messages.length;i++){
                        var mess = data.messages[i];
                        mess_item = msg_template.clone();
                        mess_item.find('.time').append(mess.time);
                        mess_item.find('.media-heading').text(mess.name);
                        mess_item.find('.text').text(mess.message);
                        mess_item.removeClass('msg-template');
                        msg_wrap.append(mess_item);
                    }
                    msg_wrap.get(0).scrollTop = msg_wrap.get(0).scrollHeight;
                }
                load_messages_timeout = setTimeout(load_messages, 1000);
            }, 'json'
        );

    }
    load_messages();

});