import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';

const Navigation = () => (
  <Switch>
    <Route exact path="/" />

    <Redirect to="/" />
  </Switch>
);

export default Navigation;
