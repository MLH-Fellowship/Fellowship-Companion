import React, { useState, useEffect, Fragment } from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Grid from '@material-ui/core/Grid';
import Pagination from '@material-ui/lab/Pagination';

import { getUsers } from '../../logic/api';

import Classes from '../Classes/Classes';

import FellowCard from './FellowCard';

import ErrorSnackbar from '../ErrorSnackbar/ErrorSnackbar';

const Fellows = () => {
  const classes = Classes();

  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    window.scrollTo(0, 0);
    setLoading(true);
    getUsers(page)
      .then((data) => setData(data))
      .catch((error) => setError(error))
      .finally(() => setLoading(false));
  }, [page]);

  return (
    <Fragment>
      {loading && <LinearProgress color="secondary" />}
      <div className={classes.root}>
        <Grid container direction="row" alignItems="center" spacing={2}>
          <Grid item>
            <Grid container justify="center" spacing={2}>
              {data?.results.map((fellow) => (
                <Grid item key={fellow.github_handle} sm={6} xs={12}>
                  <FellowCard fellow={fellow} />
                </Grid>
              ))}
            </Grid>
          </Grid>
          <Grid item>
            <Pagination
              count={data?.total_pages}
              color="secondary"
              onChange={(event, page) => setPage(page)}
            />
          </Grid>
        </Grid>
      </div>
      {error && <ErrorSnackbar error={error} />}
    </Fragment>
  );
};
export default Fellows;
