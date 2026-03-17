let playerId = 1; // Start with Player 1
let playedCount = 1;

function nextTurn() {
    console.log("playedCount", playedCount);
    playerId = (playerId % 4) + 1; // Cycle through players 1-4
    console.log("playerId", playerId);
    updateGameState();
    playedCount++;
}

function updateGameState() {
    fetch('/game_state')
        .then(response => response.json())
        .then(gameState => {
            // Set initial player to be the one after the judge
            if (playerId === gameState.current_judge && playedCount <= 3) {
                playerId = (gameState.current_judge % 4) + 1;
            }

            // Update player header
            const playerHeader = document.getElementById('current-player-header');
            playerHeader.innerHTML = `Player ${playerId}'s Turn ${gameState.current_judge === playerId ? '(JUDGE)' : ''}`;
            
            console.log("gameState", gameState);
            // Update green card
            document.getElementById('green-card').innerHTML = `
                <div class="card-text">${gameState.green_card.text}</div>
            `;
            // <div class="card-translation">${gameState.green_card.translation}</div>
            
            // Update player hand
            console.log("playerId", playerId);
            console.log("gameState.current_judge", gameState.current_judge);
            if (playerId !== gameState.current_judge) {

                const hand = gameState.players[playerId].hand;
                const handDiv = document.getElementById('player-hand');
                handDiv.innerHTML = `
                    <div class="cards-container">
                        ${hand.map(card => `
                            <div class="card ${gameState.current_judge === playerId ? 'disabled' : ''}" 
                                onclick="${gameState.current_judge !== playerId ? `selectCard(this, ${card.id})` : ''}"
                                data-card-id="${card.id}">
                                <div class="card-text">${card.text}</div>
                            </div>
                        `).join('')}
                    </div>
                    `;
                    // <div class="card-translation">${card.translation}</div>

                }
            else {
                const handDiv = document.getElementById('player-hand');
                handDiv.innerHTML = '';
            }   
            
            // Update played cards (only visible to judge)
            const playedCardsDiv = document.getElementById('played-cards');
            if (gameState.current_judge === playerId) {
                console.log("current_judge", gameState.current_judge);
                playedCardsDiv.innerHTML = '<h2 style="display: block; width: 100%; text-align: center;">Choose Winner</h2>';
                console.log("gameState", gameState);
                console.log("played_cards", gameState.played_cards);
                Object.entries(gameState.played_cards).forEach(([pid, card]) => {
                    console.log("played_cards", pid, card);
                    const cardElement = document.createElement('div');
                    cardElement.className = 'card';
                    cardElement.innerHTML = `
                        <div class="card-text">${card.text}</div>
                        <div class="card-translation">${card.translation}</div>
                    `;
                    cardElement.onclick = () => judgeRound(parseInt(pid));
                    playedCardsDiv.appendChild(cardElement);
                });
            } else {
                playedCardsDiv.innerHTML = ``;
            }
            
            // Update scores and check for winner
            const scoresDiv = document.getElementById('scores');
            let scoresHtml = '<div class="section-header">Scores</div>';
            Object.entries(gameState.players).forEach(([pid, player]) => {
                scoresHtml += `
                    <div class="score-entry">
                        Player ${pid}${gameState.current_judge == pid ? ' 👨‍⚖️ (JUDGE)' : ''}: ${player.score}
                        ${gameState.round_winner === parseInt(pid) ? 
                            '<div class="round-winner">🎯 Round Winner!</div>' : ''}
                        ${player.score >= 4 ? 
                            '<div class="winner-announcement">🎉 Game Winner! 🎉</div>' : ''}
                    </div>
                `;
            });
            scoresDiv.innerHTML = scoresHtml;
        });
}

function playCard(cardId) {
    console.log("playCard", cardId);
    fetch('/play_card', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            player_id: playerId,
            card_id: cardId
        })
    });
}

function judgeRound(winnerId) {
    fetch('/judge_round', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            winner_id: winnerId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Immediately update the game state to show the new scores
            updateGameState();
        }
    });
}

// Switch between players (for testing)
function switchPlayer(newPlayerId) {
    console.log("switchPlayer", newPlayerId);
    playerId = newPlayerId;
    updateGameState();
}

// Update game state every second
// setInterval(updateGameState, 1000);
updateGameState(); 

function selectCard(cardElement, cardId) {
    // Remove selected class from all cards
    document.querySelectorAll('#player-hand .card').forEach(card => {
        card.classList.remove('selected');
    });
    
    // Add selected class to clicked card
    cardElement.classList.add('selected');
    
    // Play the card
    playCard(cardId);
} 