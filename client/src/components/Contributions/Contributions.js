import React, { useState, useEffect, Fragment } from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Grid from '@material-ui/core/Grid';
import Pagination from '@material-ui/lab/Pagination';

import { getEvents } from '../../logic/api';

import Classes from '../Classes/Classes';

import ContributionCard from './ContributionCard';

import ErrorSnackbar from '../ErrorSnackbar/ErrorSnackbar';

const Contributions = () => {
  const classes = Classes();

  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    window.scrollTo(0, 0);
    setLoading(true);
    getEvents(page)
      .then((data) => {
        setData(data);
        console.log(data);
      })
      .catch((error) => setError(error))
      .finally(() => setLoading(false));
  }, [page]);

  const getInfo = (contribution) => {
    const info = {};
    info.type = contribution.type;
    info.createdAt = contribution.created_at;
    const name = contribution.user.name
      ? contribution.user.name
      : contribution.user.github_handle;
    let eventTitle;
    switch (contribution.type) {
      case 'IS':
        info.title =
          contribution.action === 'opened' ? 'New issue' : 'Closed issue';
        info.url = contribution.issue.url;
        eventTitle = `${contribution.issue.title} (#${contribution.issue.number})`;
        break;
      case 'PR':
        info.title =
          contribution.action === 'opened'
            ? 'New pull request'
            : 'Merged pull request';
        info.url = contribution.pull_request.url;
        eventTitle = `${contribution.pull_request.title} (#${contribution.pull_request.number})`;
        break;

      default:
        break;
    }
    info.description = `${name} ${contribution.action} "${eventTitle}" on ${contribution.repository.organization}/${contribution.repository.name}`;
    info.user = contribution.user;
    info.repository = contribution.repository;

    return info;
  };

  return (
    <Fragment>
      {loading && <LinearProgress color="secondary" />}
      <div className={classes.root}>
        <Grid
          container
          direction="row"
          alignItems="center"
          justify="center"
          spacing={2}
        >
          <Grid item>
            <Grid container justify="center" spacing={2}>
              {data?.results.map((contribution) => {
                const info = getInfo(contribution);

                return (
                  <Grid item key={info.description} sm={6} xs={12}>
                    <ContributionCard info={info} />
                  </Grid>
                );
              })}
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
export default Contributions;
