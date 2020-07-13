import React from 'react';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

const theme = createMuiTheme({
  palette: {
    primary: {
      light: '#5cc8ae',
      main: '#00be94',
      dark: '#008a6b',
    },
    secondary: {
      light: '#ffcd6a',
      main: '#f8ba2b',
      dark: '#e2a121',
    },
  },
});

const App = () => (
  <ThemeProvider theme={theme}>
    <CssBaseline />
  </ThemeProvider>
);

export default App;
