import React from 'react';
import Typography from '@material-ui/core/Typography';
import FavoriteIcon from '@material-ui/icons/Favorite';
import Link from '@material-ui/core/Link';
import GitHubIcon from '@material-ui/icons/GitHub';

import Classes from '../Classes/Classes';

const Footer = () => {
  const classes = Classes();

  return (
    <div className={classes.footer}>
      <Typography variant="caption">
        Made with{' '}
        <FavoriteIcon
          className={classes.verticalAlignMiddle}
          fontSize="small"
          color="secondary"
        />{' '}
        by{' '}
        <Link
          href="https://github.com/AlbertoPdRF/"
          target="_blank"
          rel="noopener noreferrer"
          color="secondary"
        >
          <strong>@AlbertoPdRF</strong>
        </Link>
        ,{' '}
        <Link
          href="https://github.com/LakshyaKhatri/"
          target="_blank"
          rel="noopener noreferrer"
          color="secondary"
        >
          <strong>@LakshyaKhatri</strong>
        </Link>
        , and{' '}
        <Link
          href="https://github.com/SaurabhAgarwala/"
          target="_blank"
          rel="noopener noreferrer"
          color="secondary"
        >
          <strong>@SaurabhAgarwala</strong>
        </Link>{' '}
        on{' '}
        <Link
          href="https://github.com/MLH-Fellowship/Fellowship-Companion/"
          target="_blank"
          rel="noopener noreferrer"
          color="secondary"
        >
          <GitHubIcon
            className={classes.verticalAlignMiddle}
            fontSize="small"
            color="secondary"
          />
        </Link>
      </Typography>
    </div>
  );
};

export default Footer;
