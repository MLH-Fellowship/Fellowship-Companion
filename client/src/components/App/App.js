import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

import Navigation from './Navigation';

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
  <BrowserRouter>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Navigation />
    </ThemeProvider>
  </BrowserRouter>
);

export default App;
