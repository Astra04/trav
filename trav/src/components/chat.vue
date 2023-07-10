

<template>
    <div class="window">
        <div id="background-container"></div>
        <form @submit.prevent="sendMessage">
            <label for="destination">Destination:</label>
            <input v-model="destination" id="destination" type="text">

            <label for="duration">Duration (in days):</label>
            <input v-model.number="duration" id="duration" type="number">

            <label for="reason">Reason:</label>
            <input v-model="reason" id="reason" type="text" />

            <button type="submit">Send</button>
        </form>
        <div class="response">
            <p>{{ response }}</p>
        </div>

    </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    name: 'App',
    data() {
        return {
            destination: '',
            duration: '',
            reason: '',
            response: '',

        };
    },

    computed: {
        isFormInvalid() {
            return (
                this.destination === '' ||
                this.duration === '' ||
                this.reason === ''
            );
        },
    },
    mounted() {
        this.initializeBackground();
    },
    methods: {
        sendMessage() {
            if (this.hasResponse) {
                return; // Do nothing if a response is already loaded
            }

            if (this.isFormInvalid) {
                alert('Form is invalid. Please enter all fields.');
                return;
            }

            if (this.isLoading) {
                alert('Loading. Please wait.');
                return;
            }

            const message = `Given the hotels and tourist destinations in ${this.destination}, if I'm staying for ${this.duration} days, for ${this.reason} reasons please help me find good activities and destinations in a list javascript array of Activities for activites and Destinations for destinations and also use google maps places to suggest possible hotels with good reviews and a live link of their google map location coordinates links finally suggested budget based on ${this.duration} days and current foreign exchange in its own arrarray called budget `;
            const url = 'http://127.0.0.1:8080/chat';
            const queryParams = new URLSearchParams();
            queryParams.append('human_msg', message);
            const fullUrl = `${url}?${queryParams.toString()}`;

            this.isLoading = true;

            fetch(fullUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({}), // Add an empty body to satisfy the server's expectation
            })
                .then((response) => response.json())
                .then((data) => {
                    this.response = data.response;
                })
                .finally(() => {
                    this.isLoading = false;
                });
        },
        initializeBackground() {
            $("#background-container").vegas({
                slides: [
                    { src: require('./assets/backgrounds/(3).jpg') },
                    { src: require('./assets/backgrounds/(4).jpg') },
                    { src: require('./assets/backgrounds/(5).jpg') },
                    { src: require('./assets/backgrounds/(6).jpg') },
                    { src: require('./assets/backgrounds/(7).jpg') },
                    { src: require('./assets/backgrounds/(8).jpg') },
                    { src: require('./assets/backgrounds/(9).jpg') },
                    { src: require('./assets/backgrounds/(10).jpg') },
                    // Add more images here
                ],
                delay: 5000, // Delay between slide transitions in milliseconds
                transition: 'fade', // Transition effect
                transitionDuration: 2000, // Duration of the transition effect in milliseconds
                animation: 'random', // Animation effect for the transition
                animationDuration: 2000, // Duration of the animation effect in milliseconds
            });
        },

    },
}
</script>

<style>
.response {
    margin-top: 20px;
    font-family: Arial, sans-serif;
    font-size: 14px;
}

.response-list {
    list-style-type: disc;
    margin-left: 20px;
}

.response-list li {
    margin-bottom: 5px;
}
</style>