import React, { useState, useEffect } from "react";
import "./Tweet.css";
import Loading from "./Loading";
import { useAuth0 } from "@auth0/auth0-react";
import { API } from "aws-amplify";

const Tweet = () => {
  
  const [content, setContent] = useState('')
  const [isLoading, setIsLoading] = useState(true);
  const [tweets, setTweets] = useState([]);
  const [isSent, setIsSent] = useState(false)

  const fetchData = async () => {
    await API.get('twitter', 'tweet/show')
      .then(response => {
        setTweets(response);
        setIsLoading(false);
      })
      .catch(error => {
        console.log(error.response);
    });
  }

  const submit = e => {
    e.preventDefault()
    setIsLoading(true);
    try {
        API.post("twitter", "tweet/post", {
            body: {
                message: content
            }
          }).then(() => {
            setIsSent(true);
            fetchData();
            setContent('');
          })
      } catch (e) {
        setIsLoading(false);
      }
  }


  useEffect(() => {
    fetchData();
  }, []);

  if (isLoading) {
    return <Loading />;
  }

  return (
    <div className="row">
        <div className=" col-md-6 col-xs-12 col-md-offset-3">
            <div className="panel">
                <div className="panel-heading">
                </div>
                { isSent && ( <div className="alert alert-success" role="alert">Tweet posted!</div>)}
                <div className="panel-body">
                <form onSubmit={submit}>
                    <div className="form-group">
                        <textarea 
                            className="form-control" 
                            value={content} 
                            onChange={e => setContent(e.target.value)} 
                            placeholder="Tweet your journey..." rows="3"></textarea>
                    </div>
                    <button type="submit" className="btn btn-xs fs-10 btn-bold btn-info">Tweet</button>
                </form>
                
               
                <div className="clearfix"></div>
                <hr className="margin-bottom-10"/>
                <ul className="list-group list-group-divided list-group-full"> 
                {
                    tweets.slice(0, 4).map(tweet => (
                            <li className="list-group-item">
                            <div className="media">
                                <div className="media-left">
                                    <img  src={require('../assets/avatar_male.png')} className="avatar avatar-xl no-radius" alt="..."/>
                                </div>
                                <div className="media-body">
                                <small className="text-muted pull-right">Just now</small>
                                <h4 className="media-heading">@{tweet.user.screen_name}</h4>
                                <div>{tweet.text}</div>
                                </div>
                            </div>
                            </li>
                        )
                    )
                }
                </ul>      
                </div>
            </div>
        </div>
    </div>
    );
  };

export default Tweet;