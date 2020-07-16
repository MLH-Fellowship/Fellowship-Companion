import React, { useState, useEffect, Fragment } from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';

import { getOverview } from '../../logic/api';

import Classes from '../Classes/Classes';

import DataBlock from './DataBlock';

import ErrorSnackbar from '../ErrorSnackbar/ErrorSnackbar';

const Home = () => {
  const classes = Classes();

  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    getOverview()
      .then((data) => setData(data))
      .catch((error) => setError(error));
  }, []);

  return (
    <Fragment>
      <div className={classes.root}>
        <Grid container spacing={2}>
          <Grid item sm={6} xs={12}>
            <div className={`${classes.root} ${classes.block}`}>
              <Grid
                container
                direction="column"
                alignItems="center"
                spacing={2}
              >
                <Grid item>
                  <Typography variant="h2" component="h1" color="secondary">
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
                      <strong>MLH Fellowship</strong>
                    </Link>{' '}
                    activities!
                  </Typography>
                </Grid>
              </Grid>
            </div>
          </Grid>
          <Grid item sm={6} xs={12}>
            <DataBlock
              colorClass={classes.darkPrimaryBackgroundColor}
              firstString="The Fellows have contributed"
              count={data?.loc}
              secondString="lines of code to Open Source Software projects!"
              href="/contributions"
              title="Contributions"
            />
          </Grid>
          <Grid item sm={6} xs={12}>
            <DataBlock
              colorClass={classes.lightPrimaryBackgroundColor}
              firstString="The Fellowship has"
              count={data?.fellows}
              secondString="Fellows!"
              href="/fellows"
              title="Fellows"
            />
          </Grid>
          <Grid item sm={6} xs={12}>
            <DataBlock
              colorClass={classes.mainPrimaryBackgroundColor}
              firstString="The Fellowship supports"
              count={data?.projects}
              secondString="Open Source Software projects!"
              href="/projects"
              title="Projects"
            />
          </Grid>
        </Grid>
      </div>
      {error && <ErrorSnackbar error={error} />}
    </Fragment>
  );
};

export default Home;
