import React from "react";

const Message = () => (
  <div className="text-center hero my-5">
    <h1 className="mb-4">Compose your message</h1>

    <p className="lead">
        <p>To</p>
        <input type="text" id="receiver" name="receiver"/>
      <textarea id="msg" name="msgarea" rows="4" cols="50"></textarea>
      <button type="button">Send</button>
    </p>
  </div>
);

export default Message;