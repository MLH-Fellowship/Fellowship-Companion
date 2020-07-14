import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';

import Classes from '../Classes/Classes';

const Cover = () => {
  const classes = Classes();

  return (
    <div className={classes.root}>
      <Grid container direction="column" alignItems="center" spacing={2}>
        <Grid item>
          <Typography variant="h2" component="h1" color="primary">
            Fellowship Companion
          </Typography>
        </Grid>
        <Grid item>
          <Typography variant="subtitle1">
            Welcome to the web application that let's you peek into the{' '}
            <Link
              href="https://fellowship.mlh.io/"
              target="_blank"
              rel="noopener noreferrer"
              color="secondary"
            >
              MLH Fellowship
            </Link>{' '}
            activities!
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default Cover;
