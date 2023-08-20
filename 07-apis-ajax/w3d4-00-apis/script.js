const jokesContainer = document.getElementById('jokes-container');
const jokeForm = document.getElementById('joke-form');
jokeForm.addEventListener('submit', handleSubmit);

function buildJokeCard(data) {
  return `
  <div class="card shadow mb-3">
    <div class="card-body">${data.joke}</div>
  </div>
  `;
}

async function getDadJoke() {
  const response = await fetch('https://icanhazdadjoke.com/', {
    headers: {
      Accept: 'application/json',
    },
  });

  const data = await response.json();
  console.log(data);
  const jokeCard = buildJokeCard(data);
  jokesContainer.innerHTML += jokeCard;
}

function handleSubmit(evt) {
  evt.preventDefault();
  getDadJoke();
}

/* let num = 0;
console.log(num);

function greet() {
  console.log('hello world');
  num = 2;
}

function wait() {
  setTimeout(greet, 2000);
}

wait();
console.log('goodbye world');
console.log(num); */
