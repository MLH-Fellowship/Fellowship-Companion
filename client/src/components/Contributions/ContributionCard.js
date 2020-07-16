import React from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardHeader from '@material-ui/core/CardHeader';
import Avatar from '@material-ui/core/Avatar';
import CardContent from '@material-ui/core/CardContent';

import { distanceToNow } from '../../logic/date-time';

const ContributionCard = (props) => {
  const { info } = props;

  return (
    <Card>
      <CardActionArea href={info.url} target="_blank" rel="noopener noreferrer">
        <CardHeader
          avatar={<Avatar src={info.user.avatar_url} />}
          title={info.title}
          subheader={distanceToNow(info.createdAt)}
        />
        <CardContent>{info.description}</CardContent>
      </CardActionArea>
    </Card>
  );
};

export default ContributionCard;
