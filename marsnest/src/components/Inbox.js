import React from "react";
import "./Message.css";

const Inbox = ({msgs}) => (
    msgs.map(msg => (
        <div key={msg.sender_id} className="list-group">
            <br/>
            <div className="list-group-item list-group-item-action">
                <div className="d-flex w-100 justify-content-between">
                <h5 className="mb-1">Subject</h5>
                <small>3 days ago</small>
                </div>
                <p className="mb-1">{msg.message}</p>
                <small>{msg.sender_id}</small>
            </div>
        </div>  
      )
    )
);

export default Inbox;