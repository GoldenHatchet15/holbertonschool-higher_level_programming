document.addEventListener('DOMContentLoaded', () => {
  const updateHeaderElement = document.getElementById('update_header');
  const headerElement = document.querySelector('header');

  updateHeaderElement.addEventListener('click', () => {
    headerElement.textContent = 'New Header!!!';
  });
});
