<template>
    <div id="app">
      <NavBar />
      <main>
        <router-view />
      </main>
    </div>

</template>

<script>
import NavBar from './components/General/NavBar.vue';
export default {
    name: 'App',
    components: {
        NavBar
    }
}
</script>

<style lang="scss">
*, *::after, *::before {
    padding: 0px;
    margin: 0;
    box-sizing: border-box;
    font-family: "Inter", sans-serif;
}

body {
    background-color: white;
    color: #fff;
  overflow-x: hidden;
  overflow-y: visible;
}

@import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');

</style>