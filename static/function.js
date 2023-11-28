$(document).ready(function () {
  // Socket 관리
  let ws = new WebSocket("ws://localhost:8000/ws");
  // User이름 전역관리
  let username = "";
  
  // #사전작업 DOM Element 저장
  let id = $("#id_content");
  let id_btn = $("#send_id");
  let msg = $("#message");
  let msg_btn = $("send_message");
  let display = $("#display");  
  
  // #0. ID 입력요구
  id.focus();
   
  // #1. ID 저장하기
  id_btn.click(function (event) {
    username = id.val();    
    id.val("");    
    $.getJSON("/chat", update_chats);
  });
  
  // #2. Chat 불러오기
  function update_chats(chats) { 
    if(username != ""){
      if(chats){   
        display.empty();
        chats.forEach(chat => {      
          let text = chat.content.replace(/\n/g, "<br>").concat("<br>");
          let time = get_time(chat.timestamp);
          if(chat.username === username) {                  
            display.append(talk_user_message(text, time));
          }        
          else {                       
            display.append(talk_partner_message(text, time, chat.username));
          }    
          scroll_Top();
          msg.val("");
        })    
      }
    } 
  }

  // #3. Chat 보내기
  $("#send_message").click(function (event) {  
    let text = msg.val();    
    if (text.replace(/\n/g, "").length != 0) {                  
      if(username != ""){                    
        let timestamp = new Date().toISOString();
        let data = {"content": text, "timestamp": timestamp, "username": username};
        $.ajax({
          url: "/chat",
          type: "post",
          contentType: "application/json",
          data: JSON.stringify(data),
          success: function (Data, txtStatus, xhr){            
            ws.send(JSON.stringify(Data));            
          }
        }) 
        
      } 
    }    
  })
  
  // #4. Socket 처리
  ws.onmessage = function(event) {        
    update_chats(JSON.parse(event.data));    
  }; 

  
  // #Keydown (Enter / Shift Enter)
  id.on("keydown", (event) => {
    handle_key_down(event, "#send_id");
  });

  msg.on("keydown", (event) => {
    handle_key_down(event, "#send_message");
  });  

  function handle_key_down(event, element) {
    if (event.keyCode == 13)
      if (!event.shiftKey) {
        event.preventDefault();        
        $(element).click();
        $(this).val("");
      }
  }

  // Chat Display
  function talk_user_message(text, time) {
    return (
      "<div class='talk_user'>" +
      "<div class='time'>" +
      time +
      "</div>" +
      "<div class='chat user'>" +
      text +
      "</div>" +
      "</div>"
    );
  }
  function talk_partner_message(text, time, partername) {
    return (
      "<div class='partner_container'>" +

        "<p>" +
          partername +      
        "</p>" + 

        "<div class='talk_partner'>" +
          "<div class='chat partner'>" +
            text +
          "</div>" +
          "<div class='time'>" +
            time +
          "</div>" +
        "</div>" + 

      "</div>"
    );
  }
  
  function get_time() {
    let currTime = new Date();
    let hour = currTime.getHours();
    let min = currTime.getMinutes();

    let amOrpm = hour >= 12 ? "오후" : "오전";
    if (hour > 12) {
      hour -= 12;
    }
    let formatted_min = min < 10 ? "0" + min : min;
    let time = amOrpm + " " + hour + ":" + formatted_min;
    return time;
  }
  // Chat > Scroll Down
  function scroll_Top() {
    display.scrollTop(display.prop("scrollHeight"));    
  }
});
