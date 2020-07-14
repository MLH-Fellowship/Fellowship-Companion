import React from 'react';
import Grid from '@material-ui/core/Grid';

import Classes from '../Classes/Classes';

import Cover from './Cover';
import LinesOfCode from './LinesOfCode';
import Fellows from './Fellows';

const Home = () => {
  const classes = Classes();

  return (
    <div className={classes.root}>
      <Grid container spacing={2}>
        <Grid item sm={6} xs={12}>
          <Cover />
        </Grid>
        <Grid item sm={6} xs={12}>
          <LinesOfCode />
        </Grid>
        <Grid item sm={6} xs={12}>
          <Fellows />
        </Grid>
      </Grid>
    </div>
  );
};

export default Home;
