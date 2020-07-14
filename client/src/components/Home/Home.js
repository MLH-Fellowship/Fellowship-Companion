import React from 'react';
import Grid from '@material-ui/core/Grid';

import Cover from '../Cover/Cover';

const Home = () => (
  <Grid container direction="column" alignItems="center" spacing={2}>
    <Grid item>
      <Cover />
    </Grid>
  </Grid>
);

export default Home;
