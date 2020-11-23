import React from "react";
import { useParams } from "react-router";


class Registration extends React.Component {
  render() {
    return <div className="text-center hero my-5">
    <h1 className="mb-4">Fill your details</h1>

    <p className="lead">
        <input type="text" id="receiver" name="receiver"/>
      <button type="button" onClick={() => {
        window.location.replace("https://marsnest.us.auth0.com/continue" + this.props.location.search)
      }}>Register</button>
    </p>
  </div>;
  }
}



export default Registration;