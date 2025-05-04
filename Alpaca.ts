// script.ts
const messageArea = document.getElementById('messageArea') as HTMLDivElement;
const userInput = document.getElementById('userInput') as HTMLInputElement;
const sendButton = document.getElementById('sendButton') as HTMLButtonElement;

sendButton.addEventListener('click', sendMessage);

userInput.addEventListener('keyup', (event: KeyboardEvent) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

async function sendMessage() {  // Make sendMessage async
    const message = userInput.value.trim();
    if (message !== '') {
        appendMessage(message, 'user');
        userInput.value = '';

        try {
            const response = await fetch('/api/chat', { // Fetch from your API
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            const botReply = data.reply;
            appendMessage(botReply, 'bot');
        } catch (error) {
            console.error("Error fetching from API:", error);
            appendMessage("Error communicating with the bot.", 'bot'); // Display error to the user
        }
    }
}

function appendMessage(message: string, sender: 'user' | 'bot') {
    // ... (same as previous example)
}