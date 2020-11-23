import React, { Fragment } from "react";
import Loading from "../components/Loading";
import Registration from "../components/Registration";
let history = useHistory();
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

export const RegistrationComponent = ({match, location}) => {
  const { loginWithRedirect } = useAuth0();

  return (
    <Fragment>
    <Registration/>
  </Fragment>
  );
};

export default withAuthenticationRequired(RegistrationComponent, {
  onRedirecting: () => <Loading />,
});