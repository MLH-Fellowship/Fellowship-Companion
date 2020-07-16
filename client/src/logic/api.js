export const getOverview = () => fetchApi('/overview', { method: 'GET' });

export const getEvents = (page) =>
  fetchApi(`/events?page=${page}`, { method: 'GET' });

const fetchApi = (path, fetchOptions = {}) => {
  const BASE_API_URL = 'https://agsaurabh.pythonanywhere.com/api/v1';

  return fetch(
    `${BASE_API_URL}${path}`,
    Object.assign({}, fetchOptions, {
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
    })
  ).then((response) => response.json());
};
