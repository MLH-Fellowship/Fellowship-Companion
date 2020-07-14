import { makeStyles } from '@material-ui/core/styles';

const Classes = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(2, 1),
    [theme.breakpoints.up('md')]: {
      padding: theme.spacing(3),
      paddingBottom: theme.spacing(2),
    },
    width: '100vw',
    display: 'flex',
    textAlign: 'center',
  },
}));

export default Classes;
