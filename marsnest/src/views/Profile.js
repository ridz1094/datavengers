import React from "react";
import { Container, Row, Col } from "reactstrap";

import Loading from "../components/Loading";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

export const ProfileComponent = () => {
  const { user } = useAuth0();

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
            <h2>{user.nickname}</h2>
            <p className="lead text-muted">{user.name}</p>
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
                  <div className="col-md-6">
                      <div className="form-group">
                          <label htmlFor="username">Name</label>
                          <input className="form-control" type="text" id="username" value={user.name} />
                      </div>
                  </div>
                  <div className="col-md-6">
                      <div className="form-group">
                          <label htmlFor="nickname">Nick Name</label>
                          <input className="form-control" type="text" id="nickname" value={user.nickname} />
                      </div>
                  </div>
                  <div className="col-md-6">
                      <div className="form-group">
                          <label htmlFor="email">E-mail Address</label>
                          <input className="form-control" type="email" id="email" value={user.email} disabled=""/>
                      </div>
                  </div>
                  <div className="col-md-6">
                      <div className="form-group">
                          <label htmlFor="phoneno">Phone Number</label>
                          <input className="form-control" type="text" id="phoneno" value="" />
                      </div>
                  </div>
                  <div className="col-md-6">
                      <div className="form-group">
                          <label htmlFor="password">New Password</label>
                          <input className="form-control" type="password" id="password"/>
                      </div>
                  </div>
                  <div className="col-md-6">
                      <div className="form-group">
                          <label htmlFor="confirmpassword">Confirm Password</label>
                          <input className="form-control" type="password" id="confirmpassword"/>
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
