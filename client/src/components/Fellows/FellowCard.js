import React from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardHeader from '@material-ui/core/CardHeader';
import Avatar from '@material-ui/core/Avatar';
import CardContent from '@material-ui/core/CardContent';
import Chip from '@material-ui/core/Chip';

import Classes from '../Classes/Classes';

const FellowCard = (props) => {
  const { fellow } = props;

  const classes = Classes();

  return (
    <Card>
      <CardActionArea
        href={fellow.profile_url}
        target="_blank"
        rel="noopener noreferrer"
      >
        <CardHeader
          avatar={<Avatar src={fellow.avatar_url} />}
          title={fellow.name ? fellow.name : fellow.github_handle}
          subheader={fellow.location && fellow.location}
        />
        <CardContent>
          {fellow.teams
            .filter((team) => team.name.startsWith('Pod '))
            .map((team, index) => (
              <Chip
                className={classes.chip}
                key={team.name}
                avatar={<Avatar src={team.avatar_url} />}
                label={`${team.name}${
                  team.description && ` - ${team.description}`
                }`}
                variant="outlined"
                color={index % 2 === 0 ? 'primary' : 'secondary'}
              />
            ))}
        </CardContent>
      </CardActionArea>
    </Card>
  );
};

export default FellowCard;
