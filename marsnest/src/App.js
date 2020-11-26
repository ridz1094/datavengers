import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import { Container } from "reactstrap";

import Loading from "./components/Loading";
import NavBar from "./components/NavBar";
import Registration from "./components/Registration";
import Home from "./views/Home";
import Profile from "./views/Profile";
import Message from "./views/Message";
import { useAuth0 } from "@auth0/auth0-react";
import history from "./utils/history";


// styles
import "./App.css";

// fontawesome
import initFontAwesome from "./utils/initFontAwesome";
initFontAwesome();

const App = () => {
  const { isLoading, error } = useAuth0();

  if (error) {
    return <div>Oops... {error.message}</div>;
  }

  if (isLoading) {
    return <Loading />;
  }

  return (
    <Router history={history}>
      <div id="app" className="d-flex flex-column h-100 App">
        <NavBar />
        <Container className="flex-grow-1 mt-5">
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/profile" component={Profile} />
            <Route path="/message" component={Message} />
            <Route path="/register" component={Registration} />
            <Route path="/inbox" component={Message} />
            <Route path="/compose" component={Message} />
          </Switch>
        </Container>
      </div>
    </Router>
  );
};

export default App;
