document.addEventListener('DOMContentLoaded', () => {
  const headerElement = document.querySelector('header');
  const redHeaderElement = document.getElementById('red_header');

  redHeaderElement.addEventListener('click', () => {
    headerElement.style.color = '#FF0000';
  });
});
