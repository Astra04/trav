<template>
    <nav class="navbar">
        <div class="navbar-brand">
            <a href="">Propsa</a>
            <button class="navbar-toggler" @click="toggleMenu">
                <span></span>
                <span></span>
                <span></span>
            </button>


        </div>
        <div class="navbar-menu" :class="{ 'is-active': isMenuOpen }">
            <div class="navbar-end">
                <router-link class="navbar-item" to="/">Home</router-link>
                <router-link class="navbar-item" to="/signup">Get started</router-link>
                <router-link class="navbar-item" to="/intro">Edit</router-link>
                <router-link class="navbar-item" to="/contact">Contact</router-link>
            </div>
        </div>
    </nav>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';

export default {
    name: 'Navbar',
    setup() {
        const isMenuOpen = ref(false);

        function toggleMenu() {
            isMenuOpen.value = !isMenuOpen.value;
        }

        function handleClickOutside(event) {
            if (
                isMenuOpen.value &&
                event.target.closest('.navbar') === null
            ) {
                isMenuOpen.value = false;
            }
        }

        function handleScroll() {
            isMenuOpen.value = false;

        }

        onMounted(() => {
            document.addEventListener('click', handleClickOutside);
            window.addEventListener('scroll', handleScroll);
        });

        onBeforeUnmount(() => {
            document.removeEventListener('click', handleClickOutside);
            window.removeEventListener('scroll', handleScroll);
        });

        return {
            isMenuOpen,
            toggleMenu,
        };
    },
};
</script>

<style>
body {
    padding-top: 4.5rem;
    font-family: 'Arial Narrow Bold', sans-serif;
}

.navbar {
    padding: 1rem;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    background: transparent;
    backdrop-filter: blur(100px);
    z-index: 1000;
    font-size: 1.2rem;
}

.navbar-brand {
    display: flex;
    font-size: 1.6rem;
    font-weight: bold;
    z-index: 10000;
}

.navbar-toggler {
    float: right;
    border: none;
    background-color: transparent;
    cursor: pointer;
    display: block;
    margin-left: auto;
}

.navbar-toggler span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: var(--primary-alt);
    margin-bottom: 5px;
}

.navbar-menu {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
    display: none;
    animation: appear 3s;
}

.navbar-menu.is-active {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-wrap: wrap;
    width: fit-content;
}

.navbar-end {
    display: flex;
    justify-content: center;
    align-items: center;
}

.navbar-item {

    color: var(--dark);
    font-weight: bold;
    text-decoration: none;
    display: block;
    padding: 0.5rem 1rem;
    animation: appear 0.2s;

}

@keyframes appear {

    50% {
        opacity: 0.5;
    }

    100% {
        opacity: 1;
    }


}

.navbar-item:hover {
    backdrop-filter: 20px;
    font-size: 17px;
}

@media (max-width: 768px) {
    navbar-menu {
        width: fit-content;
        position: absolute;
        top: 100%;
        left: 0;
        background-color: var(--primary-alt);
        z-index: 1000;
        display: none;
    }

    .navbar-menu.is-active {
        display: block;
        transition: 2s;
    }

    .navbar-end {
        font-size: 0.6em;
        justify-content: center;
        content: normal;
        background: #fff;

    }

    .navbar-item {

        color: var(--light);
        font-weight: bold;
        text-decoration: none;
        display: block;
        padding: 0.5rem 1rem;
        border-bottom: 1px solid #ccc;
    }

    .navbar-item:hover {
        background-color: #f5f5f5;
    }

}
</style>
