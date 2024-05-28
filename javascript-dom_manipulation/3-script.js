document.addEventListener('DOMContentLoaded', () => {
  const headerElement = document.querySelector('header');
  const toggleHeaderElement = document.getElementById('toggle_header');

  toggleHeaderElement.addEventListener('click', () => {
    if (headerElement.classList.contains('red')) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    } else {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    }
  });
});
