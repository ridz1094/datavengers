import React, { useState, useEffect } from "react";
import "./Message.css";
import ComposeMail from "./ComposeMail"
import Inbox from "./Inbox"
import {
  BrowserRouter,
  Route,
  Link,
} from "react-router-dom";

import { useAuth0 } from "@auth0/auth0-react";
import { API } from "aws-amplify";

const Message = () => {

  const [msgs, setMsgs] = useState([]);

  const fetchData = async () => {
    API.get('message', '/messages?user_id=99')
      .then(response => {
        setMsgs(response);
      })
      .catch(error => {
        console.log(error.response);
    });
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <BrowserRouter>
      <div className="email-app row">
        <div className="col-lg-3 pb-5">
        <nav>
            <Link to="/compose" className="btn btn-danger btn-block"><i className="fa fa-rocket"></i> New Email</Link>
            <ul className="nav">
                <li className="nav-item">
                    <Link to="/inbox" className="nav-link">
                      <i className="fa fa-inbox"></i>
                      Inbox 
                      <span className="badge">{msgs.length}</span>
                    </Link>
                </li>
                <li className="nav-item">
                    <Link to="/sent" className="nav-link"><i className="fa fa-rocket"></i> Sent</Link>
                </li>
                <li className="nav-item">
                    <Link to="/trash" className="nav-link"><i className="fa fa-trash-o"></i> Trash</Link>
                </li>
            </ul>
        </nav>
        </div>
        <div className="col-lg-9 pb-5">
            <Route path="/inbox">
              <Inbox msgs={msgs}/>
            </Route> 
            <Route path="/compose" component={ComposeMail} />
            
          </div>
      </div>
    </BrowserRouter>
    );
  };

export default Message;