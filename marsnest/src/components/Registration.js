import React, { useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { API } from "aws-amplify";

const Registration = props => {
  const {user} = useAuth0(),
    [isLoading, setIsLoading] = useState(false),
    [isRegistered, setIsRegistered] = useState(false),
    [dob, setDob] = useState(""),
    [mobile, setMobile] = useState("");
  
  return (
    <form>
      <center>
        <div className="col-md-6">
          <label htmlFor="to" className="col-md-6 col-sm-1 col-form-label">
            Mobile:
          </label>
          <div className="col-md-6 col-sm-11">
            <input
              onChange={e => {
                setMobile(e.target.value);
              }}
              className="form-control"
              type="number"
              id="mobile"
              value={mobile}
              placeholder="Enter Mobile"
            />
          </div>
        </div>

        <div className="col-md-6">
          <label htmlFor="to" className="col-md-6 col-sm-1 col-form-label">
            DOB:
          </label>
          <div className="col-md-6 col-sm-11">
            <input
              className="form-control"
              onChange={e => {
                setDob(e.target.value);
              }}
              type="text"
              id="dob"
              value={dob}
              placeholder="Enter DOB"
            />
          </div>
        </div>
        <br/>
          <button
            type="button"
            onClick={(e) => {
              e.preventDefault();
              setIsLoading(true);
              window.location.replace("https://marsnest.us.auth0.com/continue" + props.location.search);
              try {
                API.post("application", "users", {
                  body: {
                    email: user.email,
                    name: user.name,
                    dob: dob,
                    mobile: mobile
                    // ,token: user.token
                  }
                }).then(() => {
                  console.log("on click-----")
                  setIsRegistered(true)
                  
                });
              } catch (e) {
                console.log("on else block click-----")
                console.log(e)
                setIsLoading(false);
              }
            }}>
            Signup
          </button>
      </center>
    </form>
  );
};

export default Registration;
