import React, {useState, useEffect} from "react";
import { Container, Row, Col } from "reactstrap";

import Loading from "../components/Loading";
import { API } from "aws-amplify";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

export const ProfileComponent = () => {
  const { user } = useAuth0();
  const [userFromSys, setuser] = useState([]);
  const [isLoading, setLoading] = useState(true);
  // const [currentUser, setUser] = useState({});
  const fetchData = async () => {
    var url = "/users/email?email=" + user.email;
    API.get('application', url)
    .then(response => {
        setuser(response.data);
        setLoading(false);
    })
    .catch(error => {
        console.log(error.response);
    });
}
useEffect(() => {
  fetchData();
}, []);

if (isLoading) {
  return <Loading />;
}

  return (
      <Container className="mb-5">
        <Row className="align-items-center profile-header mb-5 text-center text-md-left">
          <Col md={2}>
            <img
              src={user.picture}
              alt="Profile"
              className="rounded-circle img-fluid profile-picture mb-3 mb-md-0"
            />
          </Col>
          <Col md>
            <h2>{userFromSys.name}</h2>
            <p className="lead text-muted">{userFromSys.name}</p>
          </Col>
        </Row>
        <Row>     
          <div className="col-lg-4 pb-5">
            <div className="card h-100">
              <h4 className="card-header">About me</h4>
              <div className="card-body">
                <p className="card-text">Excited to be a Martian!</p>
              </div>
              <div className="card-footer">
              </div>
            </div>
          </div>
          <div className="col-lg-8 pb-5">
              <form className="row">
                  <div className="col-md-12">
                      <div className="form-group">
                          <label htmlFor="email"><b>E-mail Address</b></label>
                          <input className="form-control" type="email" id="email" value={userFromSys.email} disabled="" readonly/>
                      </div>
                  </div>
                  <div className="col-md-12">
                      <div className="form-group">
                          <label htmlFor="phoneno" ><b>Mobile Number</b></label>
                          <input className="form-control" type="text" id="phoneno" value={userFromSys.mobile} disabled="" readonly/>
                      </div>
                  </div>
                  <div className="col-md-12">
                      <div className="form-group">
                          <label htmlFor="phoneno" ><b>Date Of Birth</b></label>
                          <input className="form-control" type="text" id="dob" value={userFromSys.dob} disabled="" readonly/>
                      </div>
                  </div>
                  <div className="col-12">
                      <hr className="mt-2 mb-3"/>
                      <div className="d-flex flex-wrap justify-content-between align-items-center">
                          <div className="custom-control custom-checkbox d-block">
                              
                          </div>
                          <button className="btn btn-style-1 btn-primary" type="button" data-toast="" data-toast-position="topRight" data-toast-type="success" data-toast-icon="fe-icon-check-circle" data-toast-title="Success!" data-toast-message="Your profile updated successfuly.">Update Profile</button>
                      </div>
                  </div>
              </form>
          </div>
        </Row>
      </Container>
  );
};

export default withAuthenticationRequired(ProfileComponent, {
  onRedirecting: () => <Loading />,
});
