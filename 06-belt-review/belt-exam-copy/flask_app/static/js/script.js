const jokeForm = document.getElementById('joke-form');
const jokesContainer = document.getElementById('jokes-container');

function createJokeCard(data) {
  return `
  <div class="card shadow mb-3">
    <div class="card-body">
      <p class="display-5">${data.content}</p>
    </div>
    <div class="card-footer d-flex gap-2 justify-content-end">
      <a href="/jokes/{{ joke.id }}" class="btn btn-primary">View</a>
      <form action="/groans/create" method="post">
        <input type="hidden" name="user_id" value="{{ session.user_id }}" />
        <input type="hidden" name="joke_id" value="{{ joke.id }}" />
        <button type="submit" class="btn btn-primary {{ 'disabled' if joke.is_groaned_at_by(session.user_id) else '' }}">Groan</button>
      </form>
    </div>
  </div>
  `;
}

async function createJoke() {
  const formData = new FormData(jokeForm);
  const response = await fetch('http://localhost:5001/api/jokes/create', {
    method: 'POST',
    body: formData,
  });

  const data = await response.json();
  console.log(data);
  const jokeCard = createJokeCard(data);
  jokesContainer.innerHTML += jokeCard;
}

jokeForm.addEventListener('submit', function (e) {
  e.preventDefault();
  console.log('handle submit is running');
  createJoke();
});
