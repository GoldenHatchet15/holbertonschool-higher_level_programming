document.addEventListener('DOMContentLoaded', () => {
  const headerElement = document.querySelector('header');
  const redHeaderElement = document.getElementById('red_header');

  redHeaderElement.addEventListener('click', () => {
    headerElement.classList.add('red');
  });
});
