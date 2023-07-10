<template>
    <main class="ask">
        <div>
            <!-- User Profile and Preferences -->
            <h2>User Profile and Preferences</h2>
            <form @submit.prevent="submitForm">
                <label for="travelStyle">Preferred Travel Style:</label>
                <select v-model="profile.travelStyle" id="travelStyle">
                    <option value="adventure">Adventure</option>
                    <option value="luxury">Luxury</option>
                    <option value="backpacking">Backpacking</option>
                </select>

                <label for="clothingStyle">Clothing Style:</label>
                <input v-model="profile.clothingStyle" id="clothingStyle" type="text">

                <label for="requirements">Specific Requirements:</label>
                <textarea v-model="profile.requirements" id="requirements"></textarea>

                <label for="destination">Destination:</label>
                <input v-model="trip.destination" id="destination" type="text">

                <label for="startDate">Start Date:</label>
                <input v-model="trip.startDate" id="startDate" type="date">

                <label for="duration">Duration (in days):</label>
                <input v-model.number="trip.duration" id="duration" type="number">

                <button type="submit" @click="suggestIdeas">Suggest Ideas</button>
            </form>

            <div v-if="response" class="response">
                <h3>Response:</h3>
                <p>{{ response }}</p>
            </div>
        </div>

        <!-- Response -->
        <div class="block">
            <div v-if="response" class="response">
                <h3>Response:</h3>
                <p>{{ response }}</p>
            </div>

        </div>


    </main>
</template>
<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
    name: 'Home',
    data() {
        return {
            response: ''
        };
    },

    setup() {
        // User Profile and Preferences data
        let response = {};
        const profile = ref({
            travelStyle: '',
            clothingStyle: '',
            requirements: ''
        });

        // Trip Details data
        const trip = ref({
            destination: '',
            startDate: '',
            duration: 0
        });
        // Handle form submission for User Profile and Preferences
        const submitProfile = () => {
            // Perform any necessary data validation or API calls here
            console.log('Profile submitted:', profile.value);
        };

        // Handle form submission for Trip Details
        const submitTrip = () => {
            // Perform any necessary data validation or API calls here
            console.log('Trip submitted:', trip.value);
        };

        // Handle suggestion button click
        const suggestIdeas = () => {
            const { destination, startDate, duration } = trip.value;
            const { travelStyle, clothingStyle, requirements } = profile.value;

            const message = `Please recommend ideas on how I can visit ${destination} from ${startDate} for ${duration} days if my travel style is ${travelStyle}, clothing style is ${clothingStyle}, and I have the following requirements: ${requirements}`;

            // Print the message or use it for further processing
            console.log(message);

            // Define the endpoint URL
            const url = 'http://127.0.0.1:8080/chat';
            const queryParams = new URLSearchParams();
            queryParams.append('human_msg', message);
            const fullUrl = `${url}?${queryParams.toString()}`;

            // Send the POST request to the endpoint
            fetch(fullUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({}), // Add an empty body to satisfy the server's expectation
            })
                .then((response) => response.json())
                .then((data) => {
                    // Handle the response
                    console.log('Received response:', data);
                    // Update the response variable
                    response = data;
                })

                .catch((error) => {
                    // Handle the error
                    console.error('Error:', error);
                });
        };




        return {
            profile,
            trip,
            submitProfile,
            submitTrip,
            suggestIdeas
        };
    }
};
</script>
<style>
.ask {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.form-container {
    max-width: 500px;
    padding: 40px;
    border: 1px solid #e9e9e9;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 30px;
}

.form {
    display: grid;
    gap: 20px;
}

label {
    font-weight: bold;
    font-size: 16px;
}

input,
textarea,
select {
    width: 100%;
    padding: 12px;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-size: 16px;
}

button {
    background-color: #007bff;
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    text-transform: uppercase;
}

.response {
    margin-top: 30px;
}

@media (max-width: 500px) {
    .form-container {
        width: 100%;
        padding: 20px;
    }

    h2 {
        font-size: 20px;
    }

    label {
        font-size: 14px;
    }

    input,
    textarea,
    select {
        font-size: 14px;
    }

    button {
        font-size: 14px;
        padding: 10px 20px;
    }
}
</style>