import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';

import Home from '../Home/Home';

import Contributions from '../Contributions/Contributions';

const Navigation = () => (
  <Switch>
    <Route exact path="/" component={Home} />

    <Route exact path="/contributions" component={Contributions} />

    <Redirect to="/" />
  </Switch>
);

export default Navigation;
