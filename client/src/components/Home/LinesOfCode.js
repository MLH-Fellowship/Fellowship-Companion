import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

import CountUp from 'react-countup';

import Classes from '../Classes/Classes';

const LinesOfCode = () => {
  const classes = Classes();

  return (
    <div
      className={`${classes.root} ${classes.block} ${classes.darkPrimaryBackgroundColor}`}
    >
      <Grid container direction="column" alignItems="center" spacing={2}>
        <Grid item>
          <Typography variant="body1">The Fellows have contributed</Typography>
        </Grid>
        <Grid item>
          <Typography variant="h3" component="h2" color="secondary">
            <CountUp end={1234567890} separator=" " />
          </Typography>
        </Grid>
        <Grid item>
          <Typography variant="body1">
            lines of code to Open Source Software projects!
          </Typography>
        </Grid>
        <Grid item>
          <Button variant="contained" color="secondary" href="/contributions">
            Contributions
          </Button>
        </Grid>
      </Grid>
    </div>
  );
};

export default LinesOfCode;
