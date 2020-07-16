import { parseISO, formatDistanceToNow } from 'date-fns';

export const distanceToNow = (dateTimeString) =>
  formatDistanceToNow(parseISO(dateTimeString), { addSuffix: true });
