import React, { useState } from 'react';
import Portal from '@material-ui/core/Portal';
import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';

const ErrorSnackbar = (props) => {
  const { error } = props;

  const [open, setOpen] = useState(true);

  return (
    <Portal>
      <Snackbar
        message={error.toString()}
        open={open}
        action={
          <IconButton color="inherit" onClick={() => setOpen(false)}>
            <CloseIcon />
          </IconButton>
        }
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'right',
        }}
      />
    </Portal>
  );
};

export default ErrorSnackbar;
