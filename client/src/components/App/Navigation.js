import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';

import Home from '../Home/Home';

import Contributions from '../Contributions/Contributions';
import Fellows from '../Fellows/Fellows';
import Projects from '../Projects/Projects';

const Navigation = () => (
  <Switch>
    <Route exact path="/" component={Home} />

    <Route exact path="/contributions" component={Contributions} />
    <Route exact path="/fellows" component={Fellows} />
    <Route exact path="/projects" component={Projects} />

    <Redirect to="/" />
  </Switch>
);

export default Navigation;
