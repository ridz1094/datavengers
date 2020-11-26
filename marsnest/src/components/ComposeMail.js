import React, { useState } from "react";
import "./Message.css";
import { useAuth0 } from "@auth0/auth0-react";
import { API } from "aws-amplify";


const ComposeMail = () => {
    const { user } = useAuth0();
    const [isLoading, setIsLoading] = useState(false);
    const [isSent, setIsSent] = useState(false)
    const [email, setEmail] = useState('')
    const [content, setContent] = useState('')

    const submit = e => {
        e.preventDefault()
        setIsLoading(true);
        try {
            API.post("message", "/messages", {
                body: {
                    id: "7",
                    sender_id: "91",
                    receiver_id: "99",
                    message: content
                }
              }).then(() => setIsSent(true))
          } catch (e) {
            setIsLoading(false);
          }
      }

    return (
        <form onSubmit={submit}>
            <p></p>
            
            { isSent && ( <div className="alert alert-success" role="alert">Message sent!</div>)}
            
            <div className="form-row mb-3">
                <label htmlFor="to" className="col-2 col-sm-1 col-form-label">To:</label>
                <div className="col-10 col-sm-11">
                    <input type="email" value={email} 
                        onChange={e => setEmail(e.target.value)} 
                        className="form-control" id="to" 
                        placeholder="Type email"/>
                </div>
            </div>
       
            <div className="row">
                <div className="col-sm-11 ml-auto">
                    <div className="form-group mt-4">
                        <textarea 
                            className="form-control" 
                            value={content} 
                            onChange={e => setContent(e.target.value)} 
                            id="message" name="body" rows="12" 
                            placeholder="Click here to compose"></textarea>
                    </div>
                    <div className="form-group">
                        <button type="submit" className="btn btn-success">Send</button>
                        <button type="submit" className="btn btn-danger">Discard</button>
                    </div>
                </div>
            </div>
        </form>
      )
    };

export default ComposeMail;