import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

function handleClick()
{

}

const Registration = () => (

  <div className="text-center hero my-5">
    <h1 className="mb-4">Fill your details</h1>

    <p className="lead">
        <input type="text" id="receiver" name="receiver"/>
      <button type="button" onClick={handleClick}>Register</button>
    </p>
  </div>
);

export default Registration;