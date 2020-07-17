import React from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Chip from '@material-ui/core/Chip';
import Avatar from '@material-ui/core/Avatar';

import Classes from '../Classes/Classes';

const ProjectCard = (props) => {
  const { project } = props;

  const classes = Classes();

  return (
    <Card>
      <CardActionArea
        href={project.url}
        target="_blank"
        rel="noopener noreferrer"
      >
        <CardHeader title={project.name} subheader={project.fullname} />
        <CardMedia component="img" src={project.avatar_url} />
        <CardContent>
          {project.description && (
            <Typography>{project.description}</Typography>
          )}
          {project.contributors?.map((contributor, index) => (
            <Chip
              className={classes.chip}
              key={contributor.github_handle}
              avatar={<Avatar src={contributor.avatar_url} />}
              label={
                contributor.name ? contributor.name : contributor.github_handle
              }
              variant="outlined"
              color={index % 2 === 0 ? 'primary' : 'secondary'}
            />
          ))}
        </CardContent>
      </CardActionArea>
    </Card>
  );
};

export default ProjectCard;
