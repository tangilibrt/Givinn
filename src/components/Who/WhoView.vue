<template>
  <div id = "container">
    <h1>Qui sommes-nous ?</h1>
    <WhoTitle infos="L'EQUIPE GIV'INN" />
    <div id="profileContainer" >
      <div class="profile profile1" @mouseover="expand(1)" @mouseout="normal">
        <img src="/assets/thomas_chibi.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Thomas</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile2" @mouseover="expand(2)" @mouseout="normal" >
        <img src="/assets/eden_chibi.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Eden</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile3" @mouseover="expand(3)" @mouseout="normal" >
        <img src="/assets/tanguy_chibi.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Tanguy</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile4" @mouseover="expand(4)" @mouseout="normal" >
        <img src="/assets/ame_chibi.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Ame</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
      <div class="profile profile5" @mouseover="expand(5)" @mouseout="normal">
        <img src="/assets/theo_chibi.png" alt="Avatar" class="avatar">
        <div class="containerInfos">
          <div class="content">
            <h2 class="name">Théo</h2>
            <a class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl. Donec euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, eget aliquam nisl nisl eget nisl.</a>
          </div>
        </div>
      </div>
    </div>
    <WhoTitle infos="POURQUOI GIV'INN ?" />
    <div id="containerText">
      <h3 style="color: black">
        Parce qu'on a tous quelque chose de Remy de Ratatouille.
        <br>
        <br>
        Oui oui, nous avons tous un petit côté Rat à la recherche des petites économies de tous les jours, à essayer d'obtenir des choses gratuitement...
        <br>
        <br>
        Eh bien c'est exactement ce que Giv'inn va vous permettre de faire !
        <br>
        <br>
        Notre Auberge est équipée de notre algorithme d'IA Quantique (oui oui, rien que ça), vous allez pouvoir retrouver tous les concours disponible sur Instagram, les trier selon vos centre d'intérets, tout en restant protégé des arnaques puisse que notre programme de Machine Learning à propulsion nucléaire va vous permettre de déterminer si le concours est fiable ou non.
        <br>
        <br>
        Alors, armez vous de vos meilleur likes, story et commentaires, asseyez vous confortablement et attendez que Giv'inn vous apporte vos cadeaux de Noël (ou pas, des fois il faut juste se faire plaisir roooh) comme sur un plateau.<br>
      </h3>
      <h2>
        <br>
        <br>
        On dit merci qui ?... Jacq- Giv'Inn !</h2>
      <img src="/assets/tavernPole.png" alt="tavern Pole" id="tavernPole">

    </div>
    <div id="containerSocial">
      <div class="social">
        <a href="https://www.instagram.com/givinn.fr/" target="_blank">
          <img src="https://www.clipartmax.com/png/full/25-256843_instagram-logo-[new]-vector-eps-free-download-logo-instagram-logo-vector.png" alt="Instagram" class="icon" />
        </a>
        <a href="https://www.facebook.com/Givinn-102105585288765" target="_blank">
          <img src="https://www.flaticon.com/svg/static/icons/svg/1384/1384060.svg" alt="Facebook" class="icon" />
        </a>
        <a href="https://twitter.com/Givinn1" target="_blank">
          <img src="https://pic.onlinewebfonts.com/svg/img_152340.png" alt="Twitter" class="icon" />
        </a>
        <a href="https://www.linkedin.com/company/givinn/" target="_blank">
          <img src="https://www.flaticon.com/svg/static/icons/svg/1384/1384057.svg" alt="Linkedin" class="icon" />
        </a>
      </div>
    </div>

  </div>

</template>

<script>
import WhoTitle from "@/components/Who/WhoTitle.vue";

export default {
  name: "WhoView",
  components: {WhoTitle},
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
  height: 250vh;
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
  height: 50vh;
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
    top: 10%;
    height: 50%;
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

#containerText {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 70%;
  height: 50vh;
  background-color: transparent;
  margin-top: 5vh;
  flex-direction: column;
  h3 {
    font-size: 20px;
    color: black;
    text-align: center;
  }
  h2 {
    font-size: 30px;
    color: black;
    text-align: center;
  }
}

#tavernPole {
  width: 20%;
  position: absolute;
  top: 120vh;
  right: 0;
}

#containerSocial {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 70%;
  height: 10vh;
  background-color: transparent;
  margin-top: 5vh;
  flex-direction: column;
  .social {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    .icon {
      width: 5vw;
      height: 5vw;
      margin: 1vw;
      transition: transform .5s ease-in-out;
      &:hover {
        transform: scale(1.2);
      }
    }
  }
}

@media screen and (max-width: 780px) {
  #container {
    height: 300vh;
  }
  #profileContainer {
    width: 90%;
    height: 40vh;
  }
  #containerText {
    width: 90%;
    height: 60vh;
  }

  #containerSocial {
    width: 90%;
    height: 20vh;
  }


}

@media screen and (max-width: 550px) {
  #container {
    height: 300vh;
  }
  #profileContainer {
    width: 90%;
    height: 40vh;
  }
  #containerText {
    width: 90%;
    height: 60vh;
  }
  #containerSocial {
    width: 90%;
    height: 20vh;
  }
}

@media screen and (max-width: 480px){
  #tavernPole {
    opacity: 0;
  }
  .containerInfos {
    margin-bottom: 170px;
  }
  #containerSocial {
    margin-top: 80px;
  }
}

@media screen and (max-width: 400px) {
  #container {
    height: 350vh;
  }
  #profileContainer {
    width: 90%;
    height: 40vh;
  }

  #tavernPole {
    opacity: 0;
  }

  .profile {
    h2 {
      transform: rotate(90deg);
      left: 0;
      transition: left .5s ease-in-out 0.5s, font-size .5s ease-in-out;
    }


  }
  .expand {
    h2 {
      left: 50%;
    }
  }

  #containerText {
    width: 90%;
    height: 70vh;

  }
  #tavernPole {
    width: 40%;
    top: 150vh;
  }
  #containerSocial {
    width: 90%;
    height: 20vh;
    display: flex;
    flex-flow: column;
  }
}

@media screen and (max-width: 375px){
  .expand {
    h2 {
      left: 40%;
    }
  }
  #containerSocial {
    opacity: 0;
  }
}

</style>