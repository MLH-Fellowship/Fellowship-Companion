import React, { Fragment } from 'react';
import useScrollTrigger from '@material-ui/core/useScrollTrigger';
import Slide from '@material-ui/core/Slide';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import HomeIcon from '@material-ui/icons/Home';
import TimelineIcon from '@material-ui/icons/Timeline';
import GroupIcon from '@material-ui/icons/Group';
import ListIcon from '@material-ui/icons/List';

import Classes from '../Classes/Classes';

const HideOnScroll = (props) => {
  const { children } = props;

  const trigger = useScrollTrigger();

  return (
    <Slide appear={false} direction="down" in={!trigger}>
      {children}
    </Slide>
  );
};

const NavigationBar = (props) => {
  const classes = Classes();

  return (
    <Fragment>
      <HideOnScroll {...props}>
        <AppBar color="secondary">
          <Toolbar>
            <IconButton edge="end" color="inherit" href="/">
              <HomeIcon />
            </IconButton>
            <div className={classes.grow} />
            <IconButton edge="end" color="inherit" href="/contributions">
              <TimelineIcon />
            </IconButton>
            <IconButton edge="end" color="inherit" href="/fellows">
              <GroupIcon />
            </IconButton>
            <IconButton edge="end" color="inherit" href="/projects">
              <ListIcon />
            </IconButton>
          </Toolbar>
        </AppBar>
      </HideOnScroll>
      <Toolbar />
    </Fragment>
  );
};

export default NavigationBar;
