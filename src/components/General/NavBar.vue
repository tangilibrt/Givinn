<template>
  <header>
    <section :class="toggled ? 'header header-toggled' : 'header'">
      <nav>

        <ul>
          <router-link to="/"><img src="/assets/logo.png" alt="logo" class="logo fixed-logo"></router-link>

          <div :class="toggled ? 'banner-toggled' : 'banner'">
            <li>
                <router-link class="textBanner" to="/">Accueil</router-link>
            </li>
            <li>
              <router-link class="textBanner" to="/concours">Concours</router-link>
            </li>
            <li>
              <router-link class="textBanner" to="/QuiSommesNous">Qui Sommes Nous ?</router-link>
            </li>
          </div>
          <div :class="toggled ? 'toggled' : ''" @click="toggledBar" class="cross">
            <div :class="toggled ? 'toggled' : ''"></div>
            <div :class="toggled ? 'toggled' : ''"></div>
          </div>
        </ul>
      </nav>
    </section>
  </header>
</template>

<script>
import { ref } from 'vue';
export default {
  name: 'NavBar',
  setup() {
    const toggled = ref(false);

    const toggledBar = () => {
      toggled.value = !toggled.value;
      if (toggled.value) {
        document.querySelector('header').style.height = '50vh';

      } else {
        document.querySelector('header').style.height = '75px';
      }
    };

    return {
      toggled,
      toggledBar
    };
  },
  computed: {
    isBlack() {
      return this.$route.path === '/concours';
    }
  }
};
</script>

<style lang="scss">
.logo {
  width: 100px;
  height: 100px;
}

.fixed-logo {
  position: fixed;
  top: 20px;
  left: 8%;
  z-index: 1000000000000;
}

header {
  width: 100%;
  position: fixed;
  overflow: hidden;
  z-index: 10;
  padding: 0;
  height: 75px;
}

.header {
  background-color: transparent;
  position: relative;
}

.banner,
.banner-toggled {
  background-color: #fff;
  position: absolute;
  height: 75px;
  width: 0;
  right: 0;
  top: 0;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  overflow: hidden;
  border-bottom: 1px solid lightgrey;
}

.banner-toggled {
  animation: apparitionWidth 0.4s ease-out forwards;
}

.textBanner {
  color: #000;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1rem;
  transition: all 0.3s ease-in-out;
}

nav ul {
  display: flex;
  list-style: none;
  justify-content: space-evenly;
  align-items: center;
}

nav ul li {
  margin-right: 10px;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}

nav ul li a:hover {
  text-decoration: underline;
}

.cross {
  position: absolute;
  top: 30px;
  right: 75px;
  cursor: pointer;
  height: 50px;
  &.toggled {
    transform: translateY(0.59vh); // 5px / 850px * 100vh
  }

  div {
    height: 4px; //0.3vw / 4px  / 850px * 100vh
    width: 5vh; // 43px / 1500px * 100vw
    background:linear-gradient(45deg, #405de6, #5851db, #833ab4, #c13584, #e1306c, #fd1d1d);
    transition: all 0.3s;
    &.toggled {
      background-color: #000;
    }
  }

  :first-child {
    transform: rotate(0);
    &.toggled {
      transform: rotate(45deg) translateX(5px) translateY(0.2vh); // 3px / 1500px * 100vw, 3px / 850px * 100vh
    }
  }

  :last-child {
    transform: rotate(0) translateY(1.18vh); // 10px / 850px * 100vh
    &.toggled {
      transform: rotate(135deg) translateX(-0.10vw) translateY(-0.2vh); // 3px / 1500px * 100vw, 3px / 850px * 100vh
    }
  }
}

@keyframes apparitionWidth {
  0% {
    width: 0;
  }
  100% {
    width: 100%;
  }
}

@media screen and (max-width: 1245px) {
  .logo {
    width: 75px;
    height: 75px;
  }

  .fixed-logo {
    left: 5%;
  }

  .cross {
    right: 50px;
  }
}

@media screen and (max-width: 960px) {
  .banner-toggled{
    max-width: 80%;
    right: 10%;
  }
}

@media screen and (max-width: 780px){
  .banner-toggled{
    max-width: 100%;
    right: 0;
    flex-flow: column;
    height: 50vh;
    align-items: center;
  }
  .header-toggled{
    height: 50vh;
  }
  header{
    height: 50vh;
  }

}

@media screen and (max-width: 450px){ /* mobile */
  .cross {
    top: 30px;
    right: 20px;
    /* TODO: increase the height of the divs of the cross */
  }
  .logo {
    width: 60px;
    height: 60px;
  }

}



</style>
