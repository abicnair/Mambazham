let playerId = null;
let gameId = null;
let isJudge = false;

async function createGame() {
    const response = await fetch('http://localhost:5000/create_game', {
        method: 'POST'
    });
    const data = await response.json();
    document.getElementById('game-id').value = data.game_id;
}

async function joinGame() {
    const playerName = document.getElementById('player-name').value;
    gameId = document.getElementById('game-id').value;
    
    const response = await fetch('http://localhost:5000/join_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            game_id: gameId,
            player_name: playerName
        })
    });
    
    const data = await response.json();
    if (data.player_id) {
        playerId = data.player_id;
        document.getElementById('login-screen').style.display = 'none';
        document.getElementById('game-screen').style.display = 'block';
        renderHand(data.hand);
        startGamePolling();
    }
}

function renderHand(cards) {
    const handDiv = document.getElementById('player-hand');
    handDiv.innerHTML = '';
    cards.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.innerHTML = `
            <div class="card-text">${card.text}</div>
            <div class="card-translation">${card.translation}</div>
        `;
        cardElement.onclick = () => playCard(card.id);
        handDiv.appendChild(cardElement);
    });
}

function startGamePolling() {
    setInterval(async () => {
        const response = await fetch(`http://localhost:5000/game_state?game_id=${gameId}`);
        const gameState = await response.json();
        updateGameState(gameState);
    }, 1000);
}

function updateGameState(gameState) {
    // Update green card
    document.getElementById('green-card').innerHTML = `
        <div class="card-text">${gameState.green_card.text}</div>
        <div class="card-translation">${gameState.green_card.translation}</div>
    `;
    
    // Update scores
    document.getElementById('scores').innerHTML = Object.entries(gameState.scores)
        .map(([pid, score]) => `Player ${pid}: ${score}`)
        .join('<br>');
        
    isJudge = gameState.current_judge === playerId;
}

async function playCard(cardId) {
    if (isJudge) return;
    
    await fetch('http://localhost:5000/play_card', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            game_id: gameId,
            player_id: playerId,
            card_id: cardId
        })
    });
} 