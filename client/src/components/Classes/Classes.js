import { makeStyles } from '@material-ui/core/styles';

const Classes = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(2),
    [theme.breakpoints.down('sm')]: {
      maxWidth: '100vw',
    },
    [theme.breakpoints.up('md')]: {
      maxWidth: '960px',
      margin: 'auto',
    },
    display: 'flex',
    textAlign: 'center',
    alignItems: 'center',
  },
  block: {
    [theme.breakpoints.up('sm')]: {
      height: '400px',
    },
  },
  darkPrimaryBackgroundColor: {
    backgroundColor: theme.palette.primary.dark,
  },
  lightPrimaryBackgroundColor: {
    backgroundColor: theme.palette.primary.light,
  },
  mainPrimaryBackgroundColor: {
    backgroundColor: theme.palette.primary.main,
  },
  grow: {
    flexGrow: 1,
  },
  footer: {
    position: 'relative',
    bottom: theme.spacing(1),
    width: '100%',
    textAlign: 'center',
  },
  verticalAlignMiddle: {
    verticalAlign: 'middle',
  },
  chip: {
    margin: theme.spacing(0.5),
  },
}));

export default Classes;
