import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import { Auth0Provider } from "@auth0/auth0-react";
import config from "./auth_config.json";
import history from "./utils/history";
import { Amplify } from 'aws-amplify';
import base_config from './base_config';
import application_config from './application_config';
import twitter_config from './twitter_config';


Amplify.configure({
  API: {
    endpoints: [
      {
        name: "message",
        endpoint: base_config.apiGateway.URL,
        region: base_config.apiGateway.REGION
      },
      {
        name: "application",
        endpoint: application_config.apiGateway.URL,
        region: application_config.apiGateway.REGION
      },
      {
        name: "twitter",
        endpoint: twitter_config.apiGateway.URL,
        region: twitter_config.apiGateway.REGION
      },
    ]
  }
});

const onRedirectCallback = (appState) => {
  history.push(
    appState && appState.returnTo
      ? appState.returnTo
      : window.location.pathname
  );
};

ReactDOM.render(
  <Auth0Provider
    domain={config.domain}
    clientId={config.clientId}
    audience={config.audience}
    redirectUri={window.location.origin}
    onRedirectCallback={onRedirectCallback}
  >
    <App />
  </Auth0Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
