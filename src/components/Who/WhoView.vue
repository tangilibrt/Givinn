<template>
  <div id = "container">
    <h1>Qui sommes-nous ?</h1>
    <div id="profileContainer" >
      <div class="profile profile1" @mouseover="expand(1)" @mouseout="normal">
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Thomas</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile2" @mouseover="expand(2)" @mouseout="normal" >
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Eden</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile3" @mouseover="expand(3)" @mouseout="normal" >
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Tanguy</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile4" @mouseover="expand(4)" @mouseout="normal" >
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Ame</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile5" @mouseover="expand(5)" @mouseout="normal">
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Théo</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WhoView",
  methods: {
    expand(column) {
      const profiles = document.getElementsByClassName('profile');
      for (let i = 0; i < profiles.length; i++) {
        profiles[i].classList.remove("shrink", "expand");
      }
      profiles[column - 1].classList.add("expand");
      for (let i = 0; i < profiles.length; i++) {
        if (i !== column - 1) {
          profiles[i].classList.add("shrink");
        }
      }
    },
    normal() {
      const profiles = document.getElementsByClassName('profile');
      for (let i = 0; i < profiles.length; i++) {
        profiles[i].classList.remove("shrink", "expand");
      }
    }
  }
}
</script>

<style scoped lang="scss">

#container {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

h1 {
  color: black;
  font-size: 50px;
}

#profileContainer {
  display: flex;
  border: none;
  overflow: hidden;
  width: 80%;
  height: 50%;
  background-color: transparent;
  box-shadow: 0 0 10px 0px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  // we select the childs except the last and first one
  > div:not(:first-child) {
    border-left: 1px solid lightgrey;
  }
}

.profile {
  position: relative;
  width: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: white;
  transition: width 0.5s;
  color: black;
  img {
    position: absolute;
    top: 15%;
    width: 10vw;
    height: 10vw;
  }

  h2 {
    font-size: 20px;
    margin-top: 1.5vh;
    margin-bottom: 1vh;
    position: absolute;
    top: 70%;
    left: 50%;
    transform: translateX(-50%);
    transition: font-size .5s ease-in-out, top .5s ease-in-out;

  }

  .text {
    opacity: 0;
    font-size: 15px;
    margin: 0;
    position: absolute;
    top: 80%;
    left: 50%;
    transform: translateX(-50%);
    transition: opacity .7s ease-in-out 0.3s;
  }

}

.expand {
  width: 40%;
  .text {
    opacity: 1;
  }
  h2 {
    font-size: 30px;
    top: 60%;
  }
}

.shrink {
  width: 15%;
}

</style>