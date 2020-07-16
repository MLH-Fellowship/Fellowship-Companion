import React, { useState, useEffect, Fragment } from 'react';
import Grid from '@material-ui/core/Grid';

import { getOverview } from '../../logic/api';

import Classes from '../Classes/Classes';

import Cover from './Cover';
import LinesOfCode from './LinesOfCode';
import Fellows from './Fellows';
import Projects from './Projects';

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
            <Cover />
          </Grid>
          <Grid item sm={6} xs={12}>
            <LinesOfCode linesOfCode={data?.loc} />
          </Grid>
          <Grid item sm={6} xs={12}>
            <Fellows fellows={data?.fellows} />
          </Grid>
          <Grid item sm={6} xs={12}>
            <Projects projects={data?.projects} />
          </Grid>
        </Grid>
      </div>
      {error && <ErrorSnackbar error={error} />}
    </Fragment>
  );
};

export default Home;
