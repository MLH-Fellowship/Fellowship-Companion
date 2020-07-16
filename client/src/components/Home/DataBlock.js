import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import CircularProgress from '@material-ui/core/CircularProgress';
import Button from '@material-ui/core/Button';

import CountUp from 'react-countup';

import Classes from '../Classes/Classes';

const DataBlock = (props) => {
  const { colorClass, firstString, count, secondString, href, title } = props;

  const classes = Classes();

  return (
    <div className={`${classes.root} ${classes.block} ${colorClass}`}>
      <Grid container direction="column" alignItems="center" spacing={2}>
        <Grid item>
          <Typography variant="body1">{firstString}</Typography>
        </Grid>
        <Grid item>
          {count ? (
            <Typography variant="h3" component="h2" color="secondary">
              <CountUp end={count} separator=" " />
            </Typography>
          ) : (
            <CircularProgress color="secondary" />
          )}
        </Grid>
        <Grid item>
          <Typography variant="body1">{secondString}</Typography>
        </Grid>
        <Grid item>
          <Button variant="contained" color="secondary" href={href}>
            {title}
          </Button>
        </Grid>
      </Grid>
    </div>
  );
};

export default DataBlock;
