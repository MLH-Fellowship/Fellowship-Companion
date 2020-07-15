import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

import CountUp from 'react-countup';

import Classes from '../Classes/Classes';

const Fellows = () => {
  const classes = Classes();

  return (
    <div
      className={`${classes.root} ${classes.block} ${classes.lightPrimaryBackgroundColor}`}
    >
      <Grid container direction="column" alignItems="center" spacing={2}>
        <Grid item>
          <Typography variant="body1">The Fellowship has</Typography>
        </Grid>
        <Grid item>
          <Typography variant="h3" component="h2" color="secondary">
            <CountUp end={123} separator=" " />
          </Typography>
        </Grid>
        <Grid item>
          <Typography variant="body1">Fellows!</Typography>
        </Grid>
        <Grid item>
          <Button variant="contained" color="secondary" href="/fellows">
            Fellows
          </Button>
        </Grid>
      </Grid>
    </div>
  );
};

export default Fellows;
