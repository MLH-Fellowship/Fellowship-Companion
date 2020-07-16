export const getOverview = () => fetchApi('/overview', { method: 'GET' });

const fetchApi = (path, fetchOptions = {}) => {
  const BASE_API_URL = 'http://34.69.147.19:8000/api/v1';

  return fetch(
    `${BASE_API_URL}${path}`,
    Object.assign({}, fetchOptions, {
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
    })
  ).then((response) => response.json());
};
