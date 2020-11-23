import React, { Fragment } from "react";
import Loading from "../components/Loading";
import Message from "../components/Message";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

export const MessageComponent = () => {
  const { user } = useAuth0();

  return (
    <Fragment>
    <Message />
    <hr />
  </Fragment>
  );
};

export default withAuthenticationRequired(MessageComponent, {
  onRedirecting: () => <Loading />,
});