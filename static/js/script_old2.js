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
            if (playerHeader) {
            playerHeader.innerHTML = `Player ${playerId}'s Turn ${gameState.current_judge === playerId ? '(JUDGE)' : ''}`;
            }
            console.log("gameState", gameState);
            // Update green card
            const greenCard = document.getElementById('green-card');
            if (greenCard && gameState.green_card) {
                greenCard.innerHTML = `
                    <div class="card-text">${gameState.green_card.text}</div>
                `;
            }
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
            if (scoresDiv) {
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
            }
            // Add this player list update code
            const playerList = document.getElementById('player-list');
            if (playerList && gameState.players) {
                playerList.innerHTML = Object.entries(gameState.players)
                    .map(([id, player]) => `
                        <div class="player-item ${gameState.current_judge == id ? 'judge' : ''}">
                            <span class="player-name">${player.name}</span>
                            <span class="player-status">${player.score} points</span>
                            ${gameState.current_judge == id ? '<span class="judge-badge">Judge</span>' : ''}
                        </div>
                    `).join('');
            }

            console.log("gameState", gameState);
            console.log("playerList", playerList);

            // Keep your existing updateUI call
            updateUI(gameState);
        })
        .catch(error => console.error('Error updating game state:', error));
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

// Session management functions
function createGame() {
    fetch('/create_game', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        // Auto-fill the session ID for the creator
        document.getElementById('session-id-input').value = data.session_id;
        document.getElementById('game-code').textContent = `Game Code: ${data.session_id}`;
        
        // Show both sections for the creator
        document.getElementById('create-game-section').style.display = 'none';
        document.getElementById('join-game-section').style.display = 'block';
        
        // Add a message to indicate they still need to join
        document.getElementById('join-message').textContent = 
            'Your game has been created! Enter your name below to join.';
    });
}

function joinGame() {
    const sessionId = document.getElementById('session-id-input').value;
    const playerName = document.getElementById('player-name-input').value;
    
    console.log('Joining game with session ID:', sessionId);
    
    if (!playerName) {
        alert('Please enter your name');
        return;
    }
    
    fetch('/join_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            session_id: sessionId,
            player_name: playerName
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Join game error:', data.error);
            alert(data.error);
            return;
        }
        console.log('Successfully joined game:', data);
        playerId = data.player_id;
        localStorage.setItem('gameSessionId', sessionId);
        localStorage.setItem('playerId', playerId);
        
        // Hide both create and join sections
        document.querySelector('.game-options').style.display = 'none';
        document.getElementById('game-section').style.display = 'block';
        startGameStatePolling();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to join game. Please try again.');
    });
}

function startGameStatePolling() {
    // setInterval(updateGameState, 1000);
}

function updateUI(gameState) {
    // Update player list
    const playerList = document.getElementById('player-list');
    if (playerList && gameState.players) {
        playerList.innerHTML = Object.entries(gameState.players)
            .map(([id, player]) => `
                <div class="player-item ${gameState.current_judge == id ? 'judge' : ''}">
                    <span class="player-name">${player.name}</span>
                    <span class="player-status">${player.score} points</span>
                    ${gameState.current_judge == id ? '<span class="judge-badge">Judge</span>' : ''}
                </div>
            `).join('');
    }

    // Update game state based on whether game has started
    if (gameState.game_started) {
        document.getElementById('waiting-room').style.display = 'none';
        document.getElementById('game-board').style.display = 'block';
        
        // Update green card
        if (gameState.green_card) {
            document.getElementById('green-card').innerHTML = `
                <div class="card green">
                    <div class="card-inner">
                        <div class="card-front">
                            <div class="card-text">${gameState.green_card.text}</div>
                            <button class="flip-button">Show Translation</button>
                        </div>
                        <div class="card-back">
                            <div class="card-translation">${gameState.green_card.translation}</div>
                            <button class="flip-button">Show Malayalam</button>
                        </div>
                    </div>
                </div>
            `;
        }

        // Update played cards
        const playedCardsDiv = document.getElementById('played-cards');
        if (gameState.current_judge === playerId && typeof gameState.played_cards === 'object') {
            playedCardsDiv.innerHTML = Object.entries(gameState.played_cards)
                .map(([pid, card]) => `
                    <div class="card" onclick="judgeRound(${pid})">
                        <div class="card-inner">
                            <div class="card-front">
                                <div class="card-text">${card.text}</div>
                                <button class="flip-button">Show Translation</button>
                            </div>
                            <div class="card-back">
                                <div class="card-translation">${card.translation}</div>
                                <button class="flip-button">Show Malayalam</button>
                            </div>
                        </div>
                    </div>
                `).join('');
        } else {
            playedCardsDiv.innerHTML = `<div class="played-count">Cards played: ${
                typeof gameState.played_cards === 'number' ? gameState.played_cards : 0
            }</div>`;
        }

        // Update player's hand
        const handDiv = document.getElementById('player-hand');
        if (gameState.players[playerId] && gameState.players[playerId].hand) {
            handDiv.innerHTML = gameState.players[playerId].hand
                .map(card => `
                    <div class="card ${gameState.current_judge === playerId ? 'disabled' : ''}" 
                         onclick="${gameState.current_judge !== playerId ? `playCard(${card.id})` : ''}">
                        <div class="card-inner">
                            <div class="card-front">
                                <div class="card-text">${card.text}</div>
                                <button class="flip-button">Show Translation</button>
                            </div>
                            <div class="card-back">
                                <div class="card-translation">${card.translation}</div>
                                <button class="flip-button">Show Malayalam</button>
                            </div>
                        </div>
                    </div>
                `).join('');
        }

        // Add flip functionality to all cards
        document.querySelectorAll('.flip-button').forEach(button => {
            button.onclick = (e) => {
                e.stopPropagation();  // Prevent card play/judge action
                const card = e.target.closest('.card');
                card.classList.toggle('flipped');
            };
        });
    } else {
        document.getElementById('waiting-room').style.display = 'block';
        document.getElementById('game-board').style.display = 'none';
    }
}

function startGame() {
    console.log('Start game button clicked');  // Debug log
    
    // Get the session info
    const sessionId = document.getElementById('session-id-input').value;
    console.log('Current session ID:', sessionId);  // Debug log
    
    fetch('/start_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin'  // Ensure cookies are sent
    })
    .then(response => {
        console.log('Server response:', response.status);  // Debug log
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.error || 'Failed to start game');
            });
        }
        return response.json();
    })
    .then(data => {
        console.log('Game started successfully:', data);
        updateGameState();
    })
    .catch(error => {
        console.error('Error starting game:', error);
        alert('Failed to start game: ' + error.message);
    });
}